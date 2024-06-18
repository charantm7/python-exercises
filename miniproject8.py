import zipfile

file_name = 'example.txt'
file_name_content = 'This is an example of text file'

with open(file_name,'w') as file:
    file.write(file_name_content)

zip_file_name = 'example.zip'

with zipfile.ZipFile(zip_file_name,'w') as zipf:
    zipf.write(file_name)

print(f"Here the {file_name} is added to {zip_file_name}")