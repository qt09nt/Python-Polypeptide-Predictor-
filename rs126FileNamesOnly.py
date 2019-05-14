import os

a = open("rs126FileNamesOnly.txt", "w")
lines = []
with open("rs126FileNames.txt") as f:
    for line in f:
         cleaned_line = line.replace(".concise","")
         a.write(cleaned_line + os.linesep) 
         
#for line in infile.readlines():
 #   cleaned_line = line.replace(".concise","")
