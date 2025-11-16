from exocortex.sandbox_runner import run_code_in_sandbox

# Intentionally wrong code to trigger an error
code = "print(1/0)"

result = run_code_in_sandbox(code)

print("STDOUT:", repr(result["stdout"]))
print("STDERR:", repr(result["stderr"]))
print("SUCCESS:", result["success"])
