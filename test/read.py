import pyshark, sys

capure = pyshark.FileCapture(sys.argv[1])

for packet in capure:
    print(packet)

