# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 20:08:30 2019

@author: sunflower
"""
string1 = "seorue"
string2 = "sere2"

print (string1.ljust(2) + string2.ljust(20))

#print this string1 variable left justified with a total width for the first number in the blank ie. 10, and the default characters
#as empty spaces for the rest of the width
print (string1.ljust(10, ' ') +  string2.ljust(20))