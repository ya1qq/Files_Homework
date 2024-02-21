
file_path1 = 'sorted/1.txt'
file_path2 = 'sorted/2.txt'
file_path3 = 'sorted/3.txt'

def get_linecount(file_name):
  with open(file_name, encoding='utf-8') as f:
    return len(f.readlines())

sorted_files = sorted([file_path1, file_path2, file_path3], key=get_linecount)

with open('new_file.txt', 'w', encoding='utf-8') as f:
  for file_path in sorted_files:
    with open(file_path, encoding='utf-8') as f1:
      f.write(f1.read())
      f.write('\n')

with open('new_file.txt', encoding='utf-8') as f:
  content = f.read()

print(content)



