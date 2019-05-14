'''
p3Main.py
This is the main progam which predicts secondary structure of unknonw amino acid sequences using a pre-trained model.
@author: Minoru Nakano
'''

from sklearn import svm # scikit learn module for machine learning
from joblib import dump, load # module used to save and load trained svm models
import PDBEditor.p3editPDB as editor
import p3DataReader as reader
import p3DataBuilder as builder
import aminoHelper as aHelper
import featureHelper as fHelper

features = []

##### Calculate feature scores used for the test data.
data = reader.getTD9078Dataset('td9078.csv', 2000)
aminoHelper = aHelper.AminoHelper()
scores = aminoHelper.calculateSecStructScore(data)
features += scores

##### Load a pre-trained module #####
clf = load('models\\clf-td9078-2000-HP.joblib')

totalResidue = 0
totalHelix = 0
totalSheet = 0
totalCorrect = 0
totalHelixCorrect = 0
totalSheetCorrect = 0

# reading 12 test dataset as .consice files from the test directory.
testDataset = reader.getRS126Dataset("test\\")
predictedSequences = []
for data in testDataset:
	testSet = builder.buildTestDataset(data[0], features)
	result = clf.predict(testSet) # Secondary structure prediction.
	predictedSecStructSeq = builder.buildPredictedSequence(result)
	print("Seq: ", data[0])
	print("Act: ", data[1])
	print("Pre: ", predictedSecStructSeq, "\n")
	
	predictedSequences.append(predictedSecStructSeq)
	
	##### Calcute the prediction stats
	totalResidue += len(data[0])
	for i in range(0, len(data[0])):
		if(data[1][i] == 'H'):
			totalHelix += 1
		elif(data[1][i] == 'E'):
			totalSheet += 1
			
		if(data[1][i] == predictedSecStructSeq[i]):
			totalCorrect += 1
			if(predictedSecStructSeq[i] == 'H'):
				totalHelixCorrect += 1
			elif(predictedSecStructSeq[i] == 'E'):
				totalSheetCorrect += 1

# Print the prediction statistics.
print("Total number of residues:", totalResidue)
print("Total number of Helix residues:", totalHelix)
print("Total number of Sheet residues:", totalSheet)
print("Total number of correct predcition:", totalCorrect)
print("Total number of correct helix prediction:", totalHelixCorrect)
print("Total number of correct sheet prediction:", totalSheetCorrect)
print("Pct total correct prediction:", float(totalCorrect/totalResidue) * 100)
print("Pct correct helix prediction:", float(totalHelixCorrect/totalHelix) * 100)
print("Pct correct sheet prediction:", float(totalSheetCorrect/totalSheet) * 100)

# Call the editPDB function to generate a PDB file of one of the predicted proteins (Currently, '1eca' protein is used).
editor.editPDB(testDataset[1][0], predictedSequences[1], 2)
print("A predicted PDB file for the protein \'1eca\' is created in ProteinViewer as final.pdb.")