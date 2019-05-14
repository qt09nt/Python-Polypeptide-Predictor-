c = open("pdbNames.txt", "w")
pdbName = []
with open("rs126NoBlanks.txt") as f:
    for line in f:
        pdbName = (str(pdbName) + ".pdb")
        print (pdbName)
