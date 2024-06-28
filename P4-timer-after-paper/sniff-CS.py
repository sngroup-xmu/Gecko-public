import time
import threading
from scapy.all import sendp, send, srp1
from scapy.all import Packet, hexdump
from scapy.all import Ether, StrFixedLenField, XByteField, IntField, BitField
from scapy.all import bind_layers
from scapy.all import send, IP, TCP
from scapy.all import sniff
from scapy import *

class ALBION(Packet):
    name = "ALBION"
    fields_desc = [ BitField("request_id",       0, 64),
                    BitField("opration",         0, 32),
                    BitField("address",          0, 64),
                    BitField("time",             0, 32),
                    BitField("num",              0, 32),
                    BitField("index",            0, 32),
                    BitField("CS_id_1",          0, 32),
                    BitField("CS_offset_1",      0, 32),
                    BitField("CS_id_2",          0, 32),
                    BitField("CS_offset_2",      0, 32),
                    BitField("CS_id_3",          0, 32),
                    BitField("CS_offset_3",      0, 32)]
    
class ALBION_DATA(Packet):
    name = "ALBION_DATA"
    fields_desc = [ BitField("data_1",       0, 32),
                    BitField("data_2",       0, 32),
                    BitField("data_3",       0, 32),
                    BitField("data_4",       0, 32),
                    BitField("data_5",       0, 32),
                    BitField("data_6",       0, 32),
                    BitField("data_7",       0, 32),
                    BitField("data_8",       0, 32),
                    BitField("data_9",       0, 32),
                    BitField("data_10",       0, 32),
                    BitField("data_11",       0, 32),
                    BitField("data_12",       0, 32)]

database1 = [None] * 100
database2 = [None] * 100
database3 = [None] * 100
database4 = [None] * 100

def CallBack1(packet):
    data = ''
    if packet[ALBION].opration > 9 and packet[ALBION].opration < 13:
        if packet[ALBION_DATA].data_1 != 0:
            data = data + chr(packet[ALBION_DATA].data_1)
        if packet[ALBION_DATA].data_2 != 0:
            data = data + chr(packet[ALBION_DATA].data_2)
        if packet[ALBION_DATA].data_3 != 0:
            data = data + chr(packet[ALBION_DATA].data_3)
        if packet[ALBION_DATA].data_4 != 0:
            data = data + chr(packet[ALBION_DATA].data_4)
        if packet[ALBION_DATA].data_5 != 0:
            data = data + chr(packet[ALBION_DATA].data_5)
        if packet[ALBION_DATA].data_6 != 0:
            data = data + chr(packet[ALBION_DATA].data_6)
        if packet[ALBION_DATA].data_7 != 0:
            data = data + chr(packet[ALBION_DATA].data_7)
        if packet[ALBION_DATA].data_8 != 0:
            data = data + chr(packet[ALBION_DATA].data_8)
        if packet[ALBION_DATA].data_9 != 0:
            data = data + chr(packet[ALBION_DATA].data_9)
        if packet[ALBION_DATA].data_10 != 0:
            data = data + chr(packet[ALBION_DATA].data_10)
        if packet[ALBION_DATA].data_11 != 0:
            data = data + chr(packet[ALBION_DATA].data_11)
        if packet[ALBION_DATA].data_12 != 0:
            data = data + chr(packet[ALBION_DATA].data_12)
        database1[packet[ALBION].address] = data
        packet[ALBION].opration = packet[ALBION].opration + 20
        #print("CS1: write",packet[ALBION].address,"with",data)
        sendp(packet, iface=iface1, verbose = 0)

def CallBack2(packet):
    data = ''
    if packet[ALBION].opration > 9 and packet[ALBION].opration < 13:
        if packet[ALBION_DATA].data_1 != 0:
            data = data + chr(packet[ALBION_DATA].data_1)
        if packet[ALBION_DATA].data_2 != 0:
            data = data + chr(packet[ALBION_DATA].data_2)
        if packet[ALBION_DATA].data_3 != 0:
            data = data + chr(packet[ALBION_DATA].data_3)
        if packet[ALBION_DATA].data_4 != 0:
            data = data + chr(packet[ALBION_DATA].data_4)
        if packet[ALBION_DATA].data_5 != 0:
            data = data + chr(packet[ALBION_DATA].data_5)
        if packet[ALBION_DATA].data_6 != 0:
            data = data + chr(packet[ALBION_DATA].data_6)
        if packet[ALBION_DATA].data_7 != 0:
            data = data + chr(packet[ALBION_DATA].data_7)
        if packet[ALBION_DATA].data_8 != 0:
            data = data + chr(packet[ALBION_DATA].data_8)
        if packet[ALBION_DATA].data_9 != 0:
            data = data + chr(packet[ALBION_DATA].data_9)
        if packet[ALBION_DATA].data_10 != 0:
            data = data + chr(packet[ALBION_DATA].data_10)
        if packet[ALBION_DATA].data_11 != 0:
            data = data + chr(packet[ALBION_DATA].data_11)
        if packet[ALBION_DATA].data_12 != 0:
            data = data + chr(packet[ALBION_DATA].data_12)
        database2[packet[ALBION].address] = data
        packet[ALBION].opration = packet[ALBION].opration + 20
        #print("CS2: write",packet[ALBION].address,"with",data)
        sendp(packet, iface=iface2, verbose = 0)

def CallBack3(packet):
    data = ''
    if packet[ALBION].opration > 9 and packet[ALBION].opration < 13:
        if packet[ALBION_DATA].data_1 != 0:
            data = data + chr(packet[ALBION_DATA].data_1)
        if packet[ALBION_DATA].data_2 != 0:
            data = data + chr(packet[ALBION_DATA].data_2)
        if packet[ALBION_DATA].data_3 != 0:
            data = data + chr(packet[ALBION_DATA].data_3)
        if packet[ALBION_DATA].data_4 != 0:
            data = data + chr(packet[ALBION_DATA].data_4)
        if packet[ALBION_DATA].data_5 != 0:
            data = data + chr(packet[ALBION_DATA].data_5)
        if packet[ALBION_DATA].data_6 != 0:
            data = data + chr(packet[ALBION_DATA].data_6)
        if packet[ALBION_DATA].data_7 != 0:
            data = data + chr(packet[ALBION_DATA].data_7)
        if packet[ALBION_DATA].data_8 != 0:
            data = data + chr(packet[ALBION_DATA].data_8)
        if packet[ALBION_DATA].data_9 != 0:
            data = data + chr(packet[ALBION_DATA].data_9)
        if packet[ALBION_DATA].data_10 != 0:
            data = data + chr(packet[ALBION_DATA].data_10)
        if packet[ALBION_DATA].data_11 != 0:
            data = data + chr(packet[ALBION_DATA].data_11)
        if packet[ALBION_DATA].data_12 != 0:
            data = data + chr(packet[ALBION_DATA].data_12)
        database3[packet[ALBION].address] = data
        packet[ALBION].opration = packet[ALBION].opration + 20
        #print("CS3: write",packet[ALBION].address,"with",data)
        sendp(packet, iface=iface3, verbose = 0)

def CallBack4(packet):
    data = ''
    if packet[ALBION].opration > 9 and packet[ALBION].opration < 13:
        if packet[ALBION_DATA].data_1 != 0:
            data = data + chr(packet[ALBION_DATA].data_1)
        if packet[ALBION_DATA].data_2 != 0:
            data = data + chr(packet[ALBION_DATA].data_2)
        if packet[ALBION_DATA].data_3 != 0:
            data = data + chr(packet[ALBION_DATA].data_3)
        if packet[ALBION_DATA].data_4 != 0:
            data = data + chr(packet[ALBION_DATA].data_4)
        if packet[ALBION_DATA].data_5 != 0:
            data = data + chr(packet[ALBION_DATA].data_5)
        if packet[ALBION_DATA].data_6 != 0:
            data = data + chr(packet[ALBION_DATA].data_6)
        if packet[ALBION_DATA].data_7 != 0:
            data = data + chr(packet[ALBION_DATA].data_7)
        if packet[ALBION_DATA].data_8 != 0:
            data = data + chr(packet[ALBION_DATA].data_8)
        if packet[ALBION_DATA].data_9 != 0:
            data = data + chr(packet[ALBION_DATA].data_9)
        if packet[ALBION_DATA].data_10 != 0:
            data = data + chr(packet[ALBION_DATA].data_10)
        if packet[ALBION_DATA].data_11 != 0:
            data = data + chr(packet[ALBION_DATA].data_11)
        if packet[ALBION_DATA].data_12 != 0:
            data = data + chr(packet[ALBION_DATA].data_12)
        database4[packet[ALBION].address] = data
        packet[ALBION].opration = packet[ALBION].opration + 20
        #print("CS4: write",packet[ALBION].address,"with",data)
        sendp(packet, iface=iface4, verbose = 0)

def sniff_thread_1():
    sniff(iface=iface1,prn=CallBack1)

def sniff_thread_2():
    sniff(iface=iface2,prn=CallBack2)

def sniff_thread_3():
    sniff(iface=iface3,prn=CallBack3)

def sniff_thread_4():
    sniff(iface=iface4,prn=CallBack4)

iface1 = 'enp134s0f0np0'
iface2 = 'enp59s0f0np0'
iface3 = 'enp134s0f1np1'
iface4 = 'enp59s0f1np1'
bind_layers(Ether, ALBION, type=0x5555)
bind_layers(ALBION, ALBION_DATA)

if __name__ == '__main__':
    t1 = threading.Thread(target=sniff_thread_1,args=())
    t1.start()
    t2 = threading.Thread(target=sniff_thread_2,args=())
    t2.start()
    t3 = threading.Thread(target=sniff_thread_3,args=())
    t3.start()
    t4 = threading.Thread(target=sniff_thread_4,args=())
    t4.start()
    while 1:
        op = input('op:\n')
        op = op.split(' ')
        if op[0] == 'show':
            if len(op) < 2:
                print("ARG_ERROR")
                continue
            if op[1] == '1':
                print("CS1:",database1)
            if op[1] == '2':
                print("CS2:",database2)
            if op[1] == '3':
                print("CS3:",database3)
            if op[1] == '4':
                print("CS4:",database4)

