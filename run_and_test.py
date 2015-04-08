#!/usr/bin/python
import timeit
from time import time

file = open('data/genome2.dat','rb')
subject = file.read()
pattern = "ATGTATATATATGTATAATTATAAA"

from ctypes import cdll
bruteforce = cdll.LoadLibrary("libs/brute_force.so")
horspool = cdll.LoadLibrary("libs/horspool.so")
bom_lib = cdll.LoadLibrary("libs/bom.so")
bndm = cdll.LoadLibrary("libs/bndm.so")


t0 = time()
bom_lib.BOM(pattern,len(pattern),subject,len(subject))
t1 = time()
bomtime = (t1-t0)

t0 = time()
bruteforce.BF(pattern,len(pattern),subject,len(subject))
t1 = time()
#print '\nBruteForce takes %f' %(t1-t0)
bftime = (t1-t0)

t0 = time()
horspool.HORSPOOL(pattern,len(pattern),subject,len(subject))
t1 = time()
#print '\nHorspool takes %f' %(t1-t0)
horspooltime = (t1-t0)

t0 = time()
bndm.BNDM(pattern,len(pattern),subject,len(subject))
t1 = time()
#print '\nBNDM takes %f' %(t1-t0)
bndmtime = (t1-t0)


import plotly.plotly as py
from plotly.graph_objs import *

data = Data([
    Bar(
        x=['BOM', 'BRUTEFORCE', 'HORSPOOL','BNDM'],
        y=[bomtime, bftime, horspooltime,bndmtime]
    )
])

plot_url = py.plot(data, filename='basic-bar')


