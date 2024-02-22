import os

def get_txt_files(dir):
  txt_files = []
  for file in os.listdir(dir):
    if file.endswith('.txt'):
      txt_files.append(os.path.join(dir, file))
  return txt_files

def get_linecount(file_path):
  with open(file_path, encoding='utf-8') as f:
    return len(f.readlines())

sorted_files = sorted(get_txt_files('sorted'), key=get_linecount)

with open('new_file.txt', 'w', encoding='utf-8') as f:
  for file_path in sorted_files:
    with open(file_path, encoding='utf-8') as f1:
      f.write(f1.read())
      f.write('\n')

with open('new_file.txt', encoding='utf-8') as f:
  content = f.read()

print(content)




