
#svm test results for 1azu:
testSeq = "CSVDIQGNDQMQFNTNAITVDKSCKQFTVNLSHPGNLPKNVMGHNWVLSTAADMQGVVTDGMASGLDKDYLKPDDSRVIAHTKLIGSGEKDSVTFDVSKLKEGEQYMFFCTFPGHSALMKGTLTLK"
testSecStructSeq = "-EEEE-----------EEEE-----EEEEEEE------------EEEEEE-----HHHHHHHHH-----------EEEEEEEEE-------EEEEEEE-------EEEEE-----EEEEEEEEEE-"
predictedSecStructSeq = "--------------------------------------------------HH-------------------------------------------------H-HH--------------H------"

print(predictedSecStructSeq)

positionsH = [] #list to keep track of positions of the helix elements

positionsE = [] #list to keep track of the positions of the sheet elements

for i in range(1,len(predictedSecStructSeq)):

	if(predictedSecStructSeq[i-1] != predictedSecStructSeq[i]):

		if(predictedSecStructSeq[i] == 'H'):

			positionsH.append(i)

		if(predictedSecStructSeq[i] == 'E'):

			positionsE.append(i)

		if(predictedSecStructSeq[i-1] == 'H'):

			positionsH.append(i-1)

		if(predictedSecStructSeq[i-1] == 'E'):

			positionsE.append(i-1)

#output the helix list which shows the beginning of the residue at odd positions in the list,
#and end positions of the helix in even positions of the positionsH list
print(positionsH)

#output the sheet list which shows the beginning of the residues at odd positions in the array 
#and the end residue position in even positions in the positionsE list 
print(positionsE)

    
endResiduePositionsH = positionsH[1::2]

endIndex = positionsH[1::2]

startIndex = positionsH[0::2]

print ("endresiduespositions: ") 
print (endResiduePositionsH)