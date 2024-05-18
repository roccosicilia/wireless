import pyshark, sys
from scapy.all import Dot11ProbeReq

capture = pyshark.FileCapture(sys.argv[1])

probe = [pkt for pkt in capture if Dot11ProbeReq in pkt]

for packet in probe:
    print(packet)
