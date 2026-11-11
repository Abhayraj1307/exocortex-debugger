# Exo-Cortex Debugger

A Streamlit prototype that helps Python learners understand tracebacks. It captures standard output and errors, identifies the failing line, and can use an optional language model to suggest an explanation and a fix.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Use your own trusted snippets. Code runs as a subprocess with a timeout and the permissions of your local account. The temporary directory does not provide security isolation. Keep the app local and use non-sensitive snippets: enabling the model can send code and traceback context to its provider. Configure `OPENAI_API_KEY` locally for model explanations.

## Code guide

| Path | Responsibility |
| --- | --- |
| [app.py](app.py) | Streamlit interface |
| [sandbox_runner.py](exocortex/sandbox_runner.py) | Execute the snippet and capture output |
| [traceback_parser.py](exocortex/traceback_parser.py) | Parse error type, message, and location |
| [llm_debugger.py](exocortex/llm_debugger.py) | Request an explanation and suggested correction |
| [test_sandbox.py](test_sandbox.py), [test_traceback.py](test_traceback.py) | Runner and parser checks |

Generated corrections are suggestions. Inspect them before running them.
