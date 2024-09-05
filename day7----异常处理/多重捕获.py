#多重捕获：

try:
    num = 1 / 0  # 这行代码会引发 ZeroDivisionError
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")