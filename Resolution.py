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


def CNF(sentence):
    temp=re.split("=>",sentence)
    temp1=temp[0].split('&')
    for i in range(0,len(temp1)):
        if temp1[i][0]=='~':
            temp1[i]=temp1[i][1:]
        else:
            temp1[i]='~'+temp1[i]
    temp2='|'.join(temp1)
    temp2=temp2+'|'+temp[1]
    return temp2



if __name__ == '__main__': 
    finalanswer=resolution()
    o=open("output.txt","w+")
    wc=0
    while(wc < n-1):
         o.write(finalanswer[wc]+"\n")
         wc+=1
    o.write(finalanswer[wc])
    o.close()