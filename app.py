import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from exocortex.llm_debugger import debug_code, auto_fix_loop

st.set_page_config(page_title="Exo-Cortex Debugger", layout="wide")

st.title("🧠 Exo-Cortex — Self-Correcting Code Debugger")

st.markdown("""
This tool runs your code in a safe sandbox, captures errors, and lets a GPT-4o agent fix them automatically.
""")

# ------------------------
# User Code Input Panel
# ------------------------
st.subheader("🔹 Enter Python Code:")
code_input = st.text_area("Write your Python code here:", height=200)

# ------------------------
# Run Button
# ------------------------
if st.button("Run & Debug"):
    if not code_input.strip():
        st.warning("Please enter some code before running.")
    else:
        with st.spinner("Running in sandbox..."):
            result = debug_code(code_input)

        # ------------------------
        # Display Results
        # ------------------------
        st.subheader("📌 Execution Result")
        st.code(result["traceback"] if not result["success"] else "No errors!", language="text")

        st.subheader("🤖 LLM Debugger Suggestion")
        st.markdown(result["llm_response"])
