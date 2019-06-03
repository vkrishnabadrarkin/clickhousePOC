import csv
from ipaddress import ip_network, ip_interface, ip_address
import time

listofip = []
for k in ip_network("10.0.0.0/16"):
    listofip.append(str(k))
#list contains 65536 ips

csv_file_columns = ['ipAddress', 'vm_name', 'vm_otype', 'vm_oid', 'subnet_ip', 'subnet_netmask', 'subnet_prefixLength', 'subnet_networkAddress', 'subnet_cidr', 'subnet_start', 'subnet_end', 'ipAddressType', 'privateAddress', 'source', 'Ipmetadata_domain', 'ipmetadata_isp', 'host_name', 'host_otype', 'host_oid', 'dnsinfo_ipdomain', 'dnsinfo_ip', 'dnsinfo_domainname', 'dnsinfo_hostname', 'dnsinfo_source', 'k8s_service_name', 'k8s_service_otype', 'k8s_service_oid', 'k8s_cluster_name', 'k8s_cluster_otype', 'k8s_cluster_oid', 'k8s_namespace_name', 'k8s_namespace_otype', 'k8s_namespace_oid', 'k8s_node_name', 'k8s_node_otype', 'k8s_node_oid', 'IP_entity_name', 'IP_entity_otype', 'IP_entity_oid', 'Nic_name', 'Nic_otype', 'Nic_oid', 'sg_name', 'sg_otype', 'sg_oid', 'IP_set_name', 'IP_set_otype', 'IP_set_oid', 'STag_name', 'STag_otype', 'STag_oid', 'L2net_name', 'L2net_otype', 'L2net_oid', 'Grp_name', 'Grp_otype', 'Grp_oid', 'cluster_name', 'cluster_otype', 'cluster_oid', 'RP_name', 'RP_otype', 'RP_oid', 'DC_name', 'DC_otype', 'DC_oid', 'managerNSX_name', 'managerNSX_otype', 'managerNSX_oid', 'lookupDomain_name', 'lookupDomain_otype', 'lookupDomain_oid', 'vpc_name', 'vpc_otype', 'vpc_oid', 'transportNode_name', 'transportNode_otype', 'transportNode_oid', 'Dvpg_name', 'Dvpg_otype', 'Dvpg_oid', 'Dvs_name', 'Dvs_otype', 'Dvs_oid']

csv_file = "Ip_vm_metadata_final.csv"

vm_oid_range = range(987654321432,987654371432)
host_oid_range = range(987654371432,987654373932)
k8s_service_oid_range = range(987654373932,987654373952)
k8s_cluster_oid_range = range(987654373952,987654373962)
k8s_namespace_oid_range = range(987654373962,987654373987)
k8s_node_oid_range = range(987654373987,987654373997)
IP_entity_oid_range= range(987654373997,987654423997)
Nic_oid_range = range(987654423997,987654473997)
sg_oid_range = range(987654473997,987654478997)
IP_set_oid_range = range(987654478997,987654480664)
STag_oid_range = range(987654480664,987654485664)
L2net_oid_range = range(987654485664,987654486914)
Grp_oid_range = range(987654486914,987654487914)
cluster_oid_range = range(987654487914,987654488164)
RP_oid_range = range(987654488164,987654489831)
managerNSX_oid_rage = range(987654489832,987654489842)
vpc_oid_range = range(987654489843,987654489893)
transportNode_oid_range = range(987654489893,987654489903)
Dvpg_oid_range = range(987654489903,987654502403)
Dvs_oid_range = range(987654502403,987654502820)



def write_to_csv(dict_data):
    try:
        with open(csv_file, 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_file_columns)
            writer.writerows(dict_data)
            csvfile.close()
    except IOError:
        print("I/O error")

def gen_data(i)->dict:
    ip = listofip[i]
    int_ip = int(ip_address(listofip[i]))
    subnet_Ip = str(ip_network(ip + '/27', strict=False)[0])
    start = int(ip_network(ip + '/27', strict=False)[0])
    end = int(ip_network(ip + '/27', strict=False)[-1])
    cidr = subnet_Ip + '/27'
    netmask = str(ip_interface(ip + '/27').netmask)
    vm_num = i
    #VM-0 to VM-49999(+1 in int , +_string (ip))
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
        "vm_name" : 'VM-' + str(vm_num + 1) + '-' + ip,
        "vm_otype" : 1,
        "vm_oid" : vm_oid_range[vm_num],
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
        "host_name" : 'HOST-' + str(host_num + 1),
        "host_otype" :4,
        "host_oid" : host_oid_range[host_num],
        "dnsinfo_ipdomain":  int(ip_network(ip + '/19', strict=False)[0]),
        "dnsinfo_ip" : int(ip_network(ip + '/17', strict=False)[0]),
        "dnsinfo_domainname" : 'vmware.com',
        "dnsinfo_hostname" : 'vmware rtp 192.168.0.0',
        "dnsinfo_source" : 'vmware',
        "k8s_service_name" : 'K8s_service-'+str(k8s_serv_num + 1),
        "k8s_service_otype": 1504,
        "k8s_service_oid" : k8s_service_oid_range[k8s_serv_num],
        "k8s_cluster_name" : 'k8s_cluster-' + str(k8s_cluster_num),
        "k8s_cluster_otype" : 1501,
        "k8s_cluster_oid" : k8s_cluster_oid_range[k8s_cluster_num],
        "k8s_namespace_name" : 'k8s_namespace-'+str(k8s_namespace_num + 1),
        "k8s_namespace_otype" : 1503,
        "k8s_namespace_oid" : k8s_namespace_oid_range[k8s_namespace_num],
        "k8s_node_name" : 'k8s_node-'+ str(k8s_node_num + 1),
        "k8s_node_otype" : 1502,
        "k8s_node_oid" : k8s_node_oid_range[k8s_node_num],
        "IP_entity_name" : ip,
        "IP_entity_otype" : 541,
        "IP_entity_oid" : IP_entity_oid_range[vm_num],
        "Nic_name" : 'VNetworkIntegratedChip-' + str(vm_num + 1),
        "Nic_otype" : 18,
        "Nic_oid" : Nic_oid_range[vm_num],
        "sg_name" : 'SecurityGroup-'+str(sg_num + 1),
        "sg_otype" : 550,
        "sg_oid" : sg_oid_range[sg_num],
        "IP_set_name" : 'IPSET-'+ str(ipset_num + 1),
        "IP_set_otype" : 84,
        "IP_set_oid" : IP_set_oid_range[ipset_num],
        "STag_name" : 'SecurityTag-'+ str(sg_num + 1),
        "STag_otype" : 99,
        "STag_oid" : STag_oid_range[sg_num],
        "L2net_name" : 'VLocalAreaNetwork-' + str(L2_num + 1),
        "L2net_otype" : 12,
        "L2net_oid" : L2net_oid_range[L2_num],
        "Grp_name" : 'GROUP-'+str(Grp_num + 1),
        "Grp_otype" : 81,
        "Grp_oid" : Grp_oid_range[Grp_num],
        "cluster_name" : 'CLUSTER-'+str(cluster_num + 1),
        "cluster_otype" : 66,
        "cluster_oid" : cluster_oid_range[cluster_num],
        "RP_name" : 'ResourcePool-' + str(rp_num + 1),
        "RP_otype" : 79,
        "RP_oid" : RP_oid_range[rp_num],
        "DC_name" : 'DATACENTER101',
        "DC_otype" : 105,
        "DC_oid" : 987654489831,
        "managerNSX_name" : 'NSX-Manager-' + str(NSX_VC_num + 1),
        "managerNSX_otype" : 7,
        "managerNSX_oid" : managerNSX_oid_rage[NSX_VC_num],
        "lookupDomain_name" : 'GLOBAL',
        "lookupDomain_otype" : 197,
        "lookupDomain_oid" : 987654489842,
        "vpc_name" : 'AWS-VPC-'+str(vm_num//1000),
        "vpc_otype": 603,
        "vpc_oid" : vpc_oid_range[vm_num//1000],
        "transportNode_name" : 'TransportNode-'+str(NSX_VC_num + 1),
        "transportNode_otype": 843,
        "transportNode_oid" : transportNode_oid_range[NSX_VC_num],
        "Dvpg_name" : 'DistributedVirtualPortGroup-'+ str(Dvpg_num + 1),
        "Dvpg_otype" : 3,
        "Dvpg_oid" : Dvpg_oid_range[Dvpg_num],
        "Dvs_name" : 'DistributedVirtualSwitch' + str(Dvs_num + 1),
        "Dvs_otype" : 2,
        "Dvs_oid" : Dvs_oid_range[Dvs_num]
    }
    return return_value


if __name__ == '__main__':
    start = time.time()
    events = [gen_data(i) for i in range(1, 50000)]
    csv_file = 'ipMetaDataInsertAtOneTimedict.csv'
    write_to_csv(events)
    end = time.time()
    took = round(end - start, 2)
    print(f'inserted into {csv_file} 50000 ipmetadata took {took} seconds')