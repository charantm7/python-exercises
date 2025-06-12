import os

current_path = 'c:\\root'
new_path = 'c:\root\\'

if os.path.exists(current_path):
    os.rename(current_path, new_path)
    print('Success')

else:
    print(f"Your {current_path} do not exists")