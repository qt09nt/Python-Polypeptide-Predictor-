#this code is for creating and saving pdb files, naming the files with pdb names found in the pdblist2 list 

with open('rs126NoBlanks.txt', 'r') as f:  #r is read 
    pdblist2 = [line.strip() for line in f]
print (pdblist2)

for f in pdblist2
    file = open('{0}.pdb'.format(pdblist2[10]),"w")