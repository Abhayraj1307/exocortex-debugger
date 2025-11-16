"""
LLM-powered debugger for the Exo-Cortex project.

- Runs code in a sandbox
- Extracts Python traceback
- Calls an LLM to explain + fix the error
- Supports auto-fix loops
"""

from typing import Dict, Any, Optional
import re

from exocortex.sandbox_runner import run_code_in_sandbox
from exocortex.traceback_parser import extract_traceback
from exocortex.llm_client import call_llm


# =====================================================================
# SYSTEM PROMPT
# =====================================================================

SYSTEM_PROMPT = (
    "You are an AI Python code debugger.\n\n"
    "Given the user's code and the traceback, your job is to:\n"
    "1. Explain the error in simple language.\n"
    "2. Identify the exact root cause.\n"
    "3. Provide a corrected version of the code.\n"
    "4. Briefly explain the fix.\n\n"
    "Your response MUST contain EXACTLY ONE corrected code block in this format:\n\n"
    "```python\n"
    "# corrected code here\n"
    "```\n\n"
    "Do NOT add extra python code blocks. Do NOT include shell code or text blocks.\n"
    "Write clean markdown.\n"
)


# =====================================================================
# MAIN DEBUG FUNCTION
# =====================================================================

def debug_code(code: str) -> Dict[str, Any]:
    """
    Run code in a sandbox → parse traceback → ask LLM how to fix.

    Returns:
        {
            "success": bool,
            "stderr": str,
            "traceback": str,
            "llm_response": str,
        }
    """
    # 1. Run in sandbox
    result = run_code_in_sandbox(code)
    stderr = result.get("stderr", "") or ""
    clean_tb = extract_traceback(stderr)

    # 2. Build prompt for LLM
    user_prompt = (
        "Here is the user's Python code and its traceback.\n\n"
        "CODE:\n"
        "```python\n"
        f"{code}\n"
        "```\n\n"
        "TRACEBACK:\n"
        "```\n"
        f"{clean_tb}\n"
        "```\n\n"
        "Please follow all instructions from the system prompt."
    )

    # 3. Call LLM
    try:
        llm_reply = call_llm(SYSTEM_PROMPT, user_prompt)
    except Exception as e:
        llm_reply = f"[LLM ERROR] {e}"

    return {
        "success": result.get("success", False),
        "stderr": stderr,
        "traceback": clean_tb,
        "llm_response": llm_reply,
    }


# =====================================================================
# EXTRACT CORRECTED CODE FROM LLM
# =====================================================================

def extract_corrected_code(llm_text: str) -> Optional[str]:
    """
    Extract corrected python code from the LLM markdown block.

    We expect something like:

    ```python
    # corrected code here
    ```
    """
    # Prefer ```python ... ``` block
    match = re.search(r"```python(.*?)```", llm_text, re.DOTALL | re.IGNORECASE)
    if not match:
        # Fallback to any ``` ... ``` block
        match = re.search(r"```(.*?)```", llm_text, re.DOTALL)

    if match:
        return match.group(1).strip()
    return None


# =====================================================================
# AUTO FIX LOOP
# =====================================================================

def auto_fix_loop(code: str, max_steps: int = 3) -> Dict[str, Any]:
    """
    Automatically attempts to fix code iteratively.

    Args:
        code: The original Python code as a string.
        max_steps: Maximum number of debug/fix iterations.

    Returns:
        {
            "final_code": str,
            "steps": list[dict],  # results from debug_code
            "status": "fixed" | "no_fix_found" | "max_steps_reached",
        }
    """
    current = code
    history = []

    for _ in range(max_steps):
        result = debug_code(current)
        history.append(result)

        # If code succeeded in the sandbox, we're done
        if result["success"]:
            return {
                "final_code": current,
                "steps": history,
                "status": "fixed",
            }

        # Extract suggestion from LLM
        corrected = extract_corrected_code(result["llm_response"])
        if not corrected:
            return {
                "final_code": current,
                "steps": history,
                "status": "no_fix_found",
            }

        # Apply fix for next iteration
        current = corrected

    # Max iterations reached without success
    return {
        "final_code": current,
        "steps": history,
        "status": "max_steps_reached",
    }


if __name__ == "__main__":
    # Simple manual smoke test when running the module directly
    print("Running manual test...")

    test = debug_code("print(1/0)")
    print("SUCCESS:", test["success"])
    print("TRACEBACK:\n", test["traceback"])
    print("LLM RESPONSE:\n", test["llm_response"])

    print("\n--- Auto Fix Loop ---")
    auto = auto_fix_loop("print(1/0)", max_steps=2)
    print("STATUS:", auto["status"])
    print("FINAL CODE:\n", auto["final_code"])
