import random
import time
import inserter_config
import asyncio
import asyncpool
import logging
import csv
import datetime

from ipaddress import ip_address, ip_network, ip_interface

god_number = 0

total_inserted_events = 0

event_date = datetime.datetime(2019, 6, 1)

listofip = []
for k in ip_network("10.0.0.0/18"):
    listofip.append(str(k))



def gen_ip(p):
    return listofip[p]


def generate_random_event(mins) -> dict:
    global god_number
    #god_number = god_number+1
    global event_date
    f_protocol = random.choice(['TCP', 'UDP'])
    traffic_type = random.choice(['EAST_WEST_TRAFFIC', 'INTERNET_TRAFFIC'])
    port_num = random.choice([443, 53, 80, 135, 2055, 412, 76, 3001, 2099, 11029, 1998, 1995, 2019])
    if port_num == 443:
        port_name = 'https'
    elif port_num == 53:
        port_name = 'dns'
    elif port_num == 80:
        port_name = 'https'
    elif port_num == 135:
        port_name = 'epmap'
    else:
        port_name = 'other'
    if port_name == 'dns':
        f_protocol = 'UDP'
        traffic_type = 'EAST_WEST_TRAFFIC'
    port_name_num = '[' + str(port_num) + ']' + port_name

    #VM_range = list(range(0, 131071))
    src_VM_num = (god_number % 10000)
    src_VM_name = 'VM' + str(src_VM_num)
    src_host_num = src_VM_num // 16
    src_host_name = 'HOST' + str(src_host_num)
    src_rp_num = src_VM_num // 8
    src_sg_num = src_VM_num // 6
    src_cluster_num = src_host_num // 8
    src_cluster_name = 'CLUSTER' + str(src_cluster_num)
    src_Nsx_vc_num = src_cluster_num // 16
    src_Nsx_manager_name = 'NSX' + str(src_Nsx_vc_num)
    src_VC_name = 'VC' + str(src_Nsx_vc_num)
    DC_name = 'DATACENTER101'
    #VM_range.remove(src_VM_num)
    dst_VM_num = (god_number//10000) + src_VM_num + 1
    dst_VM_name = 'VM' + str(dst_VM_num)
    dst_host_num = dst_VM_num // 16
    dst_host_name = 'HOST' + str(dst_host_num)
    dst_rp_num = dst_VM_num // 8
    dst_sg_num = dst_VM_num // 6
    dst_cluster_num = dst_host_num // 8
    dst_cluster_name = 'CLUSTER' + str(dst_cluster_num)
    dst_Nsx_vc_num = dst_cluster_num // 16
    dst_Nsx_manager_name = 'NSX' + str(dst_Nsx_vc_num)
    dst_VC_name = 'VC' + str(dst_Nsx_vc_num)
    DC_name = 'DATACENTER101'
    src_ip = gen_ip(src_VM_num)
    dst_ip = gen_ip(dst_VM_num)
    src_ip_cidr = src_ip + '/27'
    dst_ip_cidr = dst_ip + '/27'
    src_cidr = str(ip_interface(src_ip_cidr).network)
    src_network = src_cidr[:-4]
    src_netmask = str(ip_interface(src_ip_cidr).netmask)
    start_src_ip_int = int(ip_network(src_ip_cidr, strict=False)[0])
    end_src_ip_int = int(ip_network(src_ip_cidr, strict=False)[-1])
    dst_cidr = str(ip_interface(dst_ip_cidr).network)
    dst_network = dst_cidr[:-4]
    dst_netmask = str(ip_interface(dst_ip_cidr).netmask)
    start_dst_ip_int = int(ip_network(dst_ip_cidr, strict=False)[0])
    end_dst_ip_int = int(ip_network(dst_ip_cidr, strict=False)[-1])

    if (ip_address(dst_ip) in ip_network(src_ip_cidr, strict=False)):
        network_layer = 'LAYER_2'
    else:
        network_layer = 'LAYER_3'

    flow_name = src_ip + '- VM -' + str(src_VM_num)+ ' - ' + dst_ip +' - VM - '+ str(dst_VM_num) + port_name + f_protocol
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
    #new_list = random.choice(flow_tag_list)  # enum takes only one value
    new_list = flow_tag_list[god_number % 68]
    rep = ['ALLOW', 'DENY', 'DROP', 'REJECT', 'REDIRECT', 'DONT_REDIRECT']
    reported_action = rep[god_number % 6]
    rule_num = god_number % 88888
    ruleid = 'RULE' + str(rule_num)
    src_k8s_service_num = src_VM_num // 20
    src_k8s_cluster_num = src_VM_num // 10
    src_k8s_namespace = src_VM_num // 25
    src_k8s_node = src_VM_num // 10
    dst_k8s_service_num = dst_VM_num // 20
    dst_k8s_cluster_num = dst_VM_num // 10
    dst_k8s_namespace = dst_VM_num // 25
    dst_k8s_node = dst_VM_num // 10
    flowtype = random.choice(['PRE_NAT', 'POST_NAT', 'LOGICAL'])
    event_datetime = event_date.replace(
        hour=mins//60,
        minute=mins % 60)
    srcBytes = random.randint(200,800)
    dstBytes = random.randint(100,600)
    totalBytes = srcBytes + dstBytes
    totalPackets = random.randint(4,20)
    sessionCount = random.randint(100,300)
    rttMax = random.randint(20000,70000)
    rttAvg = (rttMax*2)//3


    return_value = {
        "name": flow_name,
        "time": event_datetime,
        "modelkey_cid": 12345,
        "modelkey_otype": 515,
        "modelkey_oid": int(time.time()), # changed from total inserted events
        "port.fstart": [port_num],
        "port.fend": [port_num],
        "port.display": [str(port_num)],
        "port.ianaName": [port_name],
        "port.ianaPortDisplay": [port_name_num],
        "fProtocol": f_protocol,
        "srcIP.prefixLength": [27],
        "srcIP.ipAddress": [src_ip],
        "srcIP.netMask": [src_netmask],
        "srcIP.networkAddress": [src_network],
        "srcIP.cidr": [src_cidr],
        "srcIP.fstart": [start_src_ip_int],
        "srcIP.fend": [end_src_ip_int],
        "srcIP.ipaddresstype": ['SUBNET'],
        "srcIP.privateaddress": [1],
        "srcIP.Source": ['TBD'],
        "srcIP.Ipmetadata_domain": ['TBD'],
        "srcIP.Ipmetadata_isp": ['TBD'],
        "dstIP.prefixLength": [27],
        "dstIP.ipAddress": [dst_ip],
        "dstIP.netMask": [dst_netmask],
        "dstIP.networkAddress": [dst_network],
        "dstIP.cidr": [dst_cidr],
        "dstIP.fstart": [start_dst_ip_int],
        "dstIP.fend": [end_dst_ip_int],
        "dstIP.ipaddresstype": ['TBD'],
        "dstIP.privateaddress": [1],
        "dstIP.Source": ['TBD'],
        "dstIP.Ipmetadata_domain": ['TBD'],
        "dstIP.Ipmetadata_isp": ['TBD'],
        "TrfficType": traffic_type,
        "shared": 1,
        "networkLayer": network_layer,
        "srcsubnet.prefixLength": [19],
        "srcsubnet.ipAddress": [src_ip + '/19'],
        "srcsubnet.netMask": [str(ip_interface(src_ip + '/19').netmask)],
        "srcsubnet.networkAddress": [str(ip_interface(src_ip + '/19').network)[:-4]],
        "srcsubnet.cidr": [str(ip_interface(src_ip + '/19').network)],
        "srcsubnet.fstart": [int(ip_network(src_ip + '/19', strict=False)[0])],
        "srcsubnet.fend": [int(ip_network(src_ip + '/19', strict=False)[-1])],
        "srcsubnet.ipaddresstype": ['SUBNET'],
        "srcsubnet.privateaddress": [1],
        "srcsubnet.Source": ['TBD'],
        "srcsubnet.Ipmetadata_domain": ['TBD'],
        "srcsubnet.Ipmetadata_isp": ['TBD'],
        "dstsubnet.prefixLength": [19],
        "dstsubnet.ipAddress": [dst_ip + '/19'],
        "dstsubnet.netMask": [str(ip_interface(dst_ip + '/19').netmask)],
        "dstsubnet.networkAddress": [str(ip_interface(dst_ip + '/19').network)[:-4]],
        "dstsubnet.cidr": [str(ip_interface(dst_ip + '/19').network)],
        "dstsubnet.fstart": [int(ip_network(dst_ip + '/19', strict=False)[0])],
        "dstsubnet.fend": [int(ip_network(dst_ip + '/19', strict=False)[-1])],
        "dstsubnet.ipaddresstype": ['SUBNET'],
        "dstsubnet.privateaddress": [1],
        "dstsubnet.Source": ['TBD'],
        "dstsubnet.Ipmetadata_domain": ['TBD'],
        "dstsubnet.Ipmetadata_isp": ['TBD'],
        "withinhost": int(src_host_num == dst_host_num),
        "typetag": new_list,
        "__searchTags": [flow_name, src_VM_name, dst_VM_name],
        "__related_entities": ['flows', 'traffic'],
        "srcVmTags": ['admin@vmware.com', 'badri@vmware.com'],
        "dstVmTags": ['vamsi@vmware.com', 'krishna@vmware.com'],
        "attribute.reportedaction": [reported_action],
        "attribute.reportedRuleId": [ruleid],
        "attribute.collectorId": [int(time.time()) // 8],
        "attribute_rule.name": ['AT_RULE' + str(int(time.time()))],
        "attribute_rule.modelkey_otype": [random.choice([7, 8, 603, 612, 663, 917, 5200])],
        "attribute_rule.modelkey_oid": [int(time.time())],
        "attribute_firewallmanager.name": ['AT_firewall_manager' + str(int(time.time()))],
        "attribute_firewallmanager.modelkey_otype": [random.choice([7, 8, 612])],
        "attribute_firewallmanager.modelkey_oid": [int(time.time())],
        "activedpIds": [int(time.time()) // 8],
        "typeTagsPacked": 'KCC0IABACBAA',
        "protectionStatus": 'PROTECTED',
        "flowAction": 'ALLOW',
        "srcDnsInfo.ipDomain": [int(ip_network(src_ip + '/27', strict=False)[0])],
        "srcDnsInfo.ip": [int(ip_network(src_ip + '/19', strict=False)[0])],
        "srcDnsInfo.domainName": ['domain' + src_ip],
        "srcDnsInfo.hostName": [src_host_name],
        "srcDnsInfo.source": ['TBD'],
        "dstDnsInfo.ipDomain": [int(ip_network(dst_ip + '/27', strict=False)[0])],
        "dstDnsInfo.ip": [int(ip_network(dst_ip + '/19', strict=False)[0])],
        "dstDnsInfo.domainName": ['domain' + dst_ip],
        "dstDnsInfo.hostName": [dst_host_name],
        "dstDnsInfo.source": ['TBD'],
        "reporterEntity.collectorId": [int(time.time()) // 8],
        "reporterEntity_reporter.name": ['reporter' + str(int(time.time()))],
        "reporterEntity_reporter.modelkey_otype": [random.choice([7, 8, 603, 612, 663, 917, 5200])],
        "reporterEntity_reporter.modelkey_oid": [int(time.time())],
        "SchemaVersion": random.randint(1, 9),
        "lastActivity": int(time.time() // 1),
        "activity": int(time.time() // 2),
        "srck8Info.k8scollectorId": [int(time.time()) // 8],
        "srck8Info_k8sservice.name": ['service' + str(src_k8s_service_num)],
        "srck8Info_k8sservice.modelkey_otype": [1504],
        "srck8Info_k8sservice.modelkey_oid": [src_k8s_service_num],
        "srck8Info_k8scluster.name": ['cluster' + str(src_k8s_cluster_num)],
        "srck8Info_k8scluster.modelkey_otype": [1501],
        "srck8Info_k8scluster.modelkey_oid": [src_k8s_cluster_num],
        "srck8Info_k8snamespace.name": ['namespace' + str(src_k8s_namespace)],
        "srck8Info_k8snamespace.modelkey_otype": [503],
        "srck8Info_k8snamespace.modelkey_oid": [src_k8s_namespace],
        "srck8Info_k8snode.name": ['node' + str(src_k8s_node)],
        "srck8Info_k8snode.modelkey_otype": [1502],
        "srck8Info_k8snode.modelkey_oid": [src_k8s_node],
        "dstk8Info.k8scollectorId": [int(time.time()) // 8],
        "dstk8Info_k8sservice.name": ['service' + str(dst_k8s_service_num)],
        "dstk8Info_k8sservice.modelkey_otype": [1504],
        "dstk8Info_k8sservice.modelkey_oid": [dst_k8s_service_num],
        "dstk8Info_k8scluster.name": ['cluster' + str(dst_k8s_cluster_num)],
        "dstk8Info_k8scluster.modelkey_otype": [1501],
        "dstk8Info_k8scluster.modelkey_oid": [dst_k8s_cluster_num],
        "dstk8Info_k8snamespace.name": ['namespace' + str(dst_k8s_namespace)],
        "dstk8Info_k8snamespace.modelkey_otype": [503],
        "dstk8Info_k8snamespace.modelkey_oid": [dst_k8s_namespace],
        "dstk8Info_k8snode.name": ['node' + str(dst_k8s_node)],
        "dstk8Info_k8snode.modelkey_otype": [1502],
        "dstk8Info_k8snode.modelkey_oid": [dst_k8s_node],
        "lbflowtype": flowtype,
        "loadBalancerInfo.type": [flowtype],
        "loadBalancerInfo.collectorId": [int(time.time()) // 8],
        "loadBalancerInfo.relevantPort": [random.choice([443, 53, 80, 135, 2055, 412, 76, 3001, 2099, 11029, 1998, 1995, 2019])],
        "loadBalancerInfo_loadbalancervIP.prefixLength": [27],
        "loadBalancerInfo_loadbalancervIP.ipAddress": [src_ip],
        "loadBalancerInfo_loadbalancervIP.netMask": [src_netmask],
        "loadBalancerInfo_loadbalancervIP.networkAddress": [src_network],
        "loadBalancerInfo_loadbalancervIP.cidr": [src_cidr],
        "loadBalancerInfo_loadbalancervIP.fstart": [start_src_ip_int],
        "loadBalancerInfo_loadbalancervIP.fend": [end_src_ip_int],
        "loadBalancerInfo_loadbalancervIP.ipaddresstype": ['SUBNET'],
        "loadBalancerInfo_loadbalancervIP.privateaddress": [1],
        "loadBalancerInfo_loadbalancervIP.Source": ['TBD'],
        "loadBalancerInfo_loadbalancervIP.Ipmetadata_domain": ['TBD'],
        "loadBalancerInfo_loadbalancervIP.Ipmetadata_isp": ['TBD'],
        "loadBalancerInfo_loadbalancerinternalIP.prefixLength": [27],
        "loadBalancerInfo_loadbalancerinternalIP.ipAddress": [dst_ip],
        "loadBalancerInfo_loadbalancerinternalIP.netMask": [dst_netmask],
        "loadBalancerInfo_loadbalancerinternalIP.networkAddress": [dst_network],
        "loadBalancerInfo_loadbalancerinternalIP.cidr": [dst_cidr],
        "loadBalancerInfo_loadbalancerinternalIP.fstart": [start_dst_ip_int],
        "loadBalancerInfo_loadbalancerinternalIP.fend": [end_dst_ip_int],
        "loadBalancerInfo_loadbalancerinternalIP.ipaddresstype": ['SUBNET'],
        "loadBalancerInfo_loadbalancerinternalIP.privateaddress": [1],
        "loadBalancerInfo_loadbalancerinternalIP.Source": ['TBD'],
        "loadBalancerInfo_loadbalancerinternalIP.Ipmetadata_domain": ['TBD'],
        "loadBalancerInfo_loadbalancerinternalIP.Ipmetadata_isp": ['TBD'],
        "srcIpEntity.name": [src_ip],
        "srcIpEntity.modelkey_otype": [541],
        "srcIpEntity.modelkey_oid": [int(time.time()) // 6],
        "dstIpEntity.name": [dst_ip],
        "dstIpEntity.modelkey_otype": [541],
        "dstIpEntity.modelkey_oid": [int(time.time()) // 5],
        "srcNic.name": ['VNIC' + str(src_VM_num)],
        "srcNic.modelkey_otype": [random.choice([18, 17, 16])],
        "srcNic.modelkey_oid": [src_VM_num],
        "dstNic.name": ['VNIC' + str(dst_VM_num)],
        "dstNic.modelkey_otype": [random.choice([18, 17, 16])],
        "dstNic.modelkey_oid": [dst_VM_num],
        "srcVm.name": [src_VM_name],
        "srcVm.modelkey_otype": [1601],
        "srcVm.modelkey_oid": [src_VM_num],
        "dstVm.name": [dst_VM_name],
        "dstVm.modelkey_otype": [1601],
        "dstVm.modelkey_oid": [dst_VM_num],
        "srcSg.name": ['SG' + str(src_sg_num)],
        "srcSg.modelkey_otype": [random.choice([550, 213, 602, 958])],
        "srcSg.modelkey_oid": [src_sg_num],
        "dstSg.name": ['SG' + str(dst_sg_num)],
        "dstSg.modelkey_otype": [random.choice([550, 213, 602, 958])],
        "dstSg.modelkey_oid": [dst_sg_num],
        "srcIpSet.name": ['IPSET' + str(src_VM_num // 32)],
        "srcIpSet.modelkey_otype": [random.choice([84, 214])],
        "srcIpSet.modelkey_oid": [src_VM_num // 32],
        "dstIpSet.name": ['IPSET' + str(dst_VM_num)],
        "dstIpSet.modelkey_otype": [random.choice([84, 214])],
        "dstIpSet.modelkey_oid": [dst_VM_num // 32],
        "srcSt.name": ['securitytag' + str(src_sg_num)],
        "srcSt.modelkey_otype": [99],
        "srcSt.modelkey_oid": [src_sg_num],
        "dstSt.name": ['securitytag' + str(dst_sg_num)],
        "dstSt.modelkey_otype": [99],
        "dstSt.modelkey_oid": [dst_sg_num],
        "srcL2Net.name": ['Vlan' + str(src_VM_num // 32)],
        "srcL2Net.modelkey_otype": [random.choice([11, 12, 13, 950])],
        "srcL2Net.modelkey_oid": [src_VM_num // 32],
        "dstL2Net.name": ['Vlan' + str(dst_VM_num // 32)],
        "dstL2Net.modelkey_otype": [random.choice([11, 12, 13, 950])],
        "dstL2Net.modelkey_oid": [dst_VM_num // 32],
        "srcGroup.name": ['GROUP' + str(src_VM_num // 100)],
        "srcGroup.modelkey_otype": [81],
        "srcGroup.modelkey_oid": [src_VM_num // 100],
        "dstGroup.name": ['GROUP' + str(dst_VM_num // 100)],
        "dstGroup.modelkey_otype": [81],
        "dstGroup.modelkey_oid": [dst_VM_num // 100],
        "srcCluster.name": [src_cluster_name],
        "srcCluster.modelkey_otype": [66],
        "srcCluster.modelkey_oid": [src_cluster_num],
        "dstCluster.name": [dst_cluster_name],
        "dstCluster.modelkey_otype": [66],
        "dstCluster.modelkey_oid": [dst_cluster_num],
        "srcRp.name": ['RP' + str(src_rp_num)],
        "srcRp.modelkey_otype": [79],
        "srcRp.modelkey_oid": [src_rp_num],
        "dstRp.name": ['RP' + str(dst_rp_num)],
        "dstRp.modelkey_otype": [79],
        "dstRp.modelkey_oid": [dst_rp_num],
        "srcDc.name": [DC_name],
        "srcDc.modelkey_otype": [105],
        "srcDc.modelkey_oid": [1],
        "dstDc.name": [DC_name],
        "dstDc.modelkey_otype": [105],
        "dstDc.modelkey_oid": [1],
        "srcHost.name": [src_host_name],
        "srcHost.modelkey_otype": [4],
        "srcHost.modelkey_oid": [src_host_num],
        "dstHost.name": [dst_host_name],
        "dstHost.modelkey_otype": [4],
        "dstHost.modelkey_oid": [dst_host_num],
        "svcEP.name": [dst_ip + port_name_num],
        "svcEP.modelkey_otype": [605],
        "svcEP.modelkey_oid": [int(time.time()) // 6],
        "srcManagers.name": [src_Nsx_manager_name],
        "srcManagers.modelkey_otype": [random.choice([7, 8, 612])],
        "srcManagers.modelkey_oid": [src_Nsx_vc_num],
        "dstManagers.name": [dst_Nsx_manager_name],
        "dstManagers.modelkey_otype": [random.choice([7, 8, 612])],
        "dstManagers.modelkey_oid": [dst_Nsx_vc_num],
        "flowDomain.name": ['GLOBAL'],
        "flowDomain.modelkey_otype": [random.choice([197, 664, 658])],
        "flowDomain.modelkey_oid": [int(time.time()) // 8],
        "srcLookupDomain.name": ['GLOBAL'],
        "srcLookupDomain.modelkey_otype": [random.choice([197, 664, 658])],
        "srcLookupDomain.modelkey_oid": [int(time.time()) // 8],
        "dstLookupDomain.name": ['GLOBAL'],
        "dstLookupDomain.modelkey_otype": [random.choice([197, 664, 658])],
        "dstLookupDomain.modelkey_oid": [int(time.time()) // 8],
        "srcVpc.name": ['AWS-VPC' + str(src_Nsx_vc_num)],
        "srcVpc.modelkey_otype": [603],
        "srcVpc.modelkey_oid": [src_Nsx_vc_num],
        "dstVpc.name": ['AWS-VPC' + str(dst_Nsx_vc_num)],
        "dstVpc.modelkey_otype": [603],
        "dstVpc.modelkey_oid": [dst_Nsx_vc_num],
        "srcTransportNode.name": ['TN' + str(src_Nsx_vc_num)],
        "srcTransportNode.modelkey_otype": [843],
        "srcTransportNode.modelkey_oid": [src_Nsx_vc_num],
        "dstTransportNode.name": ['TN' + str(dst_Nsx_vc_num)],
        "dstTransportNode.modelkey_otype": [843],
        "dstTransportNode.modelkey_oid": [dst_Nsx_vc_num],
        "srcDvpg.name": ['DVPG' + str(src_VM_num // 4)],
        "srcDvpg.modelkey_otype": [3],
        "srcDvpg.modelkey_oid": [src_VM_num // 4],
        "dstDvpg.name": ['DVPG' + str(dst_VM_num // 4)],
        "dstDvpg.modelkey_otype": [3],
        "dstDvpg.modelkey_oid": [dst_VM_num // 4],
        "srcDvs.name": ['DVS' + str(src_VM_num // 120)],
        "srcDvs.modelkey_otype": [2],
        "srcDvs.modelkey_oid": [src_VM_num // 120],
        "dstDvs.name": ['DVS' + str(dst_VM_num // 120)],
        "dstDvs.modelkey_otype": [2],
        "dstDvs.modelkey_oid": [dst_VM_num // 120],
        "metricData.totalBytes" : [totalBytes],
        "metricData.srcBytes": [srcBytes],
        "metricData.dstBytes": [dstBytes],
        "metricData.totalPackets": [totalPackets],
        "metricData.allowedSessionCount": [sessionCount],
        "metricData.nsxTcpRtt_abs_max_ms": [rttMax],
        "metricData.nsxTcpRtt_abs_avg_ms": [rttAvg]
    }

    return return_value


def generate_random_events(batchsize,mins):
    return [generate_random_event(mins) for _ in range(batchsize)]


csv_columns = ['name' ,'time', 'modelkey_cid' , 'modelkey_otype' , 'modelkey_oid' , 'port.fstart' , 'port.fend' , 'port.display' , 'port.ianaName' , 'port.ianaPortDisplay' , 'fProtocol' , 'srcIP.prefixLength' , 'srcIP.ipAddress' , 'srcIP.netMask' , 'srcIP.networkAddress' , 'srcIP.cidr' , 'srcIP.fstart' , 'srcIP.fend' , 'srcIP.ipaddresstype' , 'srcIP.privateaddress' , 'srcIP.Source' , 'srcIP.Ipmetadata_domain' , 'srcIP.Ipmetadata_isp' , 'dstIP.prefixLength' , 'dstIP.ipAddress' , 'dstIP.netMask' , 'dstIP.networkAddress' , 'dstIP.cidr' , 'dstIP.fstart' , 'dstIP.fend' , 'dstIP.ipaddresstype' , 'dstIP.privateaddress' , 'dstIP.Source' , 'dstIP.Ipmetadata_domain' , 'dstIP.Ipmetadata_isp' , 'TrfficType' , 'shared' , 'networkLayer' , 'srcsubnet.prefixLength' , 'srcsubnet.ipAddress' , 'srcsubnet.netMask' , 'srcsubnet.networkAddress' , 'srcsubnet.cidr' , 'srcsubnet.fstart' , 'srcsubnet.fend' , 'srcsubnet.ipaddresstype' , 'srcsubnet.privateaddress' , 'srcsubnet.Source' , 'srcsubnet.Ipmetadata_domain' , 'srcsubnet.Ipmetadata_isp' , 'dstsubnet.prefixLength' , 'dstsubnet.ipAddress' , 'dstsubnet.netMask' , 'dstsubnet.networkAddress' , 'dstsubnet.cidr' , 'dstsubnet.fstart' , 'dstsubnet.fend' , 'dstsubnet.ipaddresstype' , 'dstsubnet.privateaddress' , 'dstsubnet.Source' , 'dstsubnet.Ipmetadata_domain' , 'dstsubnet.Ipmetadata_isp' , 'withinhost' , 'typetag' , '__searchTags' , '__related_entities' , 'srcVmTags' , 'dstVmTags' , 'attribute.reportedaction' , 'attribute.reportedRuleId' , 'attribute.collectorId' , 'attribute_rule.name' , 'attribute_rule.modelkey_otype' , 'attribute_rule.modelkey_oid' , 'attribute_firewallmanager.name' , 'attribute_firewallmanager.modelkey_otype' , 'attribute_firewallmanager.modelkey_oid' , 'activedpIds' , 'typeTagsPacked' , 'protectionStatus' , 'flowAction' , 'srcDnsInfo.ipDomain' , 'srcDnsInfo.ip' , 'srcDnsInfo.domainName' , 'srcDnsInfo.hostName' , 'srcDnsInfo.source' , 'dstDnsInfo.ipDomain' , 'dstDnsInfo.ip' , 'dstDnsInfo.domainName' , 'dstDnsInfo.hostName' , 'dstDnsInfo.source' , 'reporterEntity.collectorId' , 'reporterEntity_reporter.name' , 'reporterEntity_reporter.modelkey_otype' , 'reporterEntity_reporter.modelkey_oid' , 'SchemaVersion' , 'lastActivity' , 'activity' , 'srck8Info.k8scollectorId' , 'srck8Info_k8sservice.name' , 'srck8Info_k8sservice.modelkey_otype' , 'srck8Info_k8sservice.modelkey_oid' , 'srck8Info_k8scluster.name' , 'srck8Info_k8scluster.modelkey_otype' , 'srck8Info_k8scluster.modelkey_oid' , 'srck8Info_k8snamespace.name' , 'srck8Info_k8snamespace.modelkey_otype' , 'srck8Info_k8snamespace.modelkey_oid' , 'srck8Info_k8snode.name' , 'srck8Info_k8snode.modelkey_otype' , 'srck8Info_k8snode.modelkey_oid' , 'dstk8Info.k8scollectorId' , 'dstk8Info_k8sservice.name' , 'dstk8Info_k8sservice.modelkey_otype' , 'dstk8Info_k8sservice.modelkey_oid' , 'dstk8Info_k8scluster.name' , 'dstk8Info_k8scluster.modelkey_otype' , 'dstk8Info_k8scluster.modelkey_oid' , 'dstk8Info_k8snamespace.name' , 'dstk8Info_k8snamespace.modelkey_otype' , 'dstk8Info_k8snamespace.modelkey_oid' , 'dstk8Info_k8snode.name' , 'dstk8Info_k8snode.modelkey_otype' , 'dstk8Info_k8snode.modelkey_oid' , 'lbflowtype' , 'loadBalancerInfo.type' , 'loadBalancerInfo.collectorId' , 'loadBalancerInfo.relevantPort' , 'loadBalancerInfo_loadbalancervIP.prefixLength' , 'loadBalancerInfo_loadbalancervIP.ipAddress' , 'loadBalancerInfo_loadbalancervIP.netMask' , 'loadBalancerInfo_loadbalancervIP.networkAddress' , 'loadBalancerInfo_loadbalancervIP.cidr' , 'loadBalancerInfo_loadbalancervIP.fstart' , 'loadBalancerInfo_loadbalancervIP.fend' , 'loadBalancerInfo_loadbalancervIP.ipaddresstype' , 'loadBalancerInfo_loadbalancervIP.privateaddress' , 'loadBalancerInfo_loadbalancervIP.Source' , 'loadBalancerInfo_loadbalancervIP.Ipmetadata_domain' , 'loadBalancerInfo_loadbalancervIP.Ipmetadata_isp' , 'loadBalancerInfo_loadbalancerinternalIP.prefixLength' , 'loadBalancerInfo_loadbalancerinternalIP.ipAddress' , 'loadBalancerInfo_loadbalancerinternalIP.netMask' , 'loadBalancerInfo_loadbalancerinternalIP.networkAddress' , 'loadBalancerInfo_loadbalancerinternalIP.cidr' , 'loadBalancerInfo_loadbalancerinternalIP.fstart' , 'loadBalancerInfo_loadbalancerinternalIP.fend' , 'loadBalancerInfo_loadbalancerinternalIP.ipaddresstype' , 'loadBalancerInfo_loadbalancerinternalIP.privateaddress' , 'loadBalancerInfo_loadbalancerinternalIP.Source' , 'loadBalancerInfo_loadbalancerinternalIP.Ipmetadata_domain' , 'loadBalancerInfo_loadbalancerinternalIP.Ipmetadata_isp' , 'srcIpEntity.name' , 'srcIpEntity.modelkey_otype' , 'srcIpEntity.modelkey_oid' , 'dstIpEntity.name' , 'dstIpEntity.modelkey_otype' , 'dstIpEntity.modelkey_oid' , 'srcNic.name' , 'srcNic.modelkey_otype' , 'srcNic.modelkey_oid' , 'dstNic.name' , 'dstNic.modelkey_otype' , 'dstNic.modelkey_oid' , 'srcVm.name' , 'srcVm.modelkey_otype' , 'srcVm.modelkey_oid' , 'dstVm.name' , 'dstVm.modelkey_otype' , 'dstVm.modelkey_oid' , 'srcSg.name' , 'srcSg.modelkey_otype' , 'srcSg.modelkey_oid' , 'dstSg.name' , 'dstSg.modelkey_otype' , 'dstSg.modelkey_oid' , 'srcIpSet.name' , 'srcIpSet.modelkey_otype' , 'srcIpSet.modelkey_oid' , 'dstIpSet.name' , 'dstIpSet.modelkey_otype' , 'dstIpSet.modelkey_oid' , 'srcSt.name' , 'srcSt.modelkey_otype' , 'srcSt.modelkey_oid' , 'dstSt.name' , 'dstSt.modelkey_otype' , 'dstSt.modelkey_oid' , 'srcL2Net.name' , 'srcL2Net.modelkey_otype' , 'srcL2Net.modelkey_oid' , 'dstL2Net.name' , 'dstL2Net.modelkey_otype' , 'dstL2Net.modelkey_oid' , 'srcGroup.name' , 'srcGroup.modelkey_otype' , 'srcGroup.modelkey_oid' , 'dstGroup.name' , 'dstGroup.modelkey_otype' , 'dstGroup.modelkey_oid' , 'srcCluster.name' , 'srcCluster.modelkey_otype' , 'srcCluster.modelkey_oid' , 'dstCluster.name' , 'dstCluster.modelkey_otype' , 'dstCluster.modelkey_oid' , 'srcRp.name' , 'srcRp.modelkey_otype' , 'srcRp.modelkey_oid' , 'dstRp.name' , 'dstRp.modelkey_otype' , 'dstRp.modelkey_oid' , 'srcDc.name' , 'srcDc.modelkey_otype' , 'srcDc.modelkey_oid' , 'dstDc.name' , 'dstDc.modelkey_otype' , 'dstDc.modelkey_oid' , 'srcHost.name' , 'srcHost.modelkey_otype' , 'srcHost.modelkey_oid' , 'dstHost.name' , 'dstHost.modelkey_otype' , 'dstHost.modelkey_oid' , 'svcEP.name' , 'svcEP.modelkey_otype' , 'svcEP.modelkey_oid' , 'srcManagers.name' , 'srcManagers.modelkey_otype' , 'srcManagers.modelkey_oid' , 'dstManagers.name' , 'dstManagers.modelkey_otype' , 'dstManagers.modelkey_oid' ,'flowDomain.name', 'flowDomain.modelkey_otype', 'flowDomain.modelkey_oid', 'srcLookupDomain.name' , 'srcLookupDomain.modelkey_otype' , 'srcLookupDomain.modelkey_oid' , 'dstLookupDomain.name' , 'dstLookupDomain.modelkey_otype' , 'dstLookupDomain.modelkey_oid' , 'srcVpc.name' , 'srcVpc.modelkey_otype' , 'srcVpc.modelkey_oid' , 'dstVpc.name' , 'dstVpc.modelkey_otype' , 'dstVpc.modelkey_oid' , 'srcTransportNode.name' , 'srcTransportNode.modelkey_otype' , 'srcTransportNode.modelkey_oid' , 'dstTransportNode.name' , 'dstTransportNode.modelkey_otype' , 'dstTransportNode.modelkey_oid' , 'srcDvpg.name' , 'srcDvpg.modelkey_otype' , 'srcDvpg.modelkey_oid' , 'dstDvpg.name' , 'dstDvpg.modelkey_otype' , 'dstDvpg.modelkey_oid' , 'srcDvs.name' , 'srcDvs.modelkey_otype' , 'srcDvs.modelkey_oid' , 'dstDvs.name' , 'dstDvs.modelkey_otype' , 'dstDvs.modelkey_oid','metricData.totalBytes','metricData.srcBytes', 'metricData.dstBytes','metricData.totalPackets', 'metricData.allowedSessionCount','metricData.nsxTcpRtt_abs_max_ms', 'metricData.nsxTcpRtt_abs_avg_ms']
csv_file = f"f{inserter_config.BULK_SIZE*10}Datapartbydate{time.time()}.csv"
async def write_to_event(data):
    global total_inserted_events
    try:
        with open(csv_file, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            for rowdata in data:
                writer.writerow(rowdata)
    except IOError:
        print("I/O error")
    total_inserted_events += len(data)
    print(f"writing to {inserter_config.TABLE_NAME} {len(data)} rows; total count: {total_inserted_events}")


async def fill_events(_loop):
    async with asyncpool.AsyncPool(
            _loop,
            num_workers=inserter_config.WORKERS,
            worker_co=write_to_event,
            max_task_time=300000,
            log_every_n=10,
            name="badri",
            logger=logging.getLogger("badri")) as p:
        for j in range(14):
            minutes = j
            for i in range(1):
                data = generate_random_events(inserter_config.BULK_SIZE,minutes)
                await p.push(data)


def log_experiment(_took,csv_file):
    with open("csv_creater_log.txt", 'a') as f:
        text = f"{time.ctime(time.time())} - " \
            f"csvFileName: {csv_file} - " \
            f"inserted: {total_inserted_events} - " \
            f"workers:{inserter_config.WORKERS}-"\
            f"took: {round(_took, 2)} \n"
        f.write(text)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    start = time.time()
    print("inserter started at", time.ctime(start))
    loop.run_until_complete(fill_events(loop))
    end = time.time()
    took = end - start
    log_experiment(took,csv_file)
    print(f"inserter ended at {time.ctime(end)}; took: {took} seconds")