#!/usr/bin/python

file = open('data/genome2.dat','rb')
subject = file.read()
pattern = "ATGTA"
from ctypes import cdll
bom_lib = cdll.LoadLibrary("bom.so")

bom_lib.BOM(pattern,len(pattern),subject,len(subject))
