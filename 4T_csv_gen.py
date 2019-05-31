
from ipaddress import ip_address, ip_network, ip_interface



listofip = []
for k in ip_network("10.0.0.0/16"):
    listofip.append(str(k))
#list will have 65536 ips

#csv_columns = ['srcIP', 'dstIP', 'Port']

src_ip = listofip[47443]
cidr = src_ip + '/27'

print(cidr)
print(str(ip_interface(cidr).network))
print((ip_network(ip + '/27', strict=False)[0]))

netmask = str(ip_interface(ip + '/27').netmask)
print(netmask)