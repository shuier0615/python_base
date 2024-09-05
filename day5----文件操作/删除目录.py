import os

os.rmdir('empty_directory')
import shutil
shutil.rmtree('directory_to_remove', ignore_errors=True)  # 注意：此操作不可逆