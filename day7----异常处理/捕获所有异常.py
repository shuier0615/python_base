#捕获所有异常：

try:
    result = 1 / 0  # 这行代码会引发 ZeroDivisionError
except Exception as e:
    print(f"An unexpected error occurred: {e}")