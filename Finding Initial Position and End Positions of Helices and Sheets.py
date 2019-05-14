str = '------HHHHHHHE--HHHHHHHHHHH--------HHHHHH-------HHHH--'

print(str)

positionsH = []

positionsE = []

for i in range(1,len(str)):

	if(str[i-1] != str[i]):

		if(str[i] == 'H'):

			positionsH.append(i)

		if(str[i] == 'E'):

			positionsE.append(i)

		if(str[i-1] == 'H'):

			positionsH.append(i-1)

		if(str[i-1] == 'E'):

			positionsE.append(i-1)


print(positionsH)

print(positionsE)

