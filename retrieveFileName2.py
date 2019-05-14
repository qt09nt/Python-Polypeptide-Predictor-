import os

#retrieve all the rs126FileNames from the folder and write them into a file called rs126FileNames.txt
a = open("rs126FileNames.txt", "w")
for path, subdirs, files in os.walk(r'C:\Users\sunflower\Desktop\python protein project\rs126'):
   for filename in files:
      a.write(filename + os.linesep) 
a.close()

#open rs126FileNamesOnly.txt and remove the ".concise" from the lines, then write the new file names into a
#text file called rs126FileNamesOnly.txt
a = open("rs126FileNamesOnly.txt", "w") #this is the new file you will write the file names into
lines = []
with open("rs126FileNames.txt") as f:
    for line in f:
         cleaned_line = line.replace(".concise","") #take out the ".concise" part of each line
         a.write(cleaned_line + os.linesep) 
a.close()

#remove blank lines from rs126FileNamesOnly and keep only the file          
b = open("rs126NoBlanks.txt", "w")  #w is write
with open("rs126FileNamesOnly.txt") as f:
    for line in f:
        if not line.isspace():      #take out the blank lines
            b.write(line)
b.close()

#place the pdb file names into a list:
with open('rs126NoBlanks.txt', 'r') as f:  #r is read 
    pdblist2 = [line.strip() for line in f]
print (pdblist2)

file = open('{0}.pdb'.format(pdblist2[6]),"w")
#access the name sof the pdb files from the pdblist2 list,
# and saves it as a pdb file with that pdb name 

from biopandas.pdb import PandasPdb #Loads Biopandas module

variable1 = "1csei" #PDB file we want (need to adjust it to grab string from array)
ppdb = PandasPdb().fetch_pdb(variable1) 
ppdb.parse_sse()
print(ppdb.df['ATOM']) #Grab ATOM information from PDB file
print(ppdb.df['HETATM']) #Grab HETATM information from PDB file

#saves filtered PDB file containing only ATOM and HETATM elements

ppdb.to_pdb(path='./1csei.pdb',         #change the name of the file to the name of the pdb code
           records=['ATOM','HETATM'],
           gz=False,
           append_newline=True)