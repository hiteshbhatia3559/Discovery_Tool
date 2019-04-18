import nmap
import csv

nm = nmap.PortScanner()
nm.scan('172.16.100.227','22-8000')

ip = nm['172.16.100.227']

print(ip['tcp'].keys())
