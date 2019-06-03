import csv
from ipaddress import ip_network, ip_interface, ip_address
import time

listofip = []
for k in ip_network("10.0.0.0/16"):
    listofip.append(str(k))
#list contains 65536 ips

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
        with open(csv_file, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(dict_data)
        csvfile.close()
    except IOError:
        print("I/O error")

def gen_data(i):
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

    return_value = [int_ip, 'VM-' + str(vm_num + 1) + '-' + ip, 1, vm_oid_range[vm_num], subnet_Ip, netmask, 27, subnet_Ip, cidr, start, end, 'ENDPOINT', 1, 'VMware', 'Domain', 'Isp', 'HOST-' + str(host_num + 1), 4, host_oid_range[host_num], int(ip_network(ip + '/19', strict=False)[0]), int(ip_network(ip + '/17', strict=False)[0]), 'vmware.com', 'vmware rtp 192.168.0.0', 'vmware', 'K8s_service-' + str(k8s_serv_num + 1), 1504, k8s_service_oid_range[k8s_serv_num], 'k8s_cluster-' + str(k8s_cluster_num), 1501, k8s_cluster_oid_range[k8s_cluster_num], 'k8s_namespace-' + str(k8s_namespace_num + 1), 1503, k8s_namespace_oid_range[k8s_namespace_num], 'k8s_node-' + str(k8s_node_num + 1), 1502, k8s_node_oid_range[k8s_node_num], ip, 541, IP_entity_oid_range[vm_num], 'VNetworkIntegratedChip-' + str(vm_num + 1), 18, Nic_oid_range[vm_num], 'SecurityGroup-' + str(sg_num + 1), 550, sg_oid_range[sg_num], 'IPSET-' + str(ipset_num + 1), 84, IP_set_oid_range[ipset_num], 'SecurityTag-' + str(sg_num + 1), 99, STag_oid_range[sg_num], 'VLocalAreaNetwork-' + str(L2_num + 1), 12, L2net_oid_range[L2_num], 'GROUP-' + str(Grp_num + 1), 81, Grp_oid_range[Grp_num], 'CLUSTER-' + str(cluster_num + 1), 66, cluster_oid_range[cluster_num], 'ResourcePool-' + str(rp_num + 1), 79, RP_oid_range[rp_num], 'DATACENTER101', 105, 987654489831, 'NSX-Manager-' + str(NSX_VC_num + 1), 7, managerNSX_oid_rage[NSX_VC_num], 'GLOBAL', 197, 987654489842, 'AWS-VPC-' + str(vm_num // 1000), 603, vpc_oid_range[vm_num // 1000], 'TransportNode-' + str(NSX_VC_num + 1), 843, transportNode_oid_range[NSX_VC_num], 'DistributedVirtualPortGroup-' + str(Dvpg_num + 1), 3, Dvpg_oid_range[Dvpg_num], 'DistributedVirtualSwitch' + str(Dvs_num + 1), 2, Dvs_oid_range[Dvs_num]]

    return return_value

if __name__ == '__main__':
    start = time.time()
    events = [gen_data(i) for i in range(50000)]
    csv_file = 'ipMetaDataInsertAtOneTime.csv'
    write_to_csv(events)
    end = time.time()
    took = round(end-start,2)
    print(f'inserted into {csv_file} 50000 ipmetadata took {took} seconds')