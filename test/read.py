import pyshark, sys
from scapy.all import Dot11ProbeReq

capure = pyshark.FileCapture(sys.argv[1])

for packet in capure:
    if Dot11ProbeReq in packet:
        print(packet)
        