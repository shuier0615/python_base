import os

def list_files(directory):
    """列出指定目录下的所有文件"""
    files = os.listdir(directory)
    print("文件列表:", files)

list_files("../抖店")  # 假设example_directory是你的目标目录