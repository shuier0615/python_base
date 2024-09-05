import os
file_path = "./example.txt"
if os.path.exists(file_path):
    print("文件存在")
else:
    print("文件不存在")