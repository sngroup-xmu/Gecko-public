import time
import threading
from tqdm import trange
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import stats

data_success_34 = []
data_success_35 = []
data_one_fail_34 = []
data_one_fail_35 = []
data_two_fail_34 = []
data_two_fail_35 = []

print('数据读取——success:')
for i in trange(5):
    file = '/home/jjh/P4-timer/debug/OP3/op345_' + str(i+1) + '.txt'
    file = open(file,'r')
    l = file.readline()
    while l:
        l = l.split(" ")
        if l[0] != 0:
            if len(l) > 1:
                if l[2] == '35':
                    l = l[4]
                    l = float(l)
                    if l < 0.35:
                        data_success_35.append(l)
                elif l[2] == '34':
                    l = l[4]
                    l = float(l)
                    if l < 0.35:
                        data_success_34.append(l)
        l = file.readline()
    file.close()

print('数据读取——one_fail:')
for i in trange(5):
    file = '/home/jjh/P4-timer/debug/OP3/op35_' + str(i+1) + '.txt'
    file = open(file,'r')
    l = file.readline()
    while l:
        l = l.split(" ")
        if l[0] != 0:
            if len(l) > 1:
                if l[2] == '35':
                    l = l[4]
                    l = float(l)
                    data_one_fail_35.append(l)
                elif l[2] == '34':
                    l = l[4]
                    l = float(l)
                    data_one_fail_34.append(l)
        l = file.readline()
    file.close()

print('数据读取——two_fail:')
for i in trange(5):
    file = '/home/jjh/P4-timer/debug/OP3/op3_' + str(i+1) + '.txt'
    file = open(file,'r')
    l = file.readline()
    while l:
        l = l.split(" ")
        if l[0] != 0:
            if len(l) > 1:
                if l[2] == '35':
                    l = l[4]
                    l = float(l)
                    data_two_fail_35.append(l)
                elif l[2] == '34':
                    l = l[4]
                    l = float(l)
                    data_two_fail_34.append(l)
        l = file.readline()
    file.close()

plt.xlim(0, 5000)
plt.ylim(0, 0.8)
print("画success 35时间图像:")
for i in trange(len(data_success_35)-1):
    plt.plot([i,i+1], [data_success_35[i],data_success_35[i+1]],  color='r')
    i += 1
print("保存中...")
plt.savefig('time_abs_all_success_p4_chasing_two.jpg')

plt.cla()

