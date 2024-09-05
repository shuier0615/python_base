# main.py

from my_package import math_operations, string_operations

result_add = math_operations.add(10, 5)
result_upper = string_operations.uppercase("hello")

print("Addition:", result_add)  # Output: Addition: 15
print("Uppercase:", result_upper)  # Output: Uppercase: HELLO
