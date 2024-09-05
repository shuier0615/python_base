import os

for root, dirs, files in os.walk('.'):
    print(f"当前路径: {root}")
    print("子目录:", dirs)
    print("文件:", files)
    print("--------------------")