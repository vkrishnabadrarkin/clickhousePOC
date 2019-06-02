import csv
import pandas
from ipaddress import ip_address, ip_network, ip_interface
import ast

badr = "[(80,'https','TCP'),(443,'https','TCP'),(123,'ntp','UDP'),(22,'ssh','TCP'),(53,'dns','UDP'),(445,'microsoft-ds','UDP'),(389,'ldap','UDP'),(514,'syslog','TCP'),(137,'netbios-ns','TCP'),(902,'ideafarm-door','TCP')]"

badr = ast.literal_eval(badr)
print(badr[1][1])