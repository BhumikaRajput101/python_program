#read a text and count the number of lines word and character
def count(filepath):
 with open (r'd:\python_practice\1-data-analysis.ipynb\fileoperation.ipynb\example.txt','r') as file :
  lines=file.readlines()
  countline=len(lines)
  countword=sum(len(line.split())for line in lines)
  countchar =sum(len(line)for line in lines )
  print('number of lines:',countline ,'\nnumber of word:',countword ,'\n number of char:',countchar )

filepath='d:\python_practice\1-data-analysis.ipynb\fileoperation.ipynb\example.txt'


count(filepath)