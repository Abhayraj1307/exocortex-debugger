

from exocortex.llm_debugger import debug_code

code = """
a = 10
b = 0
print(a / b)
"""

result = debug_code(code)

print(result["success"])
print(result["traceback"])
print(result["llm_response"])
from exocortex.llm_debugger import auto_fix_loop

res = auto_fix_loop("""
x = [1,2,3]
print(x[5])
""", max_steps=3)

print(res["status"])
print(res["final_code"])
