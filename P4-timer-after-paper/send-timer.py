import time

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
                    BitField("state_9",          0,  8),]

def CallBack(packet):
    packet.show()

iface = 'enp24s0f1np1'
bind_layers(Ether, ALBION, type=0x5555)
bind_layers(ALBION, ALBION_DATA)

#sniff(iface=iface,prn=CallBack)



if __name__ == '__main__':
    pkt = Ether(type=0x5555, dst='ff:ff:ff:ff:ff:ff') / ALBION(opration=100,address = 14000000) / ALBION_TIMER(times = 0,const_time = 1000 )
    # pkt.show()
    ticka = time.time()
    sendp(pkt, iface=iface)
    tickb = time.time()
    print(tickb - ticka)
