import time
import threading
from scapy.all import sendp, send, srp1
from scapy.all import Packet, hexdump
from scapy.all import Ether, StrFixedLenField, XByteField, IntField, BitField
from scapy.all import bind_layers
from scapy.all import send, IP, TCP
from scapy.all import sniff
from scapy import *
from tqdm import trange
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import stats

three = []
three_ans = []

print('数据读取：')
for i in trange(5):
    file = 'three_0' + str(i) + '.txt'
    file = open(file,'r')
    l = file.readline()
    while l:
        l = l.split(" ")
        l = l[2]
        three.append( float(l) )
        l = file.readline()
    file.close()


print("删选数据：")
a = len(three)
a = a - 4
for i in trange():
    if three[i] < 0.2:
        three_ans.append(three[i])
    elif three[i+1] >= 0.2 and three[i+2] >= 0.2:
        i = i + 100
    elif three[i-1] >= 0.2 and three[i-2] >= 0.2:
        i = i + 100
    else:
        three_ans.append(three[i])

three = three_ans

ds_sort = sorted(three)
last, i = min(ds_sort), 0
a = len(ds_sort)
ds_ans = ds_sort
t = 0
if t == 1:
    while i < len(ds_ans):
        ds_ans[i] = ds_ans[i] * 1000
        ds_ans[i] = math.log(ds_ans[i],10)
        i += 1
i = 0
plt.xlim((min(ds_ans), max(ds_ans)))
print((min(ds_ans), max(ds_ans)))
a = len(ds_ans)-1
print("画图:")
for i in trange(a):
    plt.plot([ds_ans[i],ds_ans[i+1]], [i/len(ds_ans),(i+1)/len(ds_ans)],  color='r')
    plt.plot(1,i/len(ds_ans))
    if i < len(ds_ans):
        last = ds_ans[i]
    i += 1
if t == 0:
    plt.savefig('save_0.jpg')
if t == 1:
    plt.savefig('save_1.jpg')