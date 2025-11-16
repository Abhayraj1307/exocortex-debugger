# 🧠 Exo-Cortex – Self-Correcting Python Code Debugger

Exo-Cortex is a **self-correcting Python debugger** powered by an LLM.  
You paste buggy Python code into a Streamlit UI, and Exo-Cortex:

1. Runs the code safely in a sandbox.
2. Captures `stdout`, `stderr`, and the Python traceback.
3. Sends the traceback + code to an LLM.
4. Returns:
   - A plain-language explanation of the error  
   - The root cause  
   - A corrected code snippet  
   - A short explanation of the fix  

It feels like an **AI rubber duck + auto-fixer** for Python.

---

## ✨ Features

- Safe, temporary sandbox for running user code
- Traceback extraction and cleanup
- LLM-generated explanation of errors
- Suggested corrected code block (parsed out of the LLM response)
- Streamlit front-end for an interactive debugging experience

---

## 🧱 Project Structure

```text
EXO_CORTEX_DEBUGGER/
├── app.py                 # Streamlit UI
├── exocortex/
│   ├── __init__.py        # Package marker
│   ├── llm_client.py      # Wrapper around OpenAI client
│   ├── llm_debugger.py    # Core debug + auto-fix logic
│   ├── sandbox_runner.py  # Safe code execution sandbox
│   └── traceback_parser.py# Extract/clean traceback from stderr
├── test_sandbox.py        # Simple tests for sandbox runner
├── test_traceback.py      # Simple tests for traceback parsing
├── requirements.txt       # Python dependencies
└── .gitignore             # Ignore venv, caches, OS files
