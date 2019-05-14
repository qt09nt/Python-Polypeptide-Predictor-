with open('rs126NoBlanks.txt', 'r') as f:
    pdblist2 = [line.strip() for line in f]
#print (pdblist2)

#import os
#os.chdir("C:\Users\sunflower\Desktop\python protein project\PDB")

import Bio
from Bio.PDB import PDBList
'''Selecting structures from PDB'''
pdbl = PDBList()

#pdblist2=['4B97','4IPH','4HNO','4HG7','4IRG','4G4W','4JKW','4IPC','2YPM','4KEI']
for i in pdblist2:
    pdbl.retrieve_pdb_file(i,pdir='PDB')