#Retrieve PDB files from the Protein Data Bank website:
RefinedPDBCodeList = [] #C1
with open('rs126NoBlanks.txt') as inputfile:
    for line in inputfile:
         RefinedPDBCodeList.append(line.strip().split(','))
		 
print(RefinedPDBCodeList[0])
['101m.pdb']

import urllib.request      
for i in range(0, 1): #S2 - range(0, len(RefinedPDBCodeList)):
    path=urllib.request.urlretrieve('http://files.rcsb.org/download/101M.pdb', '101m.pdb')