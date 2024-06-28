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
    file = 'two_0' + str(i) + '.txt'
    file = open(file,'r')
    l = file.readline()
    while l:
        l = l.split(" ")
        l = l[2]
        three.append( float(l)*1000 )
        l = file.readline()
    file.close()


print("删选数据：")
a = len(three)
a = a - 4
for i in trange(a):
    if three[i] <= 160:
        i = i + 1
    elif three[i] < 200:
        three_ans.append(three[i])
    elif three[i+1] >= 200:
        i = i + 200
    elif three[i-1] >= 200:
        i = i + 200
    elif three[i] >= 300:
        i = i + 1
    else:
        three_ans.append(three[i])
three = three_ans

ds_sort = sorted(three)
i = 0
ds_sort = ds_sort[7:-7]
a = len(ds_sort) - 1
i = 190
rt = []
while i < 222:
    rt.append(i)
    i = i + 2
plt.xticks(rt,rotation=70)
plt.xlim(188, 222)
plt.ylim(-0.1, 1.05)
i = 0
rt = []
while i < 1.1:
    rt.append(i)
    i = i + 0.1
plt.yticks(rt)
plt.grid()
print("画绝对值时间图像:")
for i in trange(a):
    plt.plot([ds_sort[i],ds_sort[i+1]], [i/len(ds_sort),(i+1)/len(ds_sort)],  color='r')
    plt.plot(1,i/len(ds_sort))
    if i < len(ds_sort):
        last = ds_sort[i]
    i += 1
print("保存中...")
plt.savefig('time_abs_all_success_p4_chasing_two.jpg')

plt.cla()
a = len(ds_sort)
print("取log:")
for i in trange(a):
    ds_sort[i] = math.log(ds_sort[i],10)
i = 2.28
rt = []
while i < 2.35:
    rt.append(i)
    i = i + 0.005
plt.xticks(rt,rotation=70)
plt.xlim(2.275, 2.35)
plt.ylim(-0.1, 1.05)
i = 0
rt = []
while i < 1.1:
    rt.append(i)
    i = i + 0.1
plt.yticks(rt)
plt.grid()
print("画log时间图像:")
a = len(ds_sort) - 1
for i in trange(a):
    plt.plot([ds_sort[i],ds_sort[i+1]], [i/len(ds_sort),(i+1)/len(ds_sort)],  color='r')
    plt.plot(1,i/len(ds_sort))
    if i < len(ds_sort):
        last = ds_sort[i]
    i += 1
print("保存中...")
plt.savefig('time_log_all_success_p4_chasing_two.jpg')

