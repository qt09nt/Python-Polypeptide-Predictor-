c = open("rs126PDB.txt", "w")
pdbName = []

with open("rs126NoBlanks.txt") as f:
    for line in f:
        pdbName = (str(pdbName).join(".pdb") + "/n")  
        c.write(line)
