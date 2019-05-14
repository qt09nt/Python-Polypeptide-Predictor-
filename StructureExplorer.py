import os
import re


amino_kd = {'A': 1.8,
 'R': -4.0,  
 'N': -3.5,  
 'D': -3.5,  
 'C': 2.5, 
 'Q': -3.5,
 'E': -3.5, 
 'G': 0.4, 
 'H': -3.2, 
 'I': 4.5, 
 'L': 3.8,
 'K': -3.9,
 'M': 1.9,
 'F': 2.8,
 'P': -1.6,
 'S': -0.8,
 'T': -0.7,
 'W': -0.9,
 'Y': -1.3,
 'V': 4.2}
 
motifs=[]
motifsAmino=[]
counter=[0] #keeps track of how many proteins/files are in the rs126 directory

def extractSequenceSet(content): 
	seqSet = []
	match = re.search("OrigSeq:(.*)\n", content)
	span = match.span()	
	seq = content[span[0]+8:span[1]-1]
	seqSet.append(seq)
		
	return("".join(map(str,seqSet)))#returns a string instead of a list

def extractStructure(content): 
	strucSeq=[]
	match = re.search("cons:(.*)\n", content)
	span = match.span()
	ssSeq = content[span[0]+5:span[1]-1]
	strucSeq.append(ssSeq)
	
	return("".join(map(str,strucSeq)))
	
def readFile(filename): 
	with open(filename) as f:
		lines = f.readlines()
	return(''.join(lines))

def motifFinder(structure,peptide): #determine the motifs (helix, sheet, coil) and the corresponding AA sequences of the motifs
	
	if len(structure) == 0: 
		counter[0]+=1
	
	else:
		if structure[0] == "-": # indicating no helix
			match = re.search("-*", structure) # find the coil
			span = match.span()
			m=structure[span[0]:span[1]]
			structure=structure[span[1]:]
			mAA=peptide[span[0]:span[1]]
			motifs.append(m)
			motifsAmino.append(mAA)
			peptide=peptide[span[1]:]
			motifFinder(structure, peptide)
	
		elif structure[0] == "H": #indicating helix
			match = re.search("H*", structure) #find the helix
			span = match.span() # capture the helix
			m=structure[span[0]:span[1]] # " "
			mAA=peptide[span[0]:span[1]] #capture corresponding AA sequence
			motifs.append(m) # place the motif in list
			motifsAmino.append(mAA) # place AA in list
			structure=structure[span[1]:] # declare a new structure
			peptide=peptide[span[1]:] # declare a new peptide
			motifFinder(structure, peptide) # recursive step
		
		elif structure[0] == "E":
			match = re.search("E*", structure) # find sheets
			span = match.span()
			m=structure[span[0]:span[1]]
			mAA=peptide[span[0]:span[1]]
			motifs.append(m)
			motifsAmino.append(mAA)
			structure=structure[span[1]:]
			peptide=peptide[span[1]:]
			motifFinder(structure, peptide)
		return structure, peptide

def kdAnalysis(mot): # look at the hydrophobicity
	myMotifs=list(mot)	# turns each seperate motif into a list of AA 
	motif_kd=[]
	for i in myMotifs:
		j=amino_kd[i]
		motif_kd.append(j)
		x=sum(motif_kd)
	return x
	

dir = 'rs126\\'	
filenames = os.listdir(dir)	
for filename in filenames:	
	content = readFile(dir + filename)
	seq = extractSequenceSet(content)#extracts the protein sequence
	ssSeq = extractStructure(content)#extracts the motif sequence
	motifSearch = motifFinder(ssSeq, seq)
	

motifCount=[0,0,0] #coil, helix, sheet
motifLength=[0,0,0]	
motifTKD=[0,0,0]


for (i,j) in zip(motifsAmino, motifs):
	motifKd=kdAnalysis(i)
	
	if (j[0] == "-"):
		k="COIL"
		motifCount[0]+=1
		motifLength[0]+=len(j)
		motifTKD[0]+=motifKd
		
	elif (j[0] == "H"):
		k="HELIX"
		motifCount[1]+=1
		motifLength[1]+=len(j)
		motifTKD[1]+=motifKd
		
	else:
		k="SHEET"
		motifCount[2]+=1
		motifLength[2]+=len(j)
		motifTKD[2]+=motifKd
		
	

#print("This training set has" , counter[0] +1, "proteins")  #This will output how many proteins are in the training set
print("COIL COUNT:", motifCount[0], "HELIX COUNT:", motifCount[1], "SHEET COUNT:", motifCount[2])
print('\nAVG_LEN_COIL:', (motifLength[0]/motifCount[0]), "\nAVG_LEN_HEL:", (motifLength[1]/motifCount[1]), "\nAVG_LEN_SHE:", (motifLength[2]/motifCount[2]))
print ("\nCOIL-HYDRO:" ,(motifTKD[0]/motifCount[0]), "\nHELIX HYDRO:" , (motifTKD[1]/motifCount[1]), "\nSHEET HYDRO:" ,(motifTKD[2]/motifCount[2]))
