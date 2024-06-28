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
                    BitField("data_10",      0, 32),
                    BitField("data_11",      0, 32),
                    BitField("data_12",      0, 32)]

class ALBION_TIMER(Packet):
    name = "ALBION_TIMER"
    fields_desc = [ BitField("times",            0, 32),
                    BitField("const_time",       0, 32),
                    BitField("refresh",          0, 32),
                    BitField("request_id_high_0",0, 32),
                    BitField("request_id_low_0", 0, 32),
                    BitField("state_0",          0,  8),
                    BitField("request_id_high_1",0, 32),
                    BitField("request_id_low_1", 0, 32),
                    BitField("state_1",          0,  8),
                    BitField("request_id_high_2",0, 32),
                    BitField("request_id_low_2", 0, 32),
                    BitField("state_2",          0,  8),
                    BitField("request_id_high_3",0, 32),
                    BitField("request_id_low_3", 0, 32),
                    BitField("state_3",          0,  8),
                    BitField("request_id_high_4",0, 32),
                    BitField("request_id_low_4", 0, 32),
                    BitField("state_4",          0,  8),
                    BitField("request_id_high_5",0, 32),
                    BitField("request_id_low_5", 0, 32),
                    BitField("state_5",          0,  8),
                    BitField("request_id_high_6",0, 32),
                    BitField("request_id_low_6", 0, 32),
                    BitField("state_6",          0,  8),
                    BitField("request_id_high_7",0, 32),
                    BitField("request_id_low_7", 0, 32),
                    BitField("state_7",          0,  8),
                    BitField("request_id_high_8",0, 32),
                    BitField("request_id_low_8", 0, 32),
                    BitField("state_8",          0,  8),
                    BitField("request_id_high_9",0, 32),
                    BitField("request_id_low_9", 0, 32),
                    BitField("state_9",          0,  8)]

database = [None] * 100
num = [0] * 100

def CallBack(packet):
    packet.show()


iface1 = 'enp24s0f0np0'
iface2 = 'enp24s0f1np1'
iface3 = 'enp134s0f0np0'
iface4 = 'enp134s0f1np1'
iface5 = 'enp59s0f0np0'
iface6 = 'enp59s0f1np1'
'''
bind_layers(Ether, ALBION, type=0x5555)
bind_layers(ALBION, ALBION_TIMER, opration=100)
bind_layers(ALBION, ALBION_DATA, opration=0)
bind_layers(ALBION, ALBION_DATA, opration=1)
bind_layers(ALBION, ALBION_DATA, opration=2)
bind_layers(ALBION, ALBION_DATA, opration=3)
bind_layers(ALBION, ALBION_DATA, opration=4)
bind_layers(ALBION, ALBION_DATA, opration=5)
bind_layers(ALBION, ALBION_DATA, opration=6)
bind_layers(ALBION, ALBION_DATA, opration=7)
bind_layers(ALBION, ALBION_DATA, opration=8)
bind_layers(ALBION, ALBION_DATA, opration=9)'''

def sniff_thread1():
    sniff(iface=iface1,prn=CallBack)
def sniff_thread2():
    sniff(iface=iface2,prn=CallBack)
def sniff_thread3():
    sniff(iface=iface3,prn=CallBack)
def sniff_thread4():
    sniff(iface=iface4,prn=CallBack)
def sniff_thread5():
    sniff(iface=iface5,prn=CallBack)
def sniff_thread6():
    sniff(iface=iface6,prn=CallBack)

op_list = ["show","100",'print','clear']

if __name__ == '__main__':
    t1 = threading.Thread(target=sniff_thread1,args=())
    t1.start()
    t2 = threading.Thread(target=sniff_thread2,args=())
    t2.start()
    t3 = threading.Thread(target=sniff_thread3,args=())
    t3.start()
    t4 = threading.Thread(target=sniff_thread4,args=())
    t4.start()
    t5 = threading.Thread(target=sniff_thread5,args=())
    t5.start()
    t6 = threading.Thread(target=sniff_thread6,args=())
    t6.start()
    while 1:
        op = input("op:\n")
        op = op.split(" ")


