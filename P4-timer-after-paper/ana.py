import time
import threading
from scapy.all import sendp, send, srp1
from scapy.all import Packet, hexdump
from scapy.all import Ether, StrFixedLenField, XByteField, IntField, BitField
from scapy.all import bind_layers
from scapy.all import send, IP, TCP
from scapy.all import sniff
from scapy import *

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

three = []
three_ans0 = 0
file = open('three_0.txt','r')
l = file.readline()
while l:
    l = l.split(" ")
    l = l[2]
    three_ans0 = three_ans0 + float(l)
    three.append( float(l) )
    l = file.readline()
three_ans0 = three_ans0 / 10000
print(three_ans0)
file.close()

three_ans1 = 0
file = open('three_1.txt','r')
l = file.readline()
while l:
    l = l.split(" ")
    l = l[2]
    three_ans1 = three_ans1 + float(l)
    three.append( float(l) )
    l = file.readline()
three_ans1 = three_ans1 / 10000
print(three_ans1)
file.close()

three_ans2 = 0
file = open('three_2.txt','r')
l = file.readline()
while l:
    l = l.split(" ")
    l = l[2]
    three_ans2 = three_ans2 + float(l)
    three.append( float(l) )
    l = file.readline()
three_ans2 = three_ans2 / 10000
print(three_ans2)
file.close()

three_ans3 = 0
file = open('three_3.txt','r')
l = file.readline()
while l:
    l = l.split(" ")
    l = l[2]
    three_ans3 = three_ans3 + float(l)
    three.append( float(l) )
    l = file.readline()
three_ans3 = three_ans3 / 10000
print(three_ans3)
file.close()

three_ans4 = 0
file = open('three_4.txt','r')
l = file.readline()
while l:
    l = l.split(" ")
    l = l[2]
    three_ans4 = three_ans4 + float(l)
    three.append( float(l) )
    l = file.readline()
three_ans4 = three_ans4 / 10000
print(three_ans4)
file.close()

two = []
two_ans0 = 0
file = open('two_0.txt','r')
l = file.readline()
while l:
    l = l.split(" ")
    l = l[2]
    two_ans0 = two_ans0 + float(l)
    two.append( float(l) )
    l = file.readline()
two_ans0 = two_ans0 / 10000
print(two_ans0)
file.close()

two_ans1 = 0
file = open('two_1.txt','r')
l = file.readline()
while l:
    l = l.split(" ")
    l = l[2]
    two_ans1 = two_ans1 + float(l)
    two.append( float(l) )
    l = file.readline()
two_ans1 = two_ans1 / 10000
print(two_ans1)
file.close()

two_ans2 = 0
file = open('two_2.txt','r')
l = file.readline()
while l:
    l = l.split(" ")
    l = l[2]
    two_ans2 = two_ans2 + float(l)
    two.append( float(l) )
    l = file.readline()
two_ans2 = two_ans2 / 10000
print(two_ans2)
file.close()

two_ans3 = 0
file = open('two_3.txt','r')
l = file.readline()
while l:
    l = l.split(" ")
    l = l[2]
    two_ans3 = two_ans3 + float(l)
    two.append( float(l) )
    l = file.readline()
two_ans3 = two_ans3 / 10000
print(two_ans3)
file.close()

two_ans4 = 0
file = open('two_4.txt','r')
l = file.readline()
while l:
    l = l.split(" ")
    l = l[2]
    two_ans4 = two_ans4 + float(l)
    two.append( float(l) )
    l = file.readline()
two_ans4 = two_ans4 / 10000
print(two_ans4)
file.close()
'''
ds_sort = sorted(two)
last, i = min(ds_sort), 0
ds_sort = ds_sort[1000:-1000]
print(ds_sort[0],ds_sort[-1])
plt.xlim((0.1960, 0.1980))
while i < len(ds_sort)-1:
    print(i,ds_sort[i])
    plt.plot([ds_sort[i],ds_sort[i+1]], [i/len(ds_sort),(i+1)/len(ds_sort)],  color='r')
    plt.plot(1,i/len(ds_sort))
    if i < len(ds_sort):
        last = ds_sort[i]
    i += 1

ds_sort = sorted(three)
last, i = min(ds_sort), 0
ds_sort = ds_sort[1000:-1000]
print(ds_sort[0],ds_sort[-1])
while i < len(ds_sort)-1:
    print(i,ds_sort[i])
    plt.plot([ds_sort[i],ds_sort[i+1]], [i/len(ds_sort),(i+1)/len(ds_sort)],  color='b')
    plt.plot(1,i/len(ds_sort))
    if i < len(ds_sort):
        last = ds_sort[i]
    i += 1

'''
ds_sort = sorted(two)
last, i = min(ds_sort), 0
ds_sort = ds_sort[1000:-1000]
print(ds_sort[0],ds_sort[-1])
plt.xlim((min(ds_sort), max(ds_sort)))
while i < len(ds_sort)-1:
    print(i,ds_sort[i])
    plt.plot([ds_sort[i],ds_sort[i+1]], [i/len(ds_sort),(i+1)/len(ds_sort)],  color='r')
    plt.plot(1,i/len(ds_sort))
    if i < len(ds_sort):
        last = ds_sort[i]
    i += 1
plt.savefig('save_1.jpg')