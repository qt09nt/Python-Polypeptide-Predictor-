# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 21:16:39 2019

@authors: Gayathri, Queenie
"""

#**************************************************************
#CODE FOR PDB FILES
#***************************************************************

import os

#retrieve all the rs126FileNames from the folder and write them into a file called rs126FileNames.txt
a = open("rs126FileNames.txt", "w")
for path, subdirs, files in os.walk(r'C:\Users\Gayathri\BIF 724 - Python Bioinformatics\rs126'):
   for filename in files:
      a.write(filename + os.linesep) 
a.close()

#open rs126FileNamesOnly.txt and remove the ".concise" from the lines, then write the new file names into a
#text file called rs126FileNamesOnly.txt
a = open("rs126FileNamesOnly.txt", "w") #this is the new file you will write the file names into
lines = []
with open("rs126FileNames.txt") as f:
    for line in f:
         cleaned_line = line.replace(".concise","")
         a.write(cleaned_line + os.linesep) 
a.close()

#remove blank lines from rs126FileNamesOnly and keep only the file          
b = open("rs126NoBlanks.txt", "w")
with open("rs126FileNamesOnly.txt") as f:
    for line in f:
        if not line.isspace():
            b.write(line)
#place the pdb file names into a list:
with open('rs126NoBlanks.txt', 'r') as f:
    pdblist2 = [line.strip() for line in f]
print(pdblist2)
b.close()

#load Biopandas module into Spyder
from biopandas.pdb import PandasPdb

#make a list to number each PDB file from rs126 (125 files)
list1 = list(range(1,126))

#creates a dictionary with list1 = keys while pdblist2 = values
dictionary = dict(zip(list1,pdblist2))
print(dictionary) #Resource used: https://stackoverflow.com/questions/39502079/use-strings-in-a-list-as-variable-names-in-python

#gets the PDB file name corresponding to dictionary value and stores it in ppdb variable
ppdb = PandasPdb().fetch_pdb(dictionary.get(1))
ppdb.parse_sse() #parses through PDB file

#saves filtered PDB file containing only ATOM and HETATM elements
ppdb.to_pdb(path='./final.pdb',
            records=['ATOM','HETATM'],
            gz=False,
            append_newline=True)

#example of secondary structure prediction and amino acid sequence.
string1 = "---HHHHH-HHHHHHH-H-HH-H--H--H--H---------------------H--HHHHHHH--------------HH-HH-H---"
aminoSeq = "PLTQEQLEDARRLKAIYEKKKNELGLSQESVADKMGMGQSGVGALFNGINALNAYNAALLAKILKVSVEEFSPSIAREIYEMYEAVS"

list2 = list(string1) #converts string to list
index = 1 

#import regex function, find HELIX sequences in string1
import re
result = re.findall(r"H+",string1)

#open final.pdb file
c = open("final.pdb", "a")
c.write("\n")

#recordName and serName (Columns 1 and 2)
recordName = []
serNum = []
for i in result:
    recordName.append("HELIX")
    serNum.append(str(index))
    index += 1

#dictionary for 1-letter aa to 3-letter aa
aminoacid3 = {
        "A" : "ALA",
        "R" : "ARG",
        "N" : "ASN",
        "D" : "ASP",
        "C" : "CYS",
        "E" : "GLU",
        "Q" : "GLN",
        "G" : "GLY",
        "H" : "HIS",
        "I" : "ILE",
        "L" : "LEU",
        "K" : "LYS",
        "M" : "MET",
        "F" : "PHE",
        "P" : "PRO",
        "S" : "SER",
        "T" : "THR",
        "W" : "TRP",
        "Y" : "TYR",
        "V" : "VAL"}

#find starting and ending index position of helices in secondary structure prediction
positionsH = []
positionsE = []

for i in range(1,len(string1)):
	if(string1[i-1] != string1[i]):
		if(string1[i] == 'H'):
			positionsH.append(i)
		if(string1[i] == 'E'):
			positionsE.append(i)
		if(string1[i-1] == 'H'):
			positionsH.append(i-1)
		if(string1[i-1] == 'E'):
			positionsE.append(i-1)

startIndex = positionsH[0::2]
endIndex = positionsH[1::2]

#initResName (Column 4)
initResName = []
for k in startIndex:
    if aminoSeq[k] in aminoacid3.keys():
        initResName.append(aminoacid3.get(aminoSeq[k]))
        
# initChainID (Column 5)
initChainID = "A" 

# initSeqNum (Column 6)
startIndex = positionsH[0::2]

#endResName (Column 7)
endResName = []
for l in endIndex: 
    if aminoSeq[k] in aminoacid3.keys():
        endResName.append(aminoacid3.get(aminoSeq[k]))
        
#endSeqNum (Column 9)
endIndex = positionsH[1::2]

#helix class (column 10)
helixClass = "1" 

# (ommitted) comment: takes up 30 spaces (columns 41- 70):
comment = " "

#length (Column 14)
import numpy as np
length = list(np.array(endIndex)-np.array(startIndex))

lengthCol = []
for m in length:
    lengthCol.append(m)

#write columns to PDB file
for index in range(len(recordName)):
    c.write((str(recordName[index]).ljust(6, ' ')) 
            + (str(serNum[index]).ljust(3, ' '))
            + (str(initResName[index]).ljust(3, ' ')) 
            + (str(initChainID).ljust(1, ' '))
            + (str(startIndex[index]).ljust(5, ' ')) #width of 5 to make up for the omitted initICode which has width of 1 
            + (str(endResName[index]).ljust(4, ' ')) #width of 4 to add in omitted endChainID with width of 1
            + (str(endIndex[index]).ljust(5, ' ')) #width encompasses the omitted endICode's width of 1 
            + (str(helixClass).ljust(2, ' '))
            + (str(comment).ljust(30, ' '))
            + (str(lengthCol[index]))
            + "\n")

#close PDB file
c.close()
