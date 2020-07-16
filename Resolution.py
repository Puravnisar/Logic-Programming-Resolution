#Purav Nisar
import time
start_time = time.time()
import re
import itertools
import collections 
import copy
import queue

p=open("input.txt","r")
data=list()
data1= p.readlines()
count=0

n=int(data1[0])
queries=list()
for i in range(1,n+1):
    queries.append(data1[i].rstrip())   
k=int(data1[n+1])
kbbefore=list()

if __name__ == '__main__': 
    finalanswer=resolution()
    o=open("output.txt","w+")
    wc=0
    while(wc < n-1):
         o.write(finalanswer[wc]+"\n")
         wc+=1
    o.write(finalanswer[wc])
    o.close()