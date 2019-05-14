testSeq = "CSVDIQGNDQMQFNTNAITVDKSCKQFTVNLSHPGNLPKNVMGHNWVLSTAADMQGVVTDGMASGLDKDYLKPDDSRVIAHTKLIGSGEKDSVTFDVSKLKEGEQYMFFCTFPGHSALMKGTLTLK"
testSecStructSeq = "-EEEE-----------EEEE-----EEEEEEE------------EEEEEE-----HHHHHHHHH-----------EEEEEEEEE-------EEEEEEE-------EEEEE-----EEEEEEEEEE-"
predictedSecStructSeq = "--------------------------------------------------HH-------------------------------------------------H-HH--------------H------"

import re

#searches through the predictedSecStructSeq and returns the Helix sequence predictions (H), extracted form the rest of the predicted sequence
result = re.findall(r"H+", predictedSecStructSeq)

print(result)

print(len(result)) #prints out the number of predicted helices in the predicted secondary structure

#add the extracted H predicted structures into an array\
#then search for the elements in the array within the predictedSecStruct and return the position within that predicted SecStructSeq 


iter = re.finditer(r"\bis\b", predictedSecStructSeq)
indices = [m.start(0) for m in iter]

