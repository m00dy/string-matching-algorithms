#!/usr/bin/python
import timeit
from time import time

file = open('data/genome.dat','rb')
subject = file.read()
lsubject = len(subject)


from ctypes import cdll
bruteforce = cdll.LoadLibrary("libs/brute_force.so")
horspool = cdll.LoadLibrary("libs/horspool.so")
bom_lib = cdll.LoadLibrary("libs/bom.so")
bndm = cdll.LoadLibrary("libs/bndm.so")

def random_string(slen):
  import random
  string_all = "ATGC"
  string_all_len = len(string_all)
  ret = ""
  for i in range(0,slen):
    ret+=(string_all[random.randint(0,string_all_len-1)])
  return ret

allresults = {'Bom':[],'BruteForce':[],'Horspool':[],'Bndm':[]}

def hugetest():
  inputSize = [2,4,8,16,32,63]
  for input in inputSize:
    rndstr = random_string(input)
    lrndstr = len(rndstr) 
    ##BOM 
    t0 = time()
    bom_lib.BOM(rndstr,lrndstr,subject,lsubject)
    t1 = time()
    bomtime = (t1-t0)
    allresults.get('Bom',[]).append(bomtime)
   
    ##BruteForce
    t0 = time()
    bruteforce.BF(rndstr,lrndstr,subject,lsubject)
    t1 = time()
    bftime = (t1-t0)
    allresults.get('BruteForce',[]).append(bftime)
 
    ##Horspool
    t0 = time()
    horspool.HORSPOOL(rndstr,lrndstr,subject,lsubject)
    t1 = time()
    horspooltime = (t1-t0)
    allresults.get('Horspool',[]).append(horspooltime)
  
    ##Bndm
    t0 = time()
    bndm.BNDM(rndstr,lrndstr,subject,lsubject)
    t1 = time()
    bndmtime = (t1-t0)
    allresults.get('Bndm',[]).append(bndmtime)
 
    print allresults

hugetest()


import plotly.plotly as py
from plotly.graph_objs import *

result = allresults.get('Bom',[])
trace1 = Bar(
    x=['Input size 2', 'Input size 4', 'Input size 8' , 'Input size 16','Input size 32','Input size 63'],
    y=[result[0],result[1],result[2],result[3],result[4],result[5]],
    name='BOM'
)

result = allresults.get('BruteForce',[])
trace2 = Bar(
    x=['Input size 2', 'Input size 4', 'Input size 8' , 'Input size 16','Input size 32','Input size 63'],
    y=[result[0],result[1],result[2],result[3],result[4],result[5]],
    name='BruteForce'
)

result = allresults.get('Horspool',[])
trace3 = Bar(
    x=['Input size 2', 'Input size 4', 'Input size 8' , 'Input size 16','Input size 32','Input size 63'],
    y=[result[0],result[1],result[2],result[3],result[4],result[5]],
    name='Horspool'
)

result = allresults.get('Bndm',[])
trace4 = Bar(
    x=['Input size 2', 'Input size 4', 'Input size 8' , 'Input size 16','Input size 32','Input size 63'],
    y=[result[0],result[1],result[2],result[3],result[4],result[5]],
    name='Bndm'
)

data = Data([trace1, trace2,trace3,trace4])

layout = Layout(
    barmode='group'
)

fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='grouped-bar')


