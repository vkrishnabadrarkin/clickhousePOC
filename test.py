import asyncio
import datetime
import logging
import random
import sys
import time

from random import getrandbits
from ipaddress import IPv4Network, IPv4Address,ip_address,ip_network,ip_interface



import inserter_config
from utils import format_date_from_timestamp

total_inserted_events = 1000000
listofip = []
for k in ip_network("10.0.0.0/19"):
    listofip.append(str(k))

def gen_ip(p):
    return listofip[p]

def generate_random_event() -> dict:
    f_protocol = random.choice(['TCP','UDP'])
    traffic_type = random.choice(['EAST_WEST_TRAFFIC', 'INTERNET_TRAFFIC'])
    port_num = random.choice([443,53,80,135,2055,412,76,3001,2099,11029,1998,1995,2019])
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
    port_name_num = '[' + str(port_num)+ ']'+ port_name 
    
    VM_range = list(range(0,8191))
    src_VM_num = random.choice(VM_range)
    src_VM_name = 'VM' + str(src_VM_num)
    src_host_num = src_VM_num//16
    src_host_name = 'HOST' + str(src_host_num)
    src_rp_num = src_VM_num//8
    src_sg_num = src_VM_num//6
    src_cluster_num = src_host_num//8
    src_cluster_name = 'CLUSTER' + str(src_cluster_num)
    src_Nsx_vc_num = src_cluster_num//16
    src_Nsx_manager_name = 'NSX' + str(src_Nsx_vc_num)
    src_VC_name = 'VC' + str(src_Nsx_vc_num)
    DC_name = 'DATACENTER101'
    VM_range.remove(src_VM_num)
    dst_VM_num = random.choice(VM_range)
    dst_VM_name = 'VM' + str(dst_VM_num)
    dst_host_num = dst_VM_num//16
    dst_host_name = 'HOST' + str(dst_host_num)
    dst_rp_num = dst_VM_num//8
    dst_sg_num = dst_VM_num//6
    dst_cluster_num = dst_host_num//8
    dst_cluster_name = 'CLUSTER' + str(dst_cluster_num)
    dst_Nsx_vc_num = dst_cluster_num//16
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

    flow_name = src_ip + 'VM' + str(src_VM_num) + dst_ip
    flow_tag_list = ['TAG_TRAFFIC_TYPE_UNKNOWN' , 'TAG_INTERNET_TRAFFIC' ,'TAG_EAST_WEST_TRAFFIC' , 'TAG_VM_VM_TRAFFIC', 'TAG_VM_PHY_TRAFFIC' , 'TAG_PHY_PHY_TRAFFIC' , 'TAG_SRC_IP_VMKNIC' ,'TAG_DST_IP_VMKNIC' , 'TAG_SRC_IP_ROUTER_INT' , 'TAG_DST_IP_ROUTER_INT', 'TAG_SRC_IP_VM','TAG_DST_IP_VM', 'TAG_SRC_IP_INTERNET','TAG_DST_IP_INTERNET', 'TAG_SRC_IP_PHYSICAL', 'TAG_DST_IP_PHYSICAL', 'TAG_SAME_HOST' , 'TAG_DIFF_HOST' , 'TAG_COMMON_HOST_INFO_UNKNOWN' , 'TAG_SHARED_SERVICE' , 'TAG_NOT_SHARED_SERVICE' , 'TAG_NETWORK_SWITCHED' , 'TAG_NETWORK_ROUTED' , 'TAG_NETWORK_UNKNOWN' , 'TAG_SRC_IP_VTEP' , 'TAG_DST_IP_VTEP' , 'TAG_UNICAST' , 'TAG_BROADCAST' , 'TAG_MULTICAST' , 'TAG_SRC_IP_LINK_LOCAL' , 'TAG_DST_IP_LINK_LOCAL' , 'TAG_SRC_IP_CLASS_E' , 'TAG_DST_IP_CLASS_E' , 'TAG_SRC_IP_CLASS_A_RESERVED' , 'TAG_DST_IP_CLASS_A_RESERVED' , 'TAG_INVALID_IP_PACKETS' , 'TAG_NOT_ANALYZED' , 'TAG_GENERIC_INTERNET_SRC_IP' , 'TAG_SNAT_DNAT_FLOW' , 'TAG_NATTED' , 'TAG_MULTINICS' , 'TAG_MULTI_NATRULE' , 'TAG_SRC_VC' , 'TAG_DST_VC' , 'TAG_SRC_AWS' , 'TAG_DST_AWS' , 'TAG_WITHIN_DC' , 'TAG_DIFF_DC' , 'TAG_SRC_IP_IN_SNAT_RULE_TARGET' , 'TAG_DST_IP_IN_DNAT_RULE_ORIGINAL' , 'TAG_SRC_IP_MULTI_NAT_RULE' , 'TAG_DNAT_IP_MULTI_NAT_RULE' , 'DEPRECATED_TAG_DST_IP_IN_SNAT_RULE_TARGET' , 'DEPRECATED_TAG_SRC_IP_IN_DNAT_RULE_ORIGINAL' , 'TAG_INVALID_IP_DOMAIN' , 'TAG_WITHIN_VPC' , 'TAG_DIFF_VPC' , 'TAG_SRC_IP_IN_MULTIPLE_SUBNETS' , 'TAG_DST_IP_IN_MULTIPLE_SUBNETS' , 'TAG_SFLOW' , 'TAG_PRE_NAT_FLOW' , 'TAG_POST_NAT_FLOW' , 'TAG_LOGICAL_FLOW' , 'TAG_SRC_K8S_POD' , 'TAG_DST_K8S_POD' , 'TAG_POD_POD_TRAFFIC' , 'TAG_VM_POD_TRAFFIC' , 'TAG_POD_PHYSICAL_TRAFFIC']
    new_list = random.sample(flow_tag_list,5)
    reported_action = random.choice(['ALLOW' , 'DENY' , 'DROP', 'REJECT' , 'REDIRECT' , 'DONT_REDIRECT'])
    rule_num = random.randint(1,8888)
    ruleid = 'RULE'+str(rule_num)
    src_k8s_service_num = src_VM_num//20
    src_k8s_cluster_num = src_VM_num//10
    src_k8s_namespace = src_VM_num//25
    src_k8s_node = src_VM_num//10
    dst_k8s_service_num = dst_VM_num//20
    dst_k8s_cluster_num = dst_VM_num//10
    dst_k8s_namespace = dst_VM_num//25
    dst_k8s_node = dst_VM_num//10
    flowtype = random.choice(['PRE_NAT','POST_NAT','LOGICAL'])


    return_value = {
        "name": flow_name,
        "modelkey_cid" : 12345,
        "modelkey_otype": 515,
        "modelkey_oid" : total_inserted_events,
        "port.fstart": [port_num],
        "port.fend": [port_num],
        "port.display": [port_num],
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
        "srcIP.Source": ['UNKNOWN'],
        "srcIP.Ipmetadata_domain": ['UNKNOWN'],
        "srcIP.Ipmetadata_isp": ['UNKNOWN'],
        "dstIP.prefixLength": [27],
        "dstIP.ipAddress": [dst_ip],
        "dstIP.netMask": [dst_netmask],
        "dstIP.networkAddress": [dst_network],
        "dstIP.cidr": [dst_cidr],
        "dstIP.fstart": [start_dst_ip_int],
        "dstIP.fend": [end_dst_ip_int],
        "dstIP.ipaddresstype": ['SUBNET'],
        "dstIP.privateaddress": [1],
        "dstIP.Source": ['UNKNOWN'],
        "dstIP.Ipmetadata_domain": ['UNKNOWN'],
        "dstIP.Ipmetadata_isp": ['UNKNOWN'],
        "TrfficType": traffic_type,
        "shared": [1],
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
        "srcsubnet.Source": ['UNKNOWN'],
        "srcsubnet.Ipmetadata_domain": ['UNKNOWM'],
        "srcsubnet.Ipmetadata_isp": ['UNKNOWM'],
        "dstsubnet.prefixLength": [19],
        "dstsubnet.ipAddress": [dst_ip + '/19'],
        "dstsubnet.netMask": [str(ip_interface(dst_ip + '/19').netmask)],
        "dstsubnet.networkAddress": [str(ip_interface(dst_ip + '/19').network)[:-4]],
        "dstsubnet.cidr": [str(ip_interface(dst_ip + '/19').network)],
        "dstsubnet.fstart": [int(ip_network(dst_ip + '/19', strict=False)[0])],
        "dstsubnet.fend": [int(ip_network(dst_ip + '/19', strict=False)[-1])],
        "dstsubnet.ipaddresstype": ['SUBNET'],
        "dstsubnet.privateaddress": [1],
        "dstsubnet.Source": ['UNKNOWN'],
        "dstsubnet.Ipmetadata_domain": ['UNKNOWM'],
        "dstsubnet.Ipmetadata_isp": ['UNKNOWM'],
        "withinhost": int(src_host_num == dst_host_num),
        "typetag": new_list,
        "__searchTags": [flow_name, src_VM_name, dst_VM_name],
        "__related_entities": ['flows','traffic'],
        "srcVmTags": ['admin@vmware.com','badri@vmware.com'],
        "dstVmTags": ['vamsi@vmware.com','krishna@vmware.com'],
        "attribute.reportedaction": [reported_action],
        "attribute.reportedRuleId": [ruleid],
        "attribute.collectorId": [total_inserted_events//8],
        "attribute_rule.name": ['AT_RULE' + str(total_inserted_events)],
        "attribute_rule.modelkey_otype" : [random.choice([7,8,603,612,663,917,5200])],
        "attribute_rule.modelkey_oid": [total_inserted_events],
        "attribute_firewallmanager.name": ['AT_firewall_manager' + str(total_inserted_events)],
        "attribute_firewallmanager.modelkey_otype" : [random.choice([7,8,612])],
        "attribute_firewallmanager.modelkey_oid": [total_inserted_events],
        "activedpIds": total_inserted_events//8,
        "typeTagsPacked": 'KCC0IABACBAA',
        "protectionStatus": random.choice(['UNKNOWN_STATUS', 'PROTECTED', 'ANY_ANY','UN_PROTECTED']),
        "flowAction": 'ALLOW',
        "srcDnsInfo.ipDomain": [int(ip_network(src_ip + '/27', strict=False)[0])],
        "srcDnsInfo.ip": [int(ip_network(src_ip + '/19', strict=False)[0])],
        "srcDnsInfo.domainName": ['domain'+ src_ip],
        "srcDnsInfo.hostName": [src_host_name],
        "srcDnsInfo.source": ['UNKNOWN'],
        "dstDnsInfo.ipDomain": [int(ip_network(dst_ip + '/27', strict=False)[0])],
        "dstDnsInfo.ip": [int(ip_network(dst_ip + '/19', strict=False)[0])],
        "dstDnsInfo.domainName": ['domain' + dst_ip],
        "dstDnsInfo.hostName": [dst_host_name],
        "dstDnsInfo.source": ['UNKNOWN'],
        "reporterEntity.collectorId": [total_inserted_events//8],
        "reporterEntity_reporter.name": ['reporter' + str(total_inserted_events)],
        "reporterEntity_reporter.modelkey_otype": [random.choice([7,8,603,612,663,917,5200])],
        "reporterEntity_reporter.modelkey_oid": [total_inserted_events],
        "SchemaVersion": random.randint(1,9),
        "lastActivity": time.time(),
        "activity": time.time()//2,
        "srck8Info.k8scollectorId": [total_inserted_events//8],
        "srck8Info_k8sservice.name": ['service'+str(src_k8s_service_num)],
        "srck8Info_k8sservice.modelkey_otype": [1504],
        "srck8Info_k8sservice.modelkey_oid": [src_k8s_service_num],
        "srck8Info_k8scluster.name": ['cluster'+str(src_k8s_cluster_num)],
        "srck8Info_k8scluster.modelkey_otype": [1501],
        "srck8Info_k8scluster.modelkey_oid": [src_k8s_cluster_num],
        "srck8Info_k8snamespace.name": ['namespace'+str(src_k8s_namespace)],
        "srck8Info_k8snamespace.modelkey_otype": [503],
        "srck8Info_k8snamespace.modelkey_oid": [src_k8s_namespace],
        "srck8Info_k8snode.name": ['node'+str(src_k8s_node)],
        "srck8Info_k8snode.modelkey_otype": [1502],
        "srck8Info_k8snode.modelkey_oid": [src_k8s_node],
        "dstk8Info.k8scollectorId": [total_inserted_events//8],
        "dstk8Info_k8sservice.name": ['service'+str(dst_k8s_service_num)],
        "dstk8Info_k8sservice.modelkey_otype": [1504],
        "dstk8Info_k8sservice.modelkey_oid": [dst_k8s_service_num],
        "dstk8Info_k8scluster.name": ['cluster'+str(dst_k8s_cluster_num)],
        "dstk8Info_k8scluster.modelkey_otype": [1501],
        "dstk8Info_k8scluster.modelkey_oid": [dst_k8s_cluster_num],
        "dstk8Info_k8snamespace.name": ['namespace'+str(dst_k8s_namespace)],
        "dstk8Info_k8snamespace.modelkey_otype": [503],
        "dstk8Info_k8snamespace.modelkey_oid": [dst_k8s_namespace],
        "dstk8Info_k8snode.name": ['node'+str(dst_k8s_node)], 
        "dstk8Info_k8snode.modelkey_otype": [1502],
        "dstk8Info_k8snode.modelkey_oid": [dst_k8s_node],
        "lbflowtype": flowtype,
        "loadBalancerInfo.type": [flowtype],
        "loadBalancerInfo.collectorId": [total_inserted_events//8],
        "loadBalancerInfo.relevantPort": [random.choice([443,53,80,135,2055,412,76,3001,2099,11029,1998,1995,2019])],
        "loadBalancerInfo_loadbalancervIP.prefixLength": [27],
        "loadBalancerInfo_loadbalancervIP.ipAddress": [src_ip],
        "loadBalancerInfo_loadbalancervIP.netMask": [src_netmask],
        "loadBalancerInfo_loadbalancervIP.networkAddress": [src_network],
        "loadBalancerInfo_loadbalancervIP.cidr": [src_cidr],
        "loadBalancerInfo_loadbalancervIP.fstart": [start_src_ip_int],
        "loadBalancerInfo_loadbalancervIP.fend": [end_src_ip_int],
        "loadBalancerInfo_loadbalancervIP.ipaddresstype": ['SUBNET'],
        "loadBalancerInfo_loadbalancervIP.privateaddress": [1],
        "loadBalancerInfo_loadbalancervIP.Source": ['UNKNOWN'],
        "loadBalancerInfo_loadbalancervIP.Ipmetadata_domain": ['UNKNOWN'],
        "loadBalancerInfo_loadbalancervIP.Ipmetadata_isp": ['UNKNOWN'],
        "loadBalancerInfo_loadbalancerinternalIP.prefixLength": [27],
        "loadBalancerInfo_loadbalancerinternalIP.ipAddress": [dst_ip],
        "loadBalancerInfo_loadbalancerinternalIP.netMask": [dst_netmask],
        "loadBalancerInfo_loadbalancerinternalIP.networkAddress": [dst_network],
        "loadBalancerInfo_loadbalancerinternalIP.cidr": [dst_cidr],
        "loadBalancerInfo_loadbalancerinternalIP.fstart": [start_dst_ip_int],
        "loadBalancerInfo_loadbalancerinternalIP.fend": [end_dst_ip_int],
        "loadBalancerInfo_loadbalancerinternalIP.ipaddresstype": ['SUBNET'],
        "loadBalancerInfo_loadbalancerinternalIP.privateaddress": [1],
        "loadBalancerInfo_loadbalancerinternalIP.Source": ['UNKNOWN'],
        "loadBalancerInfo_loadbalancerinternalIP.Ipmetadata_domain": ['UNKNOWN'],
        "loadBalancerInfo_loadbalancerinternalIP.Ipmetadata_isp": ['UNKNOWN'],
        "srcIpEntity.name": [src_ip],
        "srcIpEntity.modelkey_otype": [541],
        "srcIpEntity.modelkey_oid": [total_inserted_events//6],
        "dstIpEntity.name": [dst_ip],
        "dstIpEntity.modelkey_otype": [541],
        "dstIpEntity.modelkey_oid": [total_inserted_events//5],
        "srcNic.name": ['VNIC'+ str(src_VM_num)],
        "srcNic.modelkey_otype": [random.choice([18,17,16])],
        "srcNic.modelkey_oid": [src_VM_num],
        "dstNic.name": ['VNIC'+str(dst_VM_num)],
        "dstNic.modelkey_otype": [random.choice([18,17,16])],
        "dstNic.modelkey_oid": [dst_VM_num],
        "srcVm.name": [src_VM_name],
        "srcVm.modelkey_otype": [1601],
        "srcVm.modelkey_oid": [src_VM_num],
        "dstVm.name": [dst_VM_name],
        "dstVm.modelkey_otype": [1601],
        "dstVm.modelkey_oid": [dst_VM_num],
        "srcSg.name": ['SG'+str(src_sg_num)],
        "srcSg.modelkey_otype": [random.choice([550,213,602,958])],
        "srcSg.modelkey_oid": [src_sg_num],
        "dstSg.name": ['SG'+str(dst_sg_num)],
        "dstSg.modelkey_otype": [random.choice([550,213,602,958])],
        "dstSg.modelkey_oid": [dst_sg_num],
        "srcIpSet.name": ['IPSET'+str(src_VM_num//32)],
        "srcIpSet.modelkey_otype": [random.choice([84,214])],
        "srcIpSet.modelkey_oid": [src_VM_num//32],
        "dstIpSet.name": ['IPSET'+str(dst_VM_num)],
        "dstIpSet.modelkey_otype": [random.choice([84,214])],
        "dstIpSet.modelkey_oid": [dst_VM_num//32],
        "srcSt.name": ['securitytag'+str(src_sg_num)],
        "srcSt.modelkey_otype": [99],
        "srcSt.modelkey_oid": [src_sg_num],
        "dstSt.name": ['securitytag'+str(dst_sg_num)],
        "dstSt.modelkey_otype": [99],
        "dstSt.modelkey_oid": [dst_sg_num],
        "srcL2Net.name": ['Vlan'+str(src_VM_num//32)],
        "srcL2Net.modelkey_otype": [random.choice([11,12,13,950])],
        "srcL2Net.modelkey_oid": [src_VM_num//32],
        "dstL2Net.name": ['Vlan'+str(dst_VM_num//32)],
        "dstL2Net.modelkey_otype": [random.choice([11,12,13,950])],
        "dstL2Net.modelkey_oid": [dst_VM_num//32],
        "srcGroup.name": ['GROUP'+str(src_VM_num//100)],
        "srcGroup.modelkey_otype": [81],
        "srcGroup.modelkey_oid": [src_VM_num//100],
        "dstGroup.name": ['GROUP'+str(dst_VM_num//100)],
        "dstGroup.modelkey_otype": [81],
        "dstGroup.modelkey_oid": [dst_VM_num//100],
        "srcCluster.name": [src_cluster_name],
        "srcCluster.modelkey_otype": [66],
        "srcCluster.modelkey_oid": [src_cluster_num],
        "dstCluster.name": [dst_cluster_name],
        "dstCluster.modelkey_otype": [66],
        "dstCluster.modelkey_oid": [dst_cluster_num],
        "srcRp.name": ['RP'+str(src_rp_num)],
        "srcRp.modelkey_otype": [79],
        "srcRp.modelkey_oid":[src_rp_num],
        "dstRp.name": ['RP'+str(dst_rp_num)],
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
        "svcEP.modelkey_oid": [total_inserted_events//6],
        "srcManagers.name": [src_Nsx_manager_name],
        "srcManagers.modelkey_otype": [random.choice([7,8,612])],
        "srcManagers.modelkey_oid": [src_Nsx_vc_num],
        "dstManagers.name":[dst_Nsx_manager_name],
        "dstManagers.modelkey_otype": [random.choice([7,8,612])], 
        "dstManagers.modelkey_oid": [dst_Nsx_vc_num],
        "flowDomain.name": ['GLOBAL'],
        "flowDomain.modelkey_otype": [random.choice([197,664,658])],
        "flowDomain.modelkey_oid": [total_inserted_events//8],
        "srcLookupDomain.name": ['GLOBAL'],
        "srcLookupDomain.modelkey_otype": [random.choice([197,664,658])],
        "srcLookupDomain.modelkey_oid": [total_inserted_events//8],
        "dstLookupDomain.name": ['GLOBAL'],
        "dstLookupDomain.modelkey_otype": [random.choice([197,664,658])],
        "dstLookupDomain.modelkey_oid": [total_inserted_events//8],
        "srcVpc.name": ['AWS-VPC'+ str(src_Nsx_vc_num)],
        "srcVpc.modelkey_otype": [603],
        "srcVpc.modelkey_oid": [src_Nsx_vc_num],
        "dstVpc.name": ['AWS-VPC'+ str(dst_Nsx_vc_num)],
        "dstVpc.modelkey_otype": [603],
        "dstVpc.modelkey_oid": [dst_Nsx_vc_num],
        "srcTransportNode.name": ['TN'+str(src_Nsx_vc_num)],
        "srcTransportNode.modelkey_otype" : [843],
        "srcTransportNode.modelkey_oid": [src_Nsx_vc_num],
        "dstTransportNode.name": ['TN' + str(dst_Nsx_manager_name)],
        "dstTransportNode.modelkey_otype": [843],
        "dstTransportNode.modelkey_oid": [dst_Nsx_manager_name],
        "srcDvpg.name": ['DVPG'+ str(src_VM_num//4)],
        "srcDvpg.modelkey_otype": [3],
        "srcDvpg.modelkey_oid": [src_VM_num//4],
        "dstDvpg.name": ['DVPG'+ str(dst_VM_num//4)],
        "dstDvpg.modelkey_otype": [3],
        "dstDvpg.modelkey_oid": [dst_VM_num//4],
        "srcDvs.name": ['DVS'+ str(src_VM_num//120)],
        "srcDvs.modelkey_otype": [2],
        "srcDvs.modelkey_oid": [src_VM_num//120],
        "dstDvs.name": ['DVS'+ str(dst_VM_num//120)],
        "dstDvs.modelkey_otype": [2],
        "dstDvs.modelkey_oid": [dst_VM_num//120]
    }

    return return_value
    print('hi')
    print(generate_random_event())