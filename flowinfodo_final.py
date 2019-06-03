import csv
import asyncio
import time
import datetime
import random
from ipaddress import ip_network, ip_address
import pandas as pd
import inserter_config

#csv index = [(0, 'ipAddress'), (1, 'vm_name'), (2, 'vm_otype'), (3, 'vm_oid'), (4, 'subnet_ip'), (5, 'subnet_netmask'), (6, 'subnet_prefixLength'), (7, 'subnet_networkAddress'), (8, 'subnet_cidr'), (9, 'subnet_start'), (10, 'subnet_end'), (11, 'ipAddressType'), (12, 'privateAddress'), (13, 'source'), (14, 'Ipmetadata_domain'), (15, 'ipmetadata_isp'), (16, 'host_name'), (17, 'host_otype'), (18, 'host_oid'), (19, 'dnsinfo_ipdomain'), (20, 'dnsinfo_ip'), (21, 'dnsinfo_domainname'), (22, 'dnsinfo_hostname'), (23, 'dnsinfo_source'), (24, 'k8s_service_name'), (25, 'k8s_service_otype'), (26, 'k8s_service_oid'), (27, 'k8s_cluster_name'), (28, 'k8s_cluster_otype'), (29, 'k8s_cluster_oid'), (30, 'k8s_namespace_name'), (31, 'k8s_namespace_otype'), (32, 'k8s_namespace_oid'), (33, 'k8s_node_name'), (34, 'k8s_node_otype'), (35, 'k8s_node_oid'), (36, 'IP_entity_name'), (37, 'IP_entity_otype'), (38, 'IP_entity_oid'), (39, 'Nic_name'), (40, 'Nic_otype'), (41, 'Nic_oid'), (42, 'sg_name'), (43, 'sg_otype'), (44, 'sg_oid'), (45, 'IP_set_name'), (46, 'IP_set_otype'), (47, 'IP_set_oid'), (48, 'STag_name'), (49, 'STag_otype'), (50, 'STag_oid'), (51, 'L2net_name'), (52, 'L2net_otype'), (53, 'L2net_oid'), (54, 'Grp_name'), (55, 'Grp_otype'), (56, 'Grp_oid'), (57, 'cluster_name'), (58, 'cluster_otype'), (59, 'cluster_oid'), (60, 'RP_name'), (61, 'RP_otype'), (62, 'RP_oid'), (63, 'DC_name'), (64, 'DC_otype'), (65, 'DC_oid'), (66, 'managerNSX_name'), (67, 'managerNSX_otype'), (68, 'managerNSX_oid'), (69, 'lookupDomain_name'), (70, 'lookupDomain_otype'), (71, 'lookupDomain_oid'), (72, 'vpc_name'), (73, 'vpc_otype'), (74, 'vpc_oid'), (75, 'transportNode_name'), (76, 'transportNode_otype'), (77, 'transportNode_oid'), (78, 'Dvpg_name'), (79, 'Dvpg_otype'), (80, 'Dvpg_oid'), (81, 'Dvs_name'), (82, 'Dvs_otype'), (83, 'Dvs_oid')]

#metadata_columns = ['ipAddress', 'vm_name', 'vm_otype', 'vm_oid', 'subnet_ip', 'subnet_netmask', 'subnet_prefixLength', 'subnet_networkAddress', 'subnet_cidr', 'subnet_start', 'subnet_end', 'ipAddressType', 'privateAddress', 'source', 'Ipmetadata_domain', 'ipmetadata_isp', 'host_name', 'host_otype', 'host_oid', 'dnsinfo_ipdomain', 'dnsinfo_ip', 'dnsinfo_domainname', 'dnsinfo_hostname', 'dnsinfo_source', 'k8s_service_name', 'k8s_service_otype', 'k8s_service_oid', 'k8s_cluster_name', 'k8s_cluster_otype', 'k8s_cluster_oid', 'k8s_namespace_name', 'k8s_namespace_otype', 'k8s_namespace_oid', 'k8s_node_name', 'k8s_node_otype', 'k8s_node_oid', 'IP_entity_name', 'IP_entity_otype', 'IP_entity_oid', 'Nic_name', 'Nic_otype', 'Nic_oid', 'sg_name', 'sg_otype', 'sg_oid', 'IP_set_name', 'IP_set_otype', 'IP_set_oid', 'STag_name', 'STag_otype', 'STag_oid', 'L2net_name', 'L2net_otype', 'L2net_oid', 'Grp_name', 'Grp_otype', 'Grp_oid', 'cluster_name', 'cluster_otype', 'cluster_oid', 'RP_name', 'RP_otype', 'RP_oid', 'DC_name', 'DC_otype', 'DC_oid', 'managerNSX_name', 'managerNSX_otype', 'managerNSX_oid', 'lookupDomain_name', 'lookupDomain_otype', 'lookupDomain_oid', 'vpc_name', 'vpc_otype', 'vpc_oid', 'transportNode_name', 'transportNode_otype', 'transportNode_oid', 'Dvpg_name', 'Dvpg_otype', 'Dvpg_oid', 'Dvs_name', 'Dvs_otype', 'Dvs_oid']
#4t_columns = ['srcIP', 'dstIP', 'port', 'portName', 'protocol', 'trafficType', 'networkLayer', 'shared']
#start,end change in db table
#ip ADDRESSS as int
#tags as array of strings
total_inserted_events = 0
total_flows_rows = 7200000000
modelkey_oid_range = range(9876543219876,9883743219876)
collector_id_range = range(9883743219876,9890943219876)
attribute_model_oid_range = range(9890943219876,9898143219876)
firewall_manager_model_oid_range = range(9898143219876,9905343219876)
reporter_entity_oid_range = range(9905343219876,9912543219876)
flowdomain_modelkey_oid_range = range(9912543219876,9919743219876)
srvcEP_oid_range = range(9919743219876,9926943219876)

metaDataFile = 'Ip_vm_metadata_final.csv'
fourTupleDataFile = '4Tuple_final.csv'
event_date = datetime.datetime(2019, 6, 3)
with open(metaDataFile) as csvIPData:
    ipMetaData = list(csv.reader(csvIPData))
#ipMetaData = pd.read_csv('Ip_vm_metadata_final.csv')
with open(fourTupleDataFile) as csvTUPLEData:
    fourTupleData = list(csv.reader(csvTUPLEData))


def attach_metadata_gen_Metricdata(j,f,timelist,metriclist,sch_version):
    global total_inserted_events
    src_ip = fourTupleData[j][0]
    dst_ip = fourTupleData[j][1]
    port = fourTupleData[j][2]
    port_name = fourTupleData[j][3]
    port_display = '['+str(port)+'] ' + port_name
    protocol = fourTupleData[j][4]
    #src_ip_meta_row
    p = j//4000
    #dst_ip_meta_row
    q = 12500 + (j%4000)
    src_vm_name = ipMetaData[p][1]
    dst_vm_name = ipMetaData[q][1]
    flow_name = src_vm_name + dst_vm_name + '-' + port_name + '-' + protocol
    flow_tag_list = ['TAG_TRAFFIC_TYPE_UNKNOWN', 'TAG_INTERNET_TRAFFIC', 'TAG_EAST_WEST_TRAFFIC', 'TAG_VM_VM_TRAFFIC',
                     'TAG_VM_PHY_TRAFFIC', 'TAG_PHY_PHY_TRAFFIC', 'TAG_SRC_IP_VMKNIC', 'TAG_DST_IP_VMKNIC',
                     'TAG_SRC_IP_ROUTER_INT', 'TAG_DST_IP_ROUTER_INT', 'TAG_SRC_IP_VM', 'TAG_DST_IP_VM',
                     'TAG_SRC_IP_INTERNET', 'TAG_DST_IP_INTERNET', 'TAG_SRC_IP_PHYSICAL', 'TAG_DST_IP_PHYSICAL',
                     'TAG_SAME_HOST', 'TAG_DIFF_HOST', 'TAG_COMMON_HOST_INFO_UNKNOWN', 'TAG_SHARED_SERVICE',
                     'TAG_NOT_SHARED_SERVICE', 'TAG_NETWORK_SWITCHED', 'TAG_NETWORK_ROUTED', 'TAG_NETWORK_UNKNOWN',
                     'TAG_SRC_IP_VTEP', 'TAG_DST_IP_VTEP', 'TAG_UNICAST', 'TAG_BROADCAST', 'TAG_MULTICAST',
                     'TAG_SRC_IP_LINK_LOCAL', 'TAG_DST_IP_LINK_LOCAL', 'TAG_SRC_IP_CLASS_E', 'TAG_DST_IP_CLASS_E',
                     'TAG_SRC_IP_CLASS_A_RESERVED', 'TAG_DST_IP_CLASS_A_RESERVED', 'TAG_INVALID_IP_PACKETS',
                     'TAG_NOT_ANALYZED', 'TAG_GENERIC_INTERNET_SRC_IP', 'TAG_SNAT_DNAT_FLOW', 'TAG_NATTED',
                     'TAG_MULTINICS', 'TAG_MULTI_NATRULE', 'TAG_SRC_VC', 'TAG_DST_VC', 'TAG_SRC_AWS', 'TAG_DST_AWS',
                     'TAG_WITHIN_DC', 'TAG_DIFF_DC', 'TAG_SRC_IP_IN_SNAT_RULE_TARGET',
                     'TAG_DST_IP_IN_DNAT_RULE_ORIGINAL', 'TAG_SRC_IP_MULTI_NAT_RULE', 'TAG_DNAT_IP_MULTI_NAT_RULE',
                     'DEPRECATED_TAG_DST_IP_IN_SNAT_RULE_TARGET', 'DEPRECATED_TAG_SRC_IP_IN_DNAT_RULE_ORIGINAL',
                     'TAG_INVALID_IP_DOMAIN', 'TAG_WITHIN_VPC', 'TAG_DIFF_VPC', 'TAG_SRC_IP_IN_MULTIPLE_SUBNETS',
                     'TAG_DST_IP_IN_MULTIPLE_SUBNETS', 'TAG_SFLOW', 'TAG_PRE_NAT_FLOW', 'TAG_POST_NAT_FLOW',
                     'TAG_LOGICAL_FLOW', 'TAG_SRC_K8S_POD', 'TAG_DST_K8S_POD', 'TAG_POD_POD_TRAFFIC',
                     'TAG_VM_POD_TRAFFIC', 'TAG_POD_PHYSICAL_TRAFFIC']
    modelKey = modelkey_oid_range[total_inserted_events]
    collector_id = collector_id_range[total_inserted_events]
    if (f==0):
        lastactivity = 0
    else:
        lastactivity = timelist[f-1]

    flow_version_data = {
        "name": flow_name,
        "time" : timelist[f],
        "modelkey_cid": 8912345,
        "modelkey_otype": 515,
        "modelkey_oid": modelKey,  # changed from total inserted events
        "port.start": port,
        "port.end": port,
        "port.display": str(port),
        "port.ianaName": port_name,
        "port.ianaPortDisplay": port_display,
        "Protocol": protocol,
        "srcIP.prefixLength": 32,
        "srcIP.ipAddress": int(src_ip),
        "srcIP.netMask": '255.255.255.255',
        "srcIP.networkAddress": str(ip_address(int(src_ip))),
        "srcIP.cidr": str(ip_network(int(src_ip))),
        "srcIP.start" : src_ip,
        "srcIP.end": src_ip,
        "srcIP.ipaddresstype": 'ENDPOINT',
        "srcIP.privateaddress": 1,
        "srcIP.Source": 'TBD',
        "srcIP.Ipmetadata_domain": 'TBD',
        "srcIP.Ipmetadata_isp": 'TBD',
        "dstIP.prefixLength": 32,
        "dstIP.ipAddress": dst_ip,
        "dstIP.netMask": '255.255.255.255',
        "dstIP.networkAddress": str(ip_address(int(dst_ip))),
        "dstIP.cidr": str(ip_network(int(dst_ip))),
        "dstIP.start": dst_ip,
        "dstIP.end": dst_ip,
        "dstIP.ipaddresstype": 'ENDPOINT',
        "dstIP.privateaddress": 1,
        "dstIP.Source": 'TBD',
        "dstIP.Ipmetadata_domain": 'TBD',
        "dstIP.Ipmetadata_isp": 'TBD',
        "trafficType": 'EAST_WEST_TRAFFIC',
        "shared": fourTupleData[7],
        "networkLayer": fourTupleData[6],
        "srcsubnet.prefixLength": ipMetaData[p][6],
        "srcsubnet.ipAddress": ipMetaData[p][4],
        "srcsubnet.netMask": ipMetaData[p][5],
        "srcsubnet.networkAddress": ipMetaData[p][7],
        "srcsubnet.cidr": ipMetaData[p][8],
        "srcsubnet.start": ipMetaData[p][9],
        "srcsubnet.end": ipMetaData[p][10],
        "srcsubnet.ipaddresstype": 'SUBNET',
        "srcsubnet.privateaddress": 1,
        "srcsubnet.Source": ipMetaData[p][13],
        "srcsubnet.Ipmetadata_domain": ipMetaData[p][14],
        "srcsubnet.Ipmetadata_isp": ipMetaData[p][15],
        "dstsubnet.prefixLength": ipMetaData[q][6],
        "dstsubnet.ipAddress": ipMetaData[q][4],
        "dstsubnet.netMask": ipMetaData[q][5],
        "dstsubnet.networkAddress": ipMetaData[q][7],
        "dstsubnet.cidr": ipMetaData[q][8],
        "dstsubnet.start": ipMetaData[q][9],
        "dstsubnet.end": ipMetaData[q][10],
        "dstsubnet.ipaddresstype": 'SUBNET',
        "dstsubnet.privateaddress": 1,
        "dstsubnet.Source": ipMetaData[q][13],
        "dstsubnet.Ipmetadata_domain": ipMetaData[q][14],
        "dstsubnet.Ipmetadata_isp": ipMetaData[q][15],
        "withinhost": int(ipMetaData[p][16]==ipMetaData[q][16]),
        "typetag": random.sample(flow_tag_list,4),
        "__searchTags": [flow_name, src_vm_name, dst_vm_name],
        "__related_entities": ['flows', 'traffic'],
        "srcVmTags": ['admin@vmware.com', 'root@vmware.com'],
        "dstVmTags": ['vmware@vmware.com', 'vrni@vmware.com'],
        "attribute.reportedaction": 'ALLOW',
        "attribute.reportedRuleId": 'RID-' + str(modelKey),
        "attribute.collectorId": collector_id,
        "attribute_rule.name": 'AT_RULE' + str(modelKey),
        "attribute_rule.modelkey_otype": 7,
        "attribute_rule.modelkey_oid": attribute_model_oid_range[total_inserted_events],
        "attribute_firewallmanager.name": 'AT_firewall_manager' + str(modelKey),
        "attribute_firewallmanager.modelkey_otype": 8,
        "attribute_firewallmanager.modelkey_oid": firewall_manager_model_oid_range[total_inserted_events],
        "activedpIds": collector_id,
        "typeTagsPacked": 'KCC0IABACBAA',
        "protectionStatus": 'PROTECTED',
        "flowAction": 'ALLOW',
        "srcDnsInfo.ipDomain": ipMetaData[p][19],
        "srcDnsInfo.ip": ipMetaData[p][20],
        "srcDnsInfo.domainName": ipMetaData[p][21],
        "srcDnsInfo.hostName": ipMetaData[p][22],
        "srcDnsInfo.source": ipMetaData[p][23],
        "dstDnsInfo.ipDomain": ipMetaData[q][19],
        "dstDnsInfo.ip": ipMetaData[q][20],
        "dstDnsInfo.domainName": ipMetaData[q][21],
        "dstDnsInfo.hostName": ipMetaData[q][22],
        "dstDnsInfo.source": ipMetaData[q][23],
        "reporterEntity.collectorId": collector_id,
        "reporterEntity_reporter.name": 'reporter' + str(modelKey),
        "reporterEntity_reporter.modelkey_otype": 603,
        "reporterEntity_reporter.modelkey_oid": reporter_entity_oid_range[total_inserted_events],
        "SchemaVersion": sch_version,
        "lastActivity": lastactivity,
        "activity": timelist[f],
        "srck8Info.k8scollectorId": collector_id,
        "srck8Info_k8sservice.name": ipMetaData[p][24],
        "srck8Info_k8sservice.modelkey_otype": ipMetaData[p][25],
        "srck8Info_k8sservice.modelkey_oid": ipMetaData[p][26],
        "srck8Info_k8scluster.name": ipMetaData[p][27],
        "srck8Info_k8scluster.modelkey_otype": ipMetaData[p][28],
        "srck8Info_k8scluster.modelkey_oid": ipMetaData[p][29],
        "srck8Info_k8snamespace.name": ipMetaData[p][30],
        "srck8Info_k8snamespace.modelkey_otype": ipMetaData[p][31],
        "srck8Info_k8snamespace.modelkey_oid": ipMetaData[p][32],
        "srck8Info_k8snode.name": ipMetaData[p][33],
        "srck8Info_k8snode.modelkey_otype": ipMetaData[p][34],
        "srck8Info_k8snode.modelkey_oid": ipMetaData[p][35],
        "dstk8Info.k8scollectorId": collector_id,
        "dstk8Info_k8sservice.name": ipMetaData[q][24],
        "dstk8Info_k8sservice.modelkey_otype": ipMetaData[q][25],
        "dstk8Info_k8sservice.modelkey_oid": ipMetaData[q][26],
        "dstk8Info_k8scluster.name": ipMetaData[q][27],
        "dstk8Info_k8scluster.modelkey_otype": ipMetaData[q][28],
        "dstk8Info_k8scluster.modelkey_oid": ipMetaData[q][29],
        "dstk8Info_k8snamespace.name": ipMetaData[q][30],
        "dstk8Info_k8snamespace.modelkey_otype": ipMetaData[q][31],
        "dstk8Info_k8snamespace.modelkey_oid": ipMetaData[q][32],
        "dstk8Info_k8snode.name": ipMetaData[q][33],
        "dstk8Info_k8snode.modelkey_otype": ipMetaData[q][34],
        "dstk8Info_k8snode.modelkey_oid": ipMetaData[q][35],
        "srcIpEntity.name": ipMetaData[p][36],
        "srcIpEntity.modelkey_otype": ipMetaData[p][37],
        "srcIpEntity.modelkey_oid": ipMetaData[p][38],
        "dstIpEntity.name": ipMetaData[q][36],
        "dstIpEntity.modelkey_otype": ipMetaData[q][37],
        "dstIpEntity.modelkey_oid": ipMetaData[q][38],
        "srcNic.name": ipMetaData[p][39],
        "srcNic.modelkey_otype": ipMetaData[p][40],
        "srcNic.modelkey_oid": ipMetaData[p][41],
        "dstNic.name": ipMetaData[q][39],
        "dstNic.modelkey_otype": ipMetaData[q][40],
        "dstNic.modelkey_oid": ipMetaData[q][41],
        "srcVm.name": src_vm_name,
        "srcVm.modelkey_otype": ipMetaData[p][2],
        "srcVm.modelkey_oid": ipMetaData[p][3],
        "dstVm.name": dst_vm_name,
        "dstVm.modelkey_otype": ipMetaData[q][2],
        "dstVm.modelkey_oid": ipMetaData[q][3],
        "srcSg.name": ipMetaData[p][42],
        "srcSg.modelkey_otype": ipMetaData[p][43],
        "srcSg.modelkey_oid": ipMetaData[p][44],
        "dstSg.name": ipMetaData[q][42],
        "dstSg.modelkey_otype": ipMetaData[q][43],
        "dstSg.modelkey_oid": ipMetaData[q][44],
        "srcIpSet.name": ipMetaData[p][45],
        "srcIpSet.modelkey_otype": ipMetaData[p][46],
        "srcIpSet.modelkey_oid": ipMetaData[p][47],
        "dstIpSet.name": ipMetaData[q][45],
        "dstIpSet.modelkey_otype": ipMetaData[q][46],
        "dstIpSet.modelkey_oid": ipMetaData[q][47],
        "srcSt.name": ipMetaData[p][48],
        "srcSt.modelkey_otype": ipMetaData[p][49],
        "srcSt.modelkey_oid": ipMetaData[p][50],
        "dstSt.name": ipMetaData[q][48],
        "dstSt.modelkey_otype": ipMetaData[q][49],
        "dstSt.modelkey_oid": ipMetaData[q][50],
        "srcL2Net.name": ipMetaData[p][51],
        "srcL2Net.modelkey_otype": ipMetaData[p][52],
        "srcL2Net.modelkey_oid": ipMetaData[p][53],
        "dstL2Net.name": ipMetaData[q][51],
        "dstL2Net.modelkey_otype": ipMetaData[q][52],
        "dstL2Net.modelkey_oid": ipMetaData[q][53],
        "srcGroup.name": ipMetaData[p][54],
        "srcGroup.modelkey_otype": ipMetaData[p][55],
        "srcGroup.modelkey_oid": ipMetaData[p][56],
        "dstGroup.name": ipMetaData[q][54],
        "dstGroup.modelkey_otype": ipMetaData[q][55],
        "dstGroup.modelkey_oid": ipMetaData[q][56],
        "srcCluster.name": ipMetaData[p][57],
        "srcCluster.modelkey_otype": ipMetaData[p][58],
        "srcCluster.modelkey_oid": ipMetaData[p][59],
        "dstCluster.name": ipMetaData[q][57],
        "dstCluster.modelkey_otype": ipMetaData[q][58],
        "dstCluster.modelkey_oid": ipMetaData[q][59],
        "srcRp.name": ipMetaData[p][60],
        "srcRp.modelkey_otype": ipMetaData[p][61],
        "srcRp.modelkey_oid": ipMetaData[p][62],
        "dstRp.name": ipMetaData[q][60],
        "dstRp.modelkey_otype": ipMetaData[q][61],
        "dstRp.modelkey_oid": ipMetaData[q][62],
        "srcDc.name": ipMetaData[p][63],
        "srcDc.modelkey_otype": ipMetaData[p][64],
        "srcDc.modelkey_oid": ipMetaData[p][65],
        "dstDc.name": ipMetaData[q][63],
        "dstDc.modelkey_otype": ipMetaData[q][64],
        "dstDc.modelkey_oid": ipMetaData[q][65],
        "srcHost.name": ipMetaData[p][16],
        "srcHost.modelkey_otype": ipMetaData[p][17],
        "srcHost.modelkey_oid": ipMetaData[p][18],
        "dstHost.name": ipMetaData[q][16],
        "dstHost.modelkey_otype": ipMetaData[q][17],
        "dstHost.modelkey_oid": ipMetaData[q][18],
        "svcEP.name": dst_ip + port_display,
        "svcEP.modelkey_otype": 6065,
        "svcEP.modelkey_oid": srvcEP_oid_range[total_inserted_events],
        "srcManagers.name": ipMetaData[p][66],
        "srcManagers.modelkey_otype": ipMetaData[p][67],
        "srcManagers.modelkey_oid": ipMetaData[p][68],
        "dstManagers.name": ipMetaData[q][66],
        "dstManagers.modelkey_otype": ipMetaData[q][67],
        "dstManagers.modelkey_oid": ipMetaData[q][68],
        "flowDomain.name": 'GLOBAL',
        "flowDomain.modelkey_otype": 658,
        "flowDomain.modelkey_oid": flowdomain_modelkey_oid_range[total_inserted_events],
        "srcLookupDomain.name": ipMetaData[p][69],
        "srcLookupDomain.modelkey_otype": ipMetaData[p][70],
        "srcLookupDomain.modelkey_oid": ipMetaData[p][71],
        "dstLookupDomain.name": ipMetaData[q][69],
        "dstLookupDomain.modelkey_otype": ipMetaData[q][70],
        "dstLookupDomain.modelkey_oid": ipMetaData[q][71],
        "srcVpc.name": ipMetaData[p][72],
        "srcVpc.modelkey_otype": ipMetaData[p][73],
        "srcVpc.modelkey_oid": ipMetaData[p][74],
        "dstVpc.name": ipMetaData[q][72],
        "dstVpc.modelkey_otype": ipMetaData[q][73],
        "dstVpc.modelkey_oid": ipMetaData[q][74],
        "srcTransportNode.name": ipMetaData[p][75],
        "srcTransportNode.modelkey_otype": ipMetaData[p][76],
        "srcTransportNode.modelkey_oid": ipMetaData[p][77],
        "dstTransportNode.name": ipMetaData[q][75],
        "dstTransportNode.modelkey_otype": ipMetaData[q][76],
        "dstTransportNode.modelkey_oid": ipMetaData[q][77],
        "srcDvpg.name": ipMetaData[p][78],
        "srcDvpg.modelkey_otype": ipMetaData[p][79],
        "srcDvpg.modelkey_oid": ipMetaData[p][80],
        "dstDvpg.name": ipMetaData[q][78],
        "dstDvpg.modelkey_otype": ipMetaData[q][79],
        "dstDvpg.modelkey_oid": ipMetaData[q][80],
        "srcDvs.name": ipMetaData[p][78],
        "srcDvs.modelkey_otype": ipMetaData[p][79],
        "srcDvs.modelkey_oid": ipMetaData[p][80],
        "dstDvs.name": ipMetaData[q][81],
        "dstDvs.modelkey_otype": ipMetaData[q][82],
        "dstDvs.modelkey_oid": ipMetaData[q][83],
        "metricData.totalBytes": metriclist[f][2],
        "metricData.srcBytes": metriclist[f][0],
        "metricData.dstBytes": metriclist[f][1],
        "metricData.totalPackets": metriclist[f][3],
        "metricData.allowedSessionCount": metriclist[f][4],
        "metricData.nsxTcpRtt_abs_max_ms": metriclist[f][5],
        "metricData.nsxTcpRtt_abs_avg_ms": metriclist[f][6]
    }
    return flow_version_data

def fetch_metadata_gen6_Metricdatas(j):
    total_6_active = []
    metric_6_active = []
    for i in range(100):
        event_datetime = event_date.replace(minute=random.randint(0, 59), second=random.randint(0,59))
        total_6_active.append(int(event_datetime.timestamp()))
        srcBytes = random.randint(2500000, 28000000)
        dstBytes = random.randint(2500000, 28000000)
        totalBytes = srcBytes + dstBytes
        totalPackets = random.randint(1, 100)
        sessionCount = random.randint(100, 300)
        rttMax = random.randint(20000, 70000)
        rttAvg = (rttMax * 2) // 3
        metric_6_active.append((srcBytes, dstBytes, totalBytes, totalPackets, sessionCount, rttMax, rttAvg))
    total_6_active.sort()
    sch_version = random.randint(1, 9)

    return [attach_metadata_gen_Metricdata(j,f,total_6_active,metric_6_active,sch_version) for f in range(6)]
csv_columns = ['name' ,'time', 'modelkey_cid' , 'modelkey_otype' , 'modelkey_oid' , 'port.start' , 'port.end' , 'port.display' , 'port.ianaName' , 'port.ianaPortDisplay' , 'Protocol' , 'srcIP.prefixLength' , 'srcIP.ipAddress' , 'srcIP.netMask' , 'srcIP.networkAddress' , 'srcIP.cidr' , 'srcIP.start' , 'srcIP.end' , 'srcIP.ipaddresstype' , 'srcIP.privateaddress' , 'srcIP.Source' , 'srcIP.Ipmetadata_domain' , 'srcIP.Ipmetadata_isp' , 'dstIP.prefixLength' , 'dstIP.ipAddress' , 'dstIP.netMask' , 'dstIP.networkAddress' , 'dstIP.cidr' , 'dstIP.start' , 'dstIP.end' , 'dstIP.ipaddresstype' , 'dstIP.privateaddress' , 'dstIP.Source' , 'dstIP.Ipmetadata_domain' , 'dstIP.Ipmetadata_isp' , 'trafficType' , 'shared' , 'networkLayer' , 'srcsubnet.prefixLength' , 'srcsubnet.ipAddress' , 'srcsubnet.netMask' , 'srcsubnet.networkAddress' , 'srcsubnet.cidr' , 'srcsubnet.start' , 'srcsubnet.end' , 'srcsubnet.ipaddresstype' , 'srcsubnet.privateaddress' , 'srcsubnet.Source' , 'srcsubnet.Ipmetadata_domain' , 'srcsubnet.Ipmetadata_isp' , 'dstsubnet.prefixLength' , 'dstsubnet.ipAddress' , 'dstsubnet.netMask' , 'dstsubnet.networkAddress' , 'dstsubnet.cidr' , 'dstsubnet.start' , 'dstsubnet.end' , 'dstsubnet.ipaddresstype' , 'dstsubnet.privateaddress' , 'dstsubnet.Source' , 'dstsubnet.Ipmetadata_domain' , 'dstsubnet.Ipmetadata_isp' , 'withinhost' , 'typetag' , '__searchTags' , '__related_entities' , 'srcVmTags' , 'dstVmTags' , 'attribute.reportedaction' , 'attribute.reportedRuleId' , 'attribute.collectorId' , 'attribute_rule.name' , 'attribute_rule.modelkey_otype' , 'attribute_rule.modelkey_oid' , 'attribute_firewallmanager.name' , 'attribute_firewallmanager.modelkey_otype' , 'attribute_firewallmanager.modelkey_oid' , 'activedpIds' , 'typeTagsPacked' , 'protectionStatus' , 'flowAction' , 'srcDnsInfo.ipDomain' , 'srcDnsInfo.ip' , 'srcDnsInfo.domainName' , 'srcDnsInfo.hostName' , 'srcDnsInfo.source' , 'dstDnsInfo.ipDomain' , 'dstDnsInfo.ip' , 'dstDnsInfo.domainName' , 'dstDnsInfo.hostName' , 'dstDnsInfo.source' , 'reporterEntity.collectorId' , 'reporterEntity_reporter.name' , 'reporterEntity_reporter.modelkey_otype' , 'reporterEntity_reporter.modelkey_oid' , 'SchemaVersion' , 'lastActivity' , 'activity' , 'srck8Info.k8scollectorId' , 'srck8Info_k8sservice.name' , 'srck8Info_k8sservice.modelkey_otype' , 'srck8Info_k8sservice.modelkey_oid' , 'srck8Info_k8scluster.name' , 'srck8Info_k8scluster.modelkey_otype' , 'srck8Info_k8scluster.modelkey_oid' , 'srck8Info_k8snamespace.name' , 'srck8Info_k8snamespace.modelkey_otype' , 'srck8Info_k8snamespace.modelkey_oid' , 'srck8Info_k8snode.name' , 'srck8Info_k8snode.modelkey_otype' , 'srck8Info_k8snode.modelkey_oid' , 'dstk8Info.k8scollectorId' , 'dstk8Info_k8sservice.name' , 'dstk8Info_k8sservice.modelkey_otype' , 'dstk8Info_k8sservice.modelkey_oid' , 'dstk8Info_k8scluster.name' , 'dstk8Info_k8scluster.modelkey_otype' , 'dstk8Info_k8scluster.modelkey_oid' , 'dstk8Info_k8snamespace.name' , 'dstk8Info_k8snamespace.modelkey_otype' , 'dstk8Info_k8snamespace.modelkey_oid' , 'dstk8Info_k8snode.name' , 'dstk8Info_k8snode.modelkey_otype' , 'dstk8Info_k8snode.modelkey_oid' , 'srcIpEntity.name' , 'srcIpEntity.modelkey_otype' , 'srcIpEntity.modelkey_oid' , 'dstIpEntity.name' , 'dstIpEntity.modelkey_otype' , 'dstIpEntity.modelkey_oid' , 'srcNic.name' , 'srcNic.modelkey_otype' , 'srcNic.modelkey_oid' , 'dstNic.name' , 'dstNic.modelkey_otype' , 'dstNic.modelkey_oid' , 'srcVm.name' , 'srcVm.modelkey_otype' , 'srcVm.modelkey_oid' , 'dstVm.name' , 'dstVm.modelkey_otype' , 'dstVm.modelkey_oid' , 'srcSg.name' , 'srcSg.modelkey_otype' , 'srcSg.modelkey_oid' , 'dstSg.name' , 'dstSg.modelkey_otype' , 'dstSg.modelkey_oid' , 'srcIpSet.name' , 'srcIpSet.modelkey_otype' , 'srcIpSet.modelkey_oid' , 'dstIpSet.name' , 'dstIpSet.modelkey_otype' , 'dstIpSet.modelkey_oid' , 'srcSt.name' , 'srcSt.modelkey_otype' , 'srcSt.modelkey_oid' , 'dstSt.name' , 'dstSt.modelkey_otype' , 'dstSt.modelkey_oid' , 'srcL2Net.name' , 'srcL2Net.modelkey_otype' , 'srcL2Net.modelkey_oid' , 'dstL2Net.name' , 'dstL2Net.modelkey_otype' , 'dstL2Net.modelkey_oid' , 'srcGroup.name' , 'srcGroup.modelkey_otype' , 'srcGroup.modelkey_oid' , 'dstGroup.name' , 'dstGroup.modelkey_otype' , 'dstGroup.modelkey_oid' , 'srcCluster.name' , 'srcCluster.modelkey_otype' , 'srcCluster.modelkey_oid' , 'dstCluster.name' , 'dstCluster.modelkey_otype' , 'dstCluster.modelkey_oid' , 'srcRp.name' , 'srcRp.modelkey_otype' , 'srcRp.modelkey_oid' , 'dstRp.name' , 'dstRp.modelkey_otype' , 'dstRp.modelkey_oid' , 'srcDc.name' , 'srcDc.modelkey_otype' , 'srcDc.modelkey_oid' , 'dstDc.name' , 'dstDc.modelkey_otype' , 'dstDc.modelkey_oid' , 'srcHost.name' , 'srcHost.modelkey_otype' , 'srcHost.modelkey_oid' , 'dstHost.name' , 'dstHost.modelkey_otype' , 'dstHost.modelkey_oid' , 'svcEP.name' , 'svcEP.modelkey_otype' , 'svcEP.modelkey_oid' , 'srcManagers.name' , 'srcManagers.modelkey_otype' , 'srcManagers.modelkey_oid' , 'dstManagers.name' , 'dstManagers.modelkey_otype' , 'dstManagers.modelkey_oid' ,'flowDomain.name', 'flowDomain.modelkey_otype', 'flowDomain.modelkey_oid', 'srcLookupDomain.name' , 'srcLookupDomain.modelkey_otype' , 'srcLookupDomain.modelkey_oid' , 'dstLookupDomain.name' , 'dstLookupDomain.modelkey_otype' , 'dstLookupDomain.modelkey_oid' , 'srcVpc.name' , 'srcVpc.modelkey_otype' , 'srcVpc.modelkey_oid' , 'dstVpc.name' , 'dstVpc.modelkey_otype' , 'dstVpc.modelkey_oid' , 'srcTransportNode.name' , 'srcTransportNode.modelkey_otype' , 'srcTransportNode.modelkey_oid' , 'dstTransportNode.name' , 'dstTransportNode.modelkey_otype' , 'dstTransportNode.modelkey_oid' , 'srcDvpg.name' , 'srcDvpg.modelkey_otype' , 'srcDvpg.modelkey_oid' , 'dstDvpg.name' , 'dstDvpg.modelkey_otype' , 'dstDvpg.modelkey_oid' , 'srcDvs.name' , 'srcDvs.modelkey_otype' , 'srcDvs.modelkey_oid' , 'dstDvs.name' , 'dstDvs.modelkey_otype' , 'dstDvs.modelkey_oid','metricData.totalBytes','metricData.srcBytes', 'metricData.dstBytes','metricData.totalPackets', 'metricData.allowedSessionCount','metricData.nsxTcpRtt_abs_max_ms', 'metricData.nsxTcpRtt_abs_avg_ms']

def write_to_csv(dict_data,i):
    csv_file = f'flow_{i+1}_hour_{((total_inserted_events)//300000)+1}_data.csv'
    try:
        with open(csv_file, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            for data in dict_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")


#each event occured 100 times in a day
k = 50000000
#(number of unique four tuples)
t = 6
#number of versions per hour
z = 300000
#number of rows in each csv
h = (k*t)/z
#(10000 files each file with z rows in an hour span)

if __name__ == '__main__':
    start = time.time()
    print("inserter started at", time.ctime(start))
    for i in range(1):
        for j in range(200000):
            events = fetch_metadata_gen6_Metricdatas(j)
            write_to_csv(events,i)
            total_inserted_events = total_inserted_events + 6
            print(f'written {j*6}-{total_inserted_events} rows')
    end = time.time()
    took = end - start
    print(f"inserter ended at {time.ctime(end)}; took: {took} seconds")