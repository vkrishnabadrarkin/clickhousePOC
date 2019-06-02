import asyncio
import time
import random
import csv
from ipaddress import ip_network, ip_address

csvDataFile = 'Ip_vm_metadata_final.csv'
listofip = []
for k in ip_network("10.0.0.0/16"):
    listofip.append(str(k))
# first 2500 ips -srcIP's and next 2000ips -dstIP's
# srcIP - listofip[0:2499], dstIp - listofip[2500:4499]

csv_columns = ['srcIP', 'dstIP', 'port', 'portName', 'protocol', 'trafficType', 'networkLayer', 'shared']
ports_name_protocol = [(80, 'https', 'TCP'), (443, 'https', 'TCP'), (123, 'ntp', 'UDP'), (22, 'ssh', 'TCP'),
                       (53, 'dns', 'UDP'), (445, 'microsoft-ds', 'UDP'), (389, 'ldap', 'UDP'), (514, 'syslog', 'TCP'),
                       (137, 'netbios-ns', 'TCP'), (902, 'ideafarm-door', 'TCP')]

# csv_file_columns_ip_vm_metadata = ['ipAddress', 'port', 'port_name', 'protocol', 'vm_name', 'vm_otype', 'vm_oid', 'subnet_ip', 'subnet_netmask', 'subnet_prefixLength', 'subnet_networkAddress', 'subnet_cidr', 'subnet_start', 'subnet_end', 'ipAddressType', 'privateAddress', 'source', 'Ipmetadata_domain', 'ipmetadata_isp', 'host_name', 'host_otype', 'host_oid', 'dnsinfo_ipdomain', 'dnsinfo_ip', 'dnsinfo_domainname', 'dnsinfo_hostname', 'dnsinfo_source', 'k8s_service_name', 'k8s_service_otype', 'k8s_service_oid', 'k8s_cluster_name', 'k8s_cluster_otype', 'k8s_cluster_oid', 'k8s_namespace_name', 'k8s_namespace_otype', 'k8s_namespace_oid', 'k8s_node_name', 'k8s_node_otype', 'k8s_node_oid', 'IP_entity_name', 'IP_entity_otype', 'IP_entity_oid', 'Nic_name', 'Nic_otype', 'Nic_oid', 'sg_name', 'sg_otype', 'sg_oid', 'IP_set_name', 'IP_set_otype', 'IP_set_oid', 'STag_name', 'STag_otype', 'STag_oid', 'L2net_name', 'L2net_otype', 'L2net_oid', 'Grp_name', 'Grp_otype', 'Grp_oid', 'cluster_name', 'cluster_otype', 'cluster_oid', 'RP_name', 'RP_otype', 'RP_oid', 'DC_name', 'DC_otype', 'DC_oid', 'EP_name', 'EP_otype', 'EP_oid', 'managerNSX_name', 'managerNSX_otype', 'managerNSX_oid', 'lookupDomain_name', 'lookupDomain_otype', 'lookupDomain_oid', 'vpc_name', 'vpc_otype', 'vpc_oid', 'transportNode_name', 'transportNode_otype', 'transportNode_oid', 'Dvpg_name', 'Dvpg_otype', 'Dvpg_oid', 'Dvs_name', 'Dvs_otype', 'Dvs_oid', 'ipAddress', 'port', 'port_name', 'protocol', 'vm_name', 'vm_otype', 'vm_oid', 'subnet_ip', 'subnet_netmask', 'subnet_prefixLength', 'subnet_networkAddress', 'subnet_cidr', 'subnet_start', 'subnet_end', 'ipAddressType', 'privateAddress', 'source', 'Ipmetadata_domain', 'ipmetadata_isp', 'host_name', 'host_otype', 'host_oid', 'dnsinfo_ipdomain', 'dnsinfo_ip', 'dnsinfo_domainname', 'dnsinfo_hostname', 'dnsinfo_source', 'k8s_service_name', 'k8s_service_otype', 'k8s_service_oid', 'k8s_cluster_name', 'k8s_cluster_otype', 'k8s_cluster_oid', 'k8s_namespace_name', 'k8s_namespace_otype', 'k8s_namespace_oid', 'k8s_node_name', 'k8s_node_otype', 'k8s_node_oid', 'IP_entity_name', 'IP_entity_otype', 'IP_entity_oid', 'Nic_name', 'Nic_otype', 'Nic_oid', 'sg_name', 'sg_otype', 'sg_oid', 'IP_set_name', 'IP_set_otype', 'IP_set_oid', 'STag_name', 'STag_otype', 'STag_oid', 'L2net_name', 'L2net_otype', 'L2net_oid', 'Grp_name', 'Grp_otype', 'Grp_oid', 'cluster_name', 'cluster_otype', 'cluster_oid', 'RP_name', 'RP_otype', 'RP_oid', 'DC_name', 'DC_otype', 'DC_oid', 'EP_name', 'EP_otype', 'EP_oid', 'managerNSX_name', 'managerNSX_otype', 'managerNSX_oid', 'lookupDomain_name', 'lookupDomain_otype', 'lookupDomain_oid', 'vpc_name', 'vpc_otype', 'vpc_oid', 'transportNode_name', 'transportNode_otype', 'transportNode_oid', 'Dvpg_name', 'Dvpg_otype', 'Dvpg_oid', 'Dvs_name', 'Dvs_otype', 'Dvs_oid']
# csv_info = [(0, 'ipAddress'), (1, 'port'), (2, 'port_name'), (3, 'protocol'), (4, 'vm_name'), (5, 'vm_otype'), (6, 'vm_oid'), (7, 'subnet_ip'), (8, 'subnet_netmask'), (9, 'subnet_prefixLength'), (10, 'subnet_networkAddress'), (11, 'subnet_cidr'), (12, 'subnet_start'), (13, 'subnet_end'), (14, 'ipAddressType'), (15, 'privateAddress'), (16, 'source'), (17, 'Ipmetadata_domain'), (18, 'ipmetadata_isp'), (19, 'host_name'), (20, 'host_otype'), (21, 'host_oid'), (22, 'dnsinfo_ipdomain'), (23, 'dnsinfo_ip'), (24, 'dnsinfo_domainname'), (25, 'dnsinfo_hostname'), (26, 'dnsinfo_source'), (27, 'k8s_service_name'), (28, 'k8s_service_otype'), (29, 'k8s_service_oid'), (30, 'k8s_cluster_name'), (31, 'k8s_cluster_otype'), (32, 'k8s_cluster_oid'), (33, 'k8s_namespace_name'), (34, 'k8s_namespace_otype'), (35, 'k8s_namespace_oid'), (36, 'k8s_node_name'), (37, 'k8s_node_otype'), (38, 'k8s_node_oid'), (39, 'IP_entity_name'), (40, 'IP_entity_otype'), (41, 'IP_entity_oid'), (42, 'Nic_name'), (43, 'Nic_otype'), (44, 'Nic_oid'), (45, 'sg_name'), (46, 'sg_otype'), (47, 'sg_oid'), (48, 'IP_set_name'), (49, 'IP_set_otype'), (50, 'IP_set_oid'), (51, 'STag_name'), (52, 'STag_otype'), (53, 'STag_oid'), (54, 'L2net_name'), (55, 'L2net_otype'), (56, 'L2net_oid'), (57, 'Grp_name'), (58, 'Grp_otype'), (59, 'Grp_oid'), (60, 'cluster_name'), (61, 'cluster_otype'), (62, 'cluster_oid'), (63, 'RP_name'), (64, 'RP_otype'), (65, 'RP_oid'), (66, 'DC_name'), (67, 'DC_otype'), (68, 'DC_oid'), (69, 'EP_name'), (70, 'EP_otype'), (71, 'EP_oid'), (72, 'managerNSX_name'), (73, 'managerNSX_otype'), (74, 'managerNSX_oid'), (75, 'lookupDomain_name'), (76, 'lookupDomain_otype'), (77, 'lookupDomain_oid'), (78, 'vpc_name'), (79, 'vpc_otype'), (80, 'vpc_oid'), (81, 'transportNode_name'), (82, 'transportNode_otype'), (83, 'transportNode_oid'), (84, 'Dvpg_name'), (85, 'Dvpg_otype'), (86, 'Dvpg_oid'), (87, 'Dvs_name'), (88, 'Dvs_otype'), (89, 'Dvs_oid'), (90, 'ipAddress'), (91, 'port'), (92, 'port_name'), (93, 'protocol'), (94, 'vm_name'), (95, 'vm_otype'), (96, 'vm_oid'), (97, 'subnet_ip'), (98, 'subnet_netmask'), (99, 'subnet_prefixLength'), (100, 'subnet_networkAddress'), (101, 'subnet_cidr'), (102, 'subnet_start'), (103, 'subnet_end'), (104, 'ipAddressType'), (105, 'privateAddress'), (106, 'source'), (107, 'Ipmetadata_domain'), (108, 'ipmetadata_isp'), (109, 'host_name'), (110, 'host_otype'), (111, 'host_oid'), (112, 'dnsinfo_ipdomain'), (113, 'dnsinfo_ip'), (114, 'dnsinfo_domainname'), (115, 'dnsinfo_hostname'), (116, 'dnsinfo_source'), (117, 'k8s_service_name'), (118, 'k8s_service_otype'), (119, 'k8s_service_oid'), (120, 'k8s_cluster_name'), (121, 'k8s_cluster_otype'), (122, 'k8s_cluster_oid'), (123, 'k8s_namespace_name'), (124, 'k8s_namespace_otype'), (125, 'k8s_namespace_oid'), (126, 'k8s_node_name'), (127, 'k8s_node_otype'), (128, 'k8s_node_oid'), (129, 'IP_entity_name'), (130, 'IP_entity_otype'), (131, 'IP_entity_oid'), (132, 'Nic_name'), (133, 'Nic_otype'), (134, 'Nic_oid'), (135, 'sg_name'), (136, 'sg_otype'), (137, 'sg_oid'), (138, 'IP_set_name'), (139, 'IP_set_otype'), (140, 'IP_set_oid'), (141, 'STag_name'), (142, 'STag_otype'), (143, 'STag_oid'), (144, 'L2net_name'), (145, 'L2net_otype'), (146, 'L2net_oid'), (147, 'Grp_name'), (148, 'Grp_otype'), (149, 'Grp_oid'), (150, 'cluster_name'), (151, 'cluster_otype'), (152, 'cluster_oid'), (153, 'RP_name'), (154, 'RP_otype'), (155, 'RP_oid'), (156, 'DC_name'), (157, 'DC_otype'), (158, 'DC_oid'), (159, 'EP_name'), (160, 'EP_otype'), (161, 'EP_oid'), (162, 'managerNSX_name'), (163, 'managerNSX_otype'), (164, 'managerNSX_oid'), (165, 'lookupDomain_name'), (166, 'lookupDomain_otype'), (167, 'lookupDomain_oid'), (168, 'vpc_name'), (169, 'vpc_otype'), (170, 'vpc_oid'), (171, 'transportNode_name'), (172, 'transportNode_otype'), (173, 'transportNode_oid'), (174, 'Dvpg_name'), (175, 'Dvpg_otype'), (176, 'Dvpg_oid'), (177, 'Dvs_name'), (178, 'Dvs_otype'), (179, 'Dvs_oid')]
with open(csvDataFile) as csvBigData:
    data = list(csv.reader(csvBigData))

csv_file = '4Tuple_final.csv'


def write_to_csv(dict_data):
    try:
        with open(csv_file, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            for datarow in dict_data:
                writer.writerow(datarow)
    except IOError:
        print("I/O error")


def fetch_data(i, j):
    sIP = int(ip_address(listofip[i]))
    dIP = int(ip_address(listofip[j]))
    port_name_protocol = random.choice(ports_name_protocol)
    port = port_name_protocol[0]
    port_name = port_name_protocol[1]
    protocol = port_name_protocol[2]
    trafictype = 'EAST_WEST_TRAFFIC'
    shared = 0
    if data[i][7] == data[j][7]:
        networkLayer = 'LAYER_2'
        shared = 1
    else:
        networkLayer = 'LAYER_3'

    return_value = {
        "srcIP": sIP,
        "dstIP": dIP,
        "port": port,
        "portName": port_name,
        "protocol": protocol,
        "trafficType": trafictype,
        "networkLayer": networkLayer,
        "shared": shared
    }
    return return_value


def fetch_datas(i):
    return [fetch_data(i, j) for j in range(12500, 16500)]


async def fill_events(_loop):
    for i in range(12500):
        listDataForSingleVm = fetch_datas(i)
        await write_to_csv(listDataForSingleVm)
        print(f"four tuples {i}th set inserted")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    start = time.time()
    print("inserter started at", time.ctime(start))
    loop.run_until_complete(fill_events(loop))
    end = time.time()
    took = end - start
    print(f"inserter ended at {time.ctime(end)}; took: {took} seconds")
