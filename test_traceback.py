from exocortex.sandbox_runner import run_code_in_sandbox
from exocortex.traceback_parser import extract_traceback

code = "print(1/0)"

result = run_code_in_sandbox(code)
tb = extract_traceback(result["stderr"])

print("FULL STDERR:")
print(result["stderr"])
print("\nEXTRACTED TRACEBACK:")
print(tb)
