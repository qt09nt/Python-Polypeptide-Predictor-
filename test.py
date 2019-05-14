import os

filenames = os.listdir('rs126\\')
for filename in filenames:

	with open('rs126\\' + filename) as f:
		lines = f.readlines()
	print(filename, 'has been read.')