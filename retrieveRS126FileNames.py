#Retrieve file names from rs126 folder and write into a text file

import os

a = open("rs126FileList.txt", "w")
for path, subdirs, files in os.walk(r'C:\Users\sunflower\Desktop\python protein project\rs126'):
   for filename in files:
     f = os.path.join(path, filename)
     a.write(str(f) + os.linesep) 