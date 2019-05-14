# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#1lmb svm results:

#sequence: PLTQEQLEDARRLKAIYEKKKNELGLSQESVADKMGMGQSGVGALFNGINALNAYNAALLAKILKVSVEEFSPSIAREIYEMYEAVS

#predicted structure:
#-----HHHHHHHHHHHHHHHHH-----HHHHHHHHH----HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH-HHHHHHHHHHHHH--
#---HHHHH-HHHHHHH-H-HH-H--H--H--H---------------------H--HHHHHHH--------------HH-HH-H---
#


from biopandas.pdb import PandasPdb

ppdb = PandasPdb().fetch_pdb('1lmb') #Stores 1lmb PDB file into ppdb object

#Saves a file of PDB ATOM and HETATM DATA only.
ppdb.to_pdb(path='./1lmb_edited.pdb', 
            records=['ATOM', 'HETATM'], 
            gz=False, 
            append_newline=True)