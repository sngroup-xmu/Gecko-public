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
    if ALBION in packet:
        if packet[ALBION].opration == 1 :
            if num[packet[ALBION].address] == 0:
                packet[ALBION].opration = 2
                packet[ALBION].CS_id_1 = (packet[ALBION].address)%4+1
                packet[ALBION].CS_offset_1 = packet[ALBION].address
                packet[ALBION].CS_id_2 = (packet[ALBION].address+1)%4+1
                packet[ALBION].CS_offset_2 = packet[ALBION].address
                packet[ALBION].CS_id_3 = (packet[ALBION].address+2)%4+1
                packet[ALBION].CS_offset_3 = packet[ALBION].address
                sendp(packet, iface=iface, verbose = 0)
                database[packet[ALBION].address] = [0,0,0]
                database[packet[ALBION].address][0] = packet[ALBION].CS_id_1
                database[packet[ALBION].address][1] = packet[ALBION].CS_id_2
                database[packet[ALBION].address][2] = packet[ALBION].CS_id_3
                num[packet[ALBION].address] = 3
            else:
                print("")
                print("block! address:",packet[ALBION].address)
                packet[ALBION].opration = 20
                sendp(packet, iface=iface, verbose = 0)
                print("op:")
        elif packet[ALBION].opration == 200 :
            print("aaaa!!!!")
            print("op:")
        elif packet[ALBION].opration == 35 :
            num[packet[ALBION].address] = 0
        elif packet[ALBION].opration == 100 :
            if packet[ALBION_TIMER].state_0 != 0:
                print("\n+-------warning---------+")
                print("|    address:", packet[ALBION_TIMER].request_id_low_0)
                print("|      state:", packet[ALBION_TIMER].state_0)
                aa = database[packet[ALBION_TIMER].request_id_low_0].copy()
                ba = packet[ALBION_TIMER].state_0
                if ba < 4:
                    aa[2] = 0
                else:
                    ba = ba - 4
                if ba < 2:
                    aa[1] = 0
                else:
                    ba = ba - 2
                if ba < 1:
                    aa[0] = 0
                else:
                    ba = ba - 1
                print("| no success:", aa)
                print("+-----------------------+")
            if packet[ALBION_TIMER].state_1 != 0:
                print("\n+-------warning---------+")
                print("|    address:", packet[ALBION_TIMER].request_id_low_1)
                print("|      state:", packet[ALBION_TIMER].state_1)
                aa = database[packet[ALBION_TIMER].request_id_low_1].copy()
                ba = packet[ALBION_TIMER].state_1
                if ba < 4:
                    aa[2] = 0
                else:
                    ba = ba - 4
                if ba < 2:
                    aa[1] = 0
                else:
                    ba = ba - 2
                if ba < 1:
                    aa[0] = 0
                else:
                    ba = ba - 1
                print("| no success:", aa)
                print("+-----------------------+")
            if packet[ALBION_TIMER].state_2 != 0:
                print("\n+-------warning---------+")
                print("|    address:", packet[ALBION_TIMER].request_id_low_2)
                print("|      state:", packet[ALBION_TIMER].state_2)
                aa = database[packet[ALBION_TIMER].request_id_low_2].copy()
                ba = packet[ALBION_TIMER].state_2
                if ba < 4:
                    aa[2] = 0
                else:
                    ba = ba - 4
                if ba < 2:
                    aa[1] = 0
                else:
                    ba = ba - 2
                if ba < 1:
                    aa[0] = 0
                else:
                    ba = ba - 1
                print("| no success:", aa)
                print("+-----------------------+")
            if packet[ALBION_TIMER].state_3 != 0:
                print("\n+-------warning---------+")
                print("|    address:", packet[ALBION_TIMER].request_id_low_3)
                print("|      state:", packet[ALBION_TIMER].state_3)
                aa = database[packet[ALBION_TIMER].request_id_low_3].copy()
                ba = packet[ALBION_TIMER].state_3
                if ba < 4:
                    aa[2] = 0
                else:
                    ba = ba - 4
                if ba < 2:
                    aa[1] = 0
                else:
                    ba = ba - 2
                if ba < 1:
                    aa[0] = 0
                else:
                    ba = ba - 1
                print("| no success:", aa)
                print("+-----------------------+")
            if packet[ALBION_TIMER].state_4 != 0:
                print("\n+-------warning---------+")
                print("|    address:", packet[ALBION_TIMER].request_id_low_4)
                print("|      state:", packet[ALBION_TIMER].state_4)
                aa = database[packet[ALBION_TIMER].request_id_low_4].copy()
                ba = packet[ALBION_TIMER].state_4
                if ba < 4:
                    aa[2] = 0
                else:
                    ba = ba - 4
                if ba < 2:
                    aa[1] = 0
                else:
                    ba = ba - 2
                if ba < 1:
                    aa[0] = 0
                else:
                    ba = ba - 1
                print("| no success:", aa)
                print("+-----------------------+")
            if packet[ALBION_TIMER].state_5 != 0:
                print("\n+-------warning---------+")
                print("|    address:", packet[ALBION_TIMER].request_id_low_5)
                print("|      state:", packet[ALBION_TIMER].state_5)
                aa = database[packet[ALBION_TIMER].request_id_low_5].copy()
                ba = packet[ALBION_TIMER].state_5
                if ba < 4:
                    aa[2] = 0
                else:
                    ba = ba - 4
                if ba < 2:
                    aa[1] = 0
                else:
                    ba = ba - 2
                if ba < 1:
                    aa[0] = 0
                else:
                    ba = ba - 1
                print("| no success:", aa)
                print("+-----------------------+")
            if packet[ALBION_TIMER].state_6 != 0:
                print("\n+-------warning---------+")
                print("|    address:", packet[ALBION_TIMER].request_id_low_6)
                print("|      state:", packet[ALBION_TIMER].state_6)
                aa = database[packet[ALBION_TIMER].request_id_low_6].copy()
                ba = packet[ALBION_TIMER].state_6
                if ba < 4:
                    aa[2] = 0
                else:
                    ba = ba - 4
                if ba < 2:
                    aa[1] = 0
                else:
                    ba = ba - 2
                if ba < 1:
                    aa[0] = 0
                else:
                    ba = ba - 1
                print("| no success:", aa)
                print("+-----------------------+")
            if packet[ALBION_TIMER].state_7 != 0:
                print("\n+-------warning---------+")
                print("|    address:", packet[ALBION_TIMER].request_id_low_7)
                print("|      state:", packet[ALBION_TIMER].state_7)
                aa = database[packet[ALBION_TIMER].request_id_low_7].copy()
                ba = packet[ALBION_TIMER].state_7
                if ba < 4:
                    aa[2] = 0
                else:
                    ba = ba - 4
                if ba < 2:
                    aa[1] = 0
                else:
                    ba = ba - 2
                if ba < 1:
                    aa[0] = 0
                else:
                    ba = ba - 1
                print("| no success:", aa)
                print("+-----------------------+")
            print("op:")


iface = 'enp24s0f0np0'
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
bind_layers(ALBION, ALBION_DATA, opration=9)

def sniff_thread():
    sniff(iface=iface,prn=CallBack)

op_list = ["show","100",'print','clear']

if __name__ == '__main__':
    t1 = threading.Thread(target=sniff_thread,args=())
    t1.start()
    while 1:
        op = input("op:\n")
        op = op.split(" ")
        if op[0] not in op_list:
            print("OP_ERROR")
        else:
            if op[0] == "show":
                if len(op) < 2:
                    print("ARG_ERROR")
                    continue
                print("+--------show--------+")
                print("|  record:",database[int(op[1])],"|")
                print("+--------------------+")
            if op[0] == "print":
                print(database)
            if op[0] == "clear":
                database = [None] * 100


