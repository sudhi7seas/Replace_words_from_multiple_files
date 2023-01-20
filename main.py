#import Path library from pathlib
from pathlib import Path
#point to the files directory using 'Path'
files_dir = Path('files')

#iterate through the directory 
for filepath in files_dir.iterdir():
  with open(filepath, 'r') as file:
    content = file.read()

    newcontent = content.replace('amount','units')

  with open(filepath,'w') as file:
    file.write(newcontent)
    



