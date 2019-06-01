import csv
from ipaddress import ip_network, ip_interface, ip_address

listofip = []
for k in ip_network("10.0.0.0/16"):
    listofip.append(str(k))
#list will have 65536 ips

csv_file_columns = ['ipAddress', 'port_port_name_protocol', 'vm_name', 'vm_otype', 'vm_oid', 'subnet_ip', 'subnet_netmask', 'subnet_prefixLength', 'subnet_networkAddress', 'subnet_cidr', 'subnet_start', 'subnet_end', 'ipAddressType', 'privateAddress', 'source', 'Ipmetadata_domain', 'ipmetadata_isp', 'host_name', 'host_otype', 'host_oid', 'dnsinfo_ipdomain', 'dnsinfo_ip', 'dnsinfo_domainname', 'dnsinfo_hostname', 'dnsinfo_source', 'k8s_service_name', 'k8s_service_otype', 'k8s_service_oid', 'k8s_cluster_name', 'k8s_cluster_otype', 'k8s_cluster_oid', 'k8s_namespace_name', 'k8s_namespace_otype', 'k8s_namespace_oid', 'k8s_node_name', 'k8s_node_otype', 'k8s_node_oid', 'IP_entity_name', 'IP_entity_otype', 'IP_entity_oid', 'Nic_name', 'Nic_otype', 'Nic_oid', 'sg_name', 'sg_otype', 'sg_oid', 'IP_set_name', 'IP_set_otype', 'IP_set_oid', 'STag_name', 'STag_otype', 'STag_oid', 'L2net_name', 'L2net_otype', 'L2net_oid', 'Grp_name', 'Grp_otype', 'Grp_oid', 'cluster_name', 'cluster_otype', 'cluster_oid', 'RP_name', 'RP_otype', 'RP_oid', 'DC_name', 'DC_otype', 'DC_oid', 'EP_name', 'EP_otype', 'EP_oid', 'managerNSX_name', 'managerNSX_otype', 'managerNSX_oid', 'lookupDomain_name', 'lookupDomain_otype', 'lookupDomain_oid', 'vpc_name', 'vpc_otype', 'vpc_oid', 'transportNode_name', 'transportNode_otype', 'transportNode_oid', 'Dvpg_name', 'Dvpg_otype', 'Dvpg_oid', 'Dvs_name', 'Dvs_otype', 'Dvs_oid', 'ipAddress', 'port', 'port_name', 'protocol', 'vm_name', 'vm_otype', 'vm_oid', 'subnet_ip', 'subnet_netmask', 'subnet_prefixLength', 'subnet_networkAddress', 'subnet_cidr', 'subnet_start', 'subnet_end', 'ipAddressType', 'privateAddress', 'source', 'Ipmetadata_domain', 'ipmetadata_isp', 'host_name', 'host_otype', 'host_oid', 'dnsinfo_ipdomain', 'dnsinfo_ip', 'dnsinfo_domainname', 'dnsinfo_hostname', 'dnsinfo_source', 'k8s_service_name', 'k8s_service_otype', 'k8s_service_oid', 'k8s_cluster_name', 'k8s_cluster_otype', 'k8s_cluster_oid', 'k8s_namespace_name', 'k8s_namespace_otype', 'k8s_namespace_oid', 'k8s_node_name', 'k8s_node_otype', 'k8s_node_oid', 'IP_entity_name', 'IP_entity_otype', 'IP_entity_oid', 'Nic_name', 'Nic_otype', 'Nic_oid', 'sg_name', 'sg_otype', 'sg_oid', 'IP_set_name', 'IP_set_otype', 'IP_set_oid', 'STag_name', 'STag_otype', 'STag_oid', 'L2net_name', 'L2net_otype', 'L2net_oid', 'Grp_name', 'Grp_otype', 'Grp_oid', 'cluster_name', 'cluster_otype', 'cluster_oid', 'RP_name', 'RP_otype', 'RP_oid', 'DC_name', 'DC_otype', 'DC_oid', 'managerNSX_name', 'managerNSX_otype', 'managerNSX_oid', 'lookupDomain_name', 'lookupDomain_otype', 'lookupDomain_oid', 'vpc_name', 'vpc_otype', 'vpc_oid', 'transportNode_name', 'transportNode_otype', 'transportNode_oid', 'Dvpg_name', 'Dvpg_otype', 'Dvpg_oid', 'Dvs_name', 'Dvs_otype', 'Dvs_oid']

csv_file = "IP_VM_MetaData_with_all_possible_ports_with_ip_as_int.csv"

def write_to_csv(dict_data):
    try:
        with open(csv_file, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_file_columns)
            for data in dict_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")

def gen_data(i)->dict:
    ip = listofip[i]
    int_ip =  int(ip_address(listofip[i]))
    subnet_Ip = str(ip_network(ip + '/27', strict=False)[0])
    start = int(ip_network(ip + '/27', strict=False)[0])
    end = int(ip_network(ip + '/27', strict=False)[-1])
    cidr = subnet_Ip + '/27'
    netmask = str(ip_interface(ip + '/27').netmask)
    ports_name_protocol = [(80,'https','TCP'),(443,'https','TCP'),(123,'ntp','UDP'),(22,'ssh','TCP'),(53,'dns','UDP'),(445,'microsoft-ds','UDP'),(389,'ldap','UDP'),(514,'syslog','TCP'),(137,'netbios-ns','TCP'),(902,'ideafarm-door','TCP')]
    #k = random.choice(ports_name_protocol)
    #port = k[0]
    #port_name = k[1]
    #protocol = k[2]
    #netbios-ns can be UDO
    #ldap can be TCP also
    #ssh can be UDP check later
    #Using Top 10
    vm_num = i
    #VM-0 to VM-49999
    host_num = vm_num//20
    #HOST-0 to HOST-2499
    #each host having 20 VM's
    rp_num = vm_num//30
    #RP-0 to RP-1666
    #1666*30+1*20
    cluster_num = host_num//10
    #CLUSTER-0 to CLUSTER-249
    #250 cluters and 10 hosts in each
    NSX_VC_num = cluster_num//25
    #NSX-0 to NSX-9
    #VC-0 to VC-9
    #each having 25 clusters
    DC_number = 1
    k8s_serv_num = vm_num//2500
    #k8s_serv0 to k8s_serv19
    #one per 2500 vms
    k8s_cluster_num = vm_num//5000
    #k8s_cluster0 to k8s_cluster9
    #one per 5000 vms
    k8s_namespace_num = vm_num//2000
    #k8s_namespace0 to k8s_namespace24
    #one per 2000 vms
    k8s_node_num = vm_num//5000
    #k8s_node0 to k8s_node9
    #one per 5000vm

    #assuming 1 nic per vm
    sg_num = vm_num//10
    #5000 sg's sg-0 to sg-4999
    #10vm per sg
    ipset_num =  vm_num//30
    #30 ips in one set
    Dvpg_num = vm_num//4
    Dvs_num = vm_num//120
    L2_num = vm_num//40
    Grp_num = vm_num//50


    return_value = {
        "ipAddress" : int_ip,
        "port_port_name_protocol" : ports_name_protocol,
        "vm_name" : 'VM-' + str(vm_num),
        "vm_otype" : 1,
        "vm_oid" : vm_num,
        "subnet_ip" : subnet_Ip,
        "subnet_netmask" : netmask,
        "subnet_prefixLength" : 27,
        "subnet_networkAddress" :subnet_Ip,
        "subnet_cidr" : cidr,
        "subnet_start" : start,
        "subnet_end" : end,
        "ipAddressType" : 'ENDPOINT',
        "privateAddress" : 1,
        "source" : 'VMware',
        "Ipmetadata_domain" : 'Domain',
        "ipmetadata_isp" : 'Isp',
        "host_name" : 'HOST-' + str(host_num),
        "host_otype" :4,
        "host_oid" : host_num,
        "dnsinfo_ipdomain":  int(ip_network(ip + '/19', strict=False)[0]),
        "dnsinfo_ip" : int(ip_network(ip + '/17', strict=False)[0]),
        "dnsinfo_domainname" : 'vmware.com',
        "dnsinfo_hostname" : 'vmware rtp 192.168.0.0',
        "dnsinfo_source" : 'vmware',
        "k8s_service_name" : 'K8s_service-'+str(k8s_serv_num),
        "k8s_service_otype": 1504,
        "k8s_service_oid" : k8s_serv_num,
        "k8s_cluster_name" : 'k8s_cluster-' + str(k8s_cluster_num),
        "k8s_cluster_otype" : 1501,
        "k8s_cluster_oid" : k8s_cluster_num,
        "k8s_namespace_name" : 'k8s_namespace-'+str(k8s_namespace_num),
        "k8s_namespace_otype" : 1503,
        "k8s_namespace_oid" : k8s_namespace_num,
        "k8s_node_name" : 'k8s_node-'+ str(k8s_node_num),
        "k8s_node_otype" : 1502,
        "k8s_node_oid" : k8s_node_num,
        "IP_entity_name" : ip,
        "IP_entity_otype" : 541,
        "IP_entity_oid" : vm_num,
        "Nic_name" : 'VNIC-' + str(vm_num),
        "Nic_otype" : 18,
        "Nic_oid" : vm_num,
        "sg_name" : 'SG-'+str(sg_num),
        "sg_otype" : 550,
        "sg_oid" : sg_num,
        "IP_set_name" : 'IPSET-'+ str(ipset_num),
        "IP_set_otype" : 84,
        "IP_set_oid" : ipset_num,
        "STag_name" : 'SecTag-'+ str(sg_num),
        "STag_otype" : 99,
        "STag_oid" : sg_num,
        "L2net_name" : 'VLAN-' + str(L2_num),
        "L2net_otype" : 12,
        "L2net_oid" : L2_num,
        "Grp_name" : 'GROUP-'+str(Grp_num),
        "Grp_otype" : 81,
        "Grp_oid" : Grp_num,
        "cluster_name" : 'CLUSTER-'+str(cluster_num),
        "cluster_otype" : 66,
        "cluster_oid" : cluster_num,
        "RP_name" : 'RP-' + str(rp_num),
        "RP_otype" : 79,
        "RP_oid" : rp_num,
        "DC_name" : 'DATACENTER101',
        "DC_otype" : 105,
        "DC_oid" : 1,
        "managerNSX_name" : 'NSX-Manager-' + str(NSX_VC_num),
        "managerNSX_otype" : 7,
        "managerNSX_oid" : NSX_VC_num,
        "lookupDomain_name" : 'GLOBAL',
        "lookupDomain_otype" : 197,
        "lookupDomain_oid" : 876567,
        "vpc_name" : 'AWS-VPC-'+str(vm_num//1000),
        "vpc_otype": 603,
        "vpc_oid" : vm_num/1000,
        "transportNode_name" : 'TN-'+str(NSX_VC_num),
        "transportNode_otype": 843,
        "transportNode_oid" : NSX_VC_num,
        "Dvpg_name" : 'DVPG-'+ str(Dvpg_num),
        "Dvpg_otype" : 3,
        "Dvpg_oid" : Dvpg_num,
        "Dvs_name" : 'DVG' + str(Dvs_num),
        "Dvs_otype" : 2,
        "Dvs_oid" : Dvs_num
    }
    return return_value


if __name__ == '__main__':
    for i in range(5000):
        print(f"writing to {csv_file} {i+1}th row")
        write_to_csv([gen_data(i)])
