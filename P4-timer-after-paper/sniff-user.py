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
                    BitField("CS_id",            0, 32),
                    BitField("CS_offset",        0, 32)]

def CallBack(packet):
    packet.show()

iface = 'enp59s0f1'
bind_layers(Ether, ALBION, type=0x5555)

sniff(iface=iface,prn=CallBack)



