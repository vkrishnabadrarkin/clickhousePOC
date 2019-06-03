import time
import random
import csv
from ipaddress import ip_network, ip_address
count = 0
listofip = []
for k in ip_network("10.0.0.0/16"):
    listofip.append(str(k))

ports_name_protocol = [(80, 'https', 'TCP'), (443, 'https', 'TCP'), (123, 'ntp', 'UDP'), (22, 'ssh', 'TCP'),
                       (53, 'dns', 'UDP'), (445, 'microsoft-ds', 'UDP'), (389, 'ldap', 'UDP'), (514, 'syslog', 'TCP'),
                       (137, 'netbios-ns', 'TCP'), (902, 'ideafarm-door', 'TCP')]

def write_to_csv(dict_data):
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(dict_data)
        csvfile.close()
    except IOError:
        print("I/O error")


def fetch_data(i, j):
    global count
    sIP = int(ip_address(listofip[i]))
    dIP = int(ip_address(listofip[j]))
    port_name_protocol = random.choice(ports_name_protocol)
    port = port_name_protocol[0]
    port_name = port_name_protocol[1]
    protocol = port_name_protocol[2]
    count = count + 1
    #print(f'created {count} datas')
    return [sIP, dIP, port, port_name, protocol]

if __name__ == '__main__':
    start = time.time()
    print("inserter started at", time.ctime(start))
    events = [fetch_data(i,j) for i in range(12500) for j in range(12500,16500)]
    csv_file = '4Tuple_final_all_at_once.csv'
    write_to_csv(events)
    end = time.time()
    took = end - start
    print(f"inserter ended at {time.ctime(end)}; took: {took} seconds")
