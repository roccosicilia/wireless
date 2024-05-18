import pyshark, sys
from scapy.all import Dot11ProbeReq, rdpcap

# capture = pyshark.FileCapture(sys.argv[1])
capture = rdpcap(sys.argv[1])

# probe = [pkt for pkt in capture if Dot11ProbeReq in pkt]
probe = [pkt for pkt in capture if 'Wildcard' in str(pkt)]

for packet in probe:
    print(packet)
