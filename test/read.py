import pyshark, sys

capure = pyshark.FileCapture(sys.argn[1])

for packet in capure:
    print(packet)

