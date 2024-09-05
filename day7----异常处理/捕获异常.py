#捕获异常：使用 try 和 except 块来捕获和处理可能发生的异常。
try:
    num = int("abc")  # 这行代码会引发 ValueError
except ValueError as e:
    print(f"ValueError: {e}")