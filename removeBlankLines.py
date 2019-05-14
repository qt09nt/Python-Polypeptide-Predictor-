#with open('rs126FileNamesOnly.txt','rw') as file:
 #   for line in file:
  #      if not line.isspace():
   #         file.write(line)

#import sys

b = open("rs126NoBlanks.txt", "w")
with open("rs126FileNamesOnly.txt") as f:
    for line in f:
        if not line.isspace():
            b.write(line)