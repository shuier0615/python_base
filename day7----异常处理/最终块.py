#最终块：
file = None
try:
    file = open('example.txt', 'r')
    content = file.read()
except FileNotFoundError as e:
    print(f"File not found: {e}")
finally:
    if file is not None:
        file.close()  # 确保文件被关闭