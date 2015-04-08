#!/usr/bin/python

file = open('data/genome.dat','rb')
subject = file.read()
pattern = "ATGTATATATATATATATAATATATATATATATATATATATATATATA"

from ctypes import cdll
bruteforce = cdll.LoadLibrary("brute_force.so")
horspool = cdll.LoadLibrary("horspool.so")
bom_lib = cdll.LoadLibrary("bom.so")
bndm = cdll.LoadLibrary("bndm.so")


bom_lib.BOM(pattern,len(pattern),subject,len(subject))

