#!/usr/bin/python

file = open('data/genome.dat','rb')
subject = file.read()
pattern = "ATGTATATATATATATATAATATATATATATATATATATATATATATA"
from ctypes import cdll
bom_lib = cdll.LoadLibrary("bom.so")

bom_lib.BOM(pattern,len(pattern),subject,len(subject))
