import nmap
import csv

nm = nmap.PortScanner()
print("Scanner done")
nm.scan('192.168.1.254','22-9000')
print("Scanning now")
ip = nm['192.168.1.254']

print(ip)
