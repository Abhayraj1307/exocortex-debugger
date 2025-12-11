# Exo-Cortex Debugger – AI-Assisted Python Error Explainer

## 1. What the code does

Exo-Cortex Debugger is an **AI-assisted Python debugging tool** designed to support students and beginner programmers.

At a high level, the application:

1. Accepts Python code from the user through a Streamlit web interface.
2. Executes the code in a controlled sandbox environment.
3. Captures:
   - Standard output (`stdout`),
   - Error output (`stderr`), and
   - The full Python traceback if an exception occurs.
4. Parses the traceback to identify the error type, message, and failing line.
5. Sends the relevant context (code + traceback) to a Large Language Model (LLM), such as ChatGPT, via an API client.
6. Receives:
   - A plain-language explanation of what went wrong,
   - The root cause of the error,
   - A suggested corrected version of the code, and
   - A brief explanation of the fix.
7. Displays the explanation and suggested fix to the user, who can then update and re-run their code.

The purpose of the project is to **reduce the friction of reading Python tracebacks** and help learners build intuition around common errors, rather than replacing the debugging process entirely.

---

## 2. Structure of the code

The repository is organized as follows:


EXO_CORTEX_DEBUGGER/
├── app.py                 # Streamlit UI
├── exocortex/
│   ├── __init__.py        # Package marker
│   ├── llm_client.py      # Wrapper around the LLM client (e.g., OpenAI / ChatGPT)
│   ├── llm_debugger.py    # Core debug + auto-fix orchestration logic
│   ├── sandbox_runner.py  # Safe code execution sandbox
│   └── traceback_parser.py# Extracts and cleans the traceback from stderr
├── test_sandbox.py        # Basic tests for sandbox execution
├── test_traceback.py      # Basic tests for traceback parsing
├── requirements.txt       # Python dependencies
└── .gitignore             # Ignored files (venv, caches, OS artifacts)
### 3. How to prepare to run
Prerequisites

Before running the project, ensure that you have:

Python 3.9 or newer installed.

Git installed (to clone the repository).

An LLM API key (for example, an OpenAI API key) if you want AI-generated explanations and fixes to be available.

Without a valid API key, the application can still execute code and show the raw traceback, but no AI explanation or suggested fix will be generated.

Setup steps

Clone the repository

git clone https://github.com/Abhayraj1307/exocortex-debugger.git
cd exocortex-debugger


Create and activate a virtual environment

On macOS / Linux:

python3 -m venv .venv
source .venv/bin/activate


On Windows (PowerShell):

python -m venv .venv
.venv\Scripts\activate


Install the required dependencies

pip install -r requirements.txt


Configure your LLM API key

If you are using OpenAI as the backend, set the OPENAI_API_KEY environment variable.

On macOS / Linux (for the current shell session):

export OPENAI_API_KEY="your_api_key_here"


On Windows (PowerShell, current session):

$env:OPENAI_API_KEY="your_api_key_here"


Replace "your_api_key_here" with your actual key.

For a permanent configuration, you can add this environment variable to your shell/profile configuration or system environment variables.

####4. How to run
Starting the application

With the virtual environment activated and dependencies installed, run the Streamlit application from the project root:

streamlit run app.py


This will:

Start a local Streamlit server.

Open the application in your default browser (or provide a URL such as http://localhost:8501).

Using the debugger

Open the URL shown in the terminal (typically http://localhost:8501).

Paste your Python code into the code input area.

Click the Run button.

Review the results:

If the code runs successfully, you will see the program output.

If there is an error:

The raw traceback will be displayed.

If the LLM API key is configured:

You will see a natural-language explanation of the error.

I've included a suggested corrected code snippet and a short explanation of the fix.

Optionally, copy the suggested fixed code back into the input box and rerun it to verify that the error has been resolved.
