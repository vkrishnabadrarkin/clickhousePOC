import csv
import pandas
from ipaddress import ip_address, ip_network, ip_interface
# import ast
#
# badr = "[(80,'https','TCP'),(443,'https','TCP'),(123,'ntp','UDP'),(22,'ssh','TCP'),(53,'dns','UDP'),(445,'microsoft-ds','UDP'),(389,'ldap','UDP'),(514,'syslog','TCP'),(137,'netbios-ns','TCP'),(902,'ideafarm-door','TCP')]"
#
# badr = ast.literal_eval(badr)
# print(badr[1][1])
k = enumerate(['ipAddress', 'vm_name', 'vm_otype', 'vm_oid', 'subnet_ip', 'subnet_netmask', 'subnet_prefixLength', 'subnet_networkAddress', 'subnet_cidr', 'subnet_start', 'subnet_end', 'ipAddressType', 'privateAddress', 'source', 'Ipmetadata_domain', 'ipmetadata_isp', 'host_name', 'host_otype', 'host_oid', 'dnsinfo_ipdomain', 'dnsinfo_ip', 'dnsinfo_domainname', 'dnsinfo_hostname', 'dnsinfo_source', 'k8s_service_name', 'k8s_service_otype', 'k8s_service_oid', 'k8s_cluster_name', 'k8s_cluster_otype', 'k8s_cluster_oid', 'k8s_namespace_name', 'k8s_namespace_otype', 'k8s_namespace_oid', 'k8s_node_name', 'k8s_node_otype', 'k8s_node_oid', 'IP_entity_name', 'IP_entity_otype', 'IP_entity_oid', 'Nic_name', 'Nic_otype', 'Nic_oid', 'sg_name', 'sg_otype', 'sg_oid', 'IP_set_name', 'IP_set_otype', 'IP_set_oid', 'STag_name', 'STag_otype', 'STag_oid', 'L2net_name', 'L2net_otype', 'L2net_oid', 'Grp_name', 'Grp_otype', 'Grp_oid', 'cluster_name', 'cluster_otype', 'cluster_oid', 'RP_name', 'RP_otype', 'RP_oid', 'DC_name', 'DC_otype', 'DC_oid', 'managerNSX_name', 'managerNSX_otype', 'managerNSX_oid', 'lookupDomain_name', 'lookupDomain_otype', 'lookupDomain_oid', 'vpc_name', 'vpc_otype', 'vpc_oid', 'transportNode_name', 'transportNode_otype', 'transportNode_oid', 'Dvpg_name', 'Dvpg_otype', 'Dvpg_oid', 'Dvs_name', 'Dvs_otype', 'Dvs_oid'])
print(list(k))