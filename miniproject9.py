import os

file_path = 'c:\Desktop\ppt'

if os.path.exists(file_path):
    os.remove(file_path)
    print("The file path{file_path} had been successfully removed")

else:
    print("The file path {file_path} do not exist")




import shutil

dir_path = 'c:\Desktop\pythonfiles'

try:
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
        print(f"Your directory path {dir_path} has been removed")

    else:
        print("The directory path {dir_path} do not exist")

except OSError as e:
    print(f"Error:{e.strerror}")