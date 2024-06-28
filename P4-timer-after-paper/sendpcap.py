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
    fields_desc = [ BitField("uns",              0, 16),
                    BitField("request_id",       0, 64),
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

class ALBION_TIMER(Packet):
    name = "ALBION_TIMER"
    fields_desc = [ BitField("times",            0, 32),
                    BitField("const_time",       0, 32),
                    BitField("refresh",          0, 32),
                    BitField("request_id_high_0",0, 32),
                    BitField("request_id_low_0", 0, 32),
                    BitField("state_0",          0, 32),
                    BitField("request_id_high_1",0, 32),
                    BitField("request_id_low_1", 0, 32),
                    BitField("state_1",          0, 32),
                    BitField("request_id_high_2",0, 32),
                    BitField("request_id_low_2", 0, 32),
                    BitField("state_2",          0, 32),
                    BitField("request_id_high_3",0, 32),
                    BitField("request_id_low_3", 0, 32),
                    BitField("state_3",          0, 32),
                    BitField("request_id_high_4",0, 32),
                    BitField("request_id_low_4", 0, 32),
                    BitField("state_4",          0, 32),
                    BitField("request_id_high_5",0, 32),
                    BitField("request_id_low_5", 0, 32),
                    BitField("state_5",          0, 32),
                    BitField("request_id_high_6",0, 32),
                    BitField("request_id_low_6", 0, 32),
                    BitField("state_6",          0, 32),
                    BitField("request_id_high_7",0, 32),
                    BitField("request_id_low_7", 0, 32),
                    BitField("state_7",          0, 32),
                    BitField("request_id_high_8",0, 32),
                    BitField("request_id_low_8", 0, 32),
                    BitField("state_8",          0, 32),
                    BitField("request_id_high_9",0, 32),
                    BitField("request_id_low_9", 0, 32),
                    BitField("state_9",          0, 32),]

data_time = [[None,None]] * 100

def CallBack(packet):
    if ALBION in packet:
        if packet[ALBION].opration == 20 :
            print("Address:",packet[ALBION].address,"Block!")
            print("op:")
        elif packet[ALBION].opration == 34 :
            print("Address:",packet[ALBION].address,"Success!")
            print("op:")
            #data_time[0][1] = time.time()
            #print(data_time[0][1] - data_time[0][0])


def sniff_thread():
    sniff(iface=iface,prn=CallBack)

iface = 'enp24s0f1np1'
bind_layers(Ether, ALBION, type=0x5555)
bind_layers(ALBION, ALBION_DATA)

#sniff(iface=iface,prn=CallBack)

op_list = ["1","100","50"]



if __name__ == '__main__':
    t1 = threading.Thread(target=sniff_thread,args=())
    #t1.start()
    while 1:
        op = input("op:\n")
        op = op.split(" ")
        if op[0] not in op_list:
            print("OP_ERROR")
        else:
            op[0] = int(op[0])
            if op[0] == 1:
                if len(op) < 3:
                    print("ARG_ERROR")
                    continue
                op[1] = int(op[1])
                pkt = Ether(type=0x5555, dst='ff:ff:ff:ff:ff:ff') / ALBION(request_id=0,opration=1,address = op[1],time=0,num=0) / ALBION_DATA(data_1 = ord("A"))
                if len(op[2]) > 0:
                    pkt[ALBION_DATA].data_1 = ord(op[2][0])
                if len(op[2]) > 1:
                    pkt[ALBION_DATA].data_2 = ord(op[2][1])
                if len(op[2]) > 2:
                    pkt[ALBION_DATA].data_3 = ord(op[2][2])
                if len(op[2]) > 3:
                    pkt[ALBION_DATA].data_4 = ord(op[2][3])
                if len(op[2]) > 4:
                    pkt[ALBION_DATA].data_5 = ord(op[2][4])
                if len(op[2]) > 5:
                    pkt[ALBION_DATA].data_6 = ord(op[2][5])
                if len(op[2]) > 6:
                    pkt[ALBION_DATA].data_7 = ord(op[2][6])
                if len(op[2]) > 7:
                    pkt[ALBION_DATA].data_8 = ord(op[2][7])
                if len(op[2]) > 8:
                    pkt[ALBION_DATA].data_9 = ord(op[2][8])
                if len(op[2]) > 9:
                    pkt[ALBION_DATA].data_10 = ord(op[2][9])
                if len(op[2]) > 10:
                    pkt[ALBION_DATA].data_11 = ord(op[2][10])
                if len(op[2]) > 11:
                    pkt[ALBION_DATA].data_11 = ord(op[2][11])
                i = 0
                sendp(pkt, iface=iface)
                while i < 5000:
                    i = i+ 1
                    sendp(pkt, iface=iface)
                #data_time[0][0] = time.time()
            elif op[0] == 100:
                if len(op) < 2:
                    print("ARG_ERROR")
                    continue
                pkt = Ether(type=0x5555, dst='ff:ff:ff:ff:ff:ff') / ALBION(request_id=1,opration=op[0],address = 0,time=0,num=0) / ALBION_TIMER(const_time = int(op[1]))
                sendp(pkt, iface=iface, verbose = 0)
            elif op[0] == 50:
                for i in range(0,100):
                    pkt = Ether(type=0x5555, dst='ff:ff:ff:ff:ff:ff') / ALBION(request_id=1,opration=1,address = i,time=0,num=0) / ALBION_DATA(data_1 = ord("A"))
                    sendp(pkt, iface=iface, verbose = 0)
                    data_time[0][0] = time.time()
