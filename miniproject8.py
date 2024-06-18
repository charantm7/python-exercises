import zipfile

file_name = 'example.txt'
file_name_content = 'This is an example of text file'

with open(file_name,'w') as file:
    file.write(file_name_content)

zip_file_name = 'example.zip'

with zipfile.ZipFile(zip_file_name,'w') as zipf:
    zipf.write(file_name)

print(f"Here the {file_name} is added to {zip_file_name}")



import zipfile

text_file_name = 'example.txt'
text_file_name_content = 'This is an example of text file'

with open(text_file_name,'w') as file:
    file.write(text_file_name_content)

zip_file_name = 'example.zip'

zipf = zipfile.ZipFile(zip_file_name,'w')

zipf.write(text_file_name)

zipf.close()

print(f"Your file{text_file_name} has been written to {zip_file_name}")