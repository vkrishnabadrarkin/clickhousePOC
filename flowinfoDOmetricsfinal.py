import csv
import time
import datetime
import random
from ipaddress import ip_network, ip_address
import inserter_config


total_inserted_events = 0
total_flows_rows = 7200000000
modelkey_oid_range = range(9876543219876,9883743219876)
collector_id_range = range(9883743219876,9890943219876)
attribute_model_oid_range = range(9890943219876,9898143219876)
firewall_manager_model_oid_range = range(9898143219876,9905343219876)
reporter_entity_oid_range = range(9905343219876,9912543219876)
flowdomain_modelkey_oid_range = range(9912543219876,9919743219876)
srvcEP_oid_range = range(9919743219876,9926943219876)

metaDataFile = 'ipMetaDataInsertAtOneTime.csv'

event_date = datetime.datetime(2019, 6, 3)
with open(metaDataFile) as csvIPData:
    ipMetaData = list(csv.reader(csvIPData))


def fetch_metadata(fourtuple,j):
    global total_inserted_events
    src_ip = fourtuple[0]
    dst_ip = fourtuple[1]
    port = fourtuple[2]
    port_name = fourtuple[3]
    port_display = '['+str(port)+'] ' + port_name
    protocol = fourtuple[4]
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

    shared = 0
    if (ipMetaData[p][7] == ipMetaData[q][7]):
        networkLayer = 'LAYER_2'
        shared = 1
    else:
        networkLayer = 'LAYER_3'

    flow_version_data = [flow_name, 8912345, 515, modelKey, port, port, str(port), port_name, port_display, protocol, 32, int(src_ip), '255.255.255.255', str(ip_address(int(src_ip))), str(ip_network(int(src_ip))), src_ip, src_ip, 'ENDPOINT', 1, 'TBD', 'TBD', 'TBD', 32, dst_ip, '255.255.255.255', str(ip_address(int(dst_ip))), str(ip_network(int(dst_ip))), dst_ip, dst_ip, 'ENDPOINT', 1, 'TBD', 'TBD', 'TBD', 'EAST_WEST_TRAFFIC', shared, networkLayer, ipMetaData[p][6], ipMetaData[p][4], ipMetaData[p][5], ipMetaData[p][7], ipMetaData[p][8], ipMetaData[p][9], ipMetaData[p][10], 'SUBNET', 1, ipMetaData[p][13], ipMetaData[p][14], ipMetaData[p][15], ipMetaData[q][6], ipMetaData[q][4], ipMetaData[q][5], ipMetaData[q][7], ipMetaData[q][8], ipMetaData[q][9], ipMetaData[q][10], 'SUBNET', 1, ipMetaData[q][13], ipMetaData[q][14], ipMetaData[q][15], int(ipMetaData[p][16] == ipMetaData[q][16]), random.sample(flow_tag_list, 4), [flow_name, src_vm_name, dst_vm_name], ['flows', 'traffic'], ['admin@vmware.com', 'root@vmware.com'], ['vmware@vmware.com', 'vrni@vmware.com'], 'ALLOW', 'RID-' + str(modelKey), collector_id, 'AT_RULE' + str(modelKey), 7, attribute_model_oid_range[total_inserted_events], 'AT_firewall_manager' + str(modelKey), 8, firewall_manager_model_oid_range[total_inserted_events], collector_id, 'KCC0IABACBAA', 'PROTECTED', 'ALLOW', ipMetaData[p][19], ipMetaData[p][20], ipMetaData[p][21], ipMetaData[p][22], ipMetaData[p][23], ipMetaData[q][19], ipMetaData[q][20], ipMetaData[q][21], ipMetaData[q][22], ipMetaData[q][23], collector_id, 'reporter' + str(modelKey), 603, reporter_entity_oid_range[total_inserted_events], collector_id, ipMetaData[p][24], ipMetaData[p][25], ipMetaData[p][26], ipMetaData[p][27], ipMetaData[p][28], ipMetaData[p][29], ipMetaData[p][30], ipMetaData[p][31], ipMetaData[p][32], ipMetaData[p][33], ipMetaData[p][34], ipMetaData[p][35], collector_id, ipMetaData[q][24], ipMetaData[q][25], ipMetaData[q][26], ipMetaData[q][27], ipMetaData[q][28], ipMetaData[q][29], ipMetaData[q][30], ipMetaData[q][31], ipMetaData[q][32], ipMetaData[q][33], ipMetaData[q][34], ipMetaData[q][35], ipMetaData[p][36], ipMetaData[p][37], ipMetaData[p][38], ipMetaData[q][36], ipMetaData[q][37], ipMetaData[q][38], ipMetaData[p][39], ipMetaData[p][40], ipMetaData[p][41], ipMetaData[q][39], ipMetaData[q][40], ipMetaData[q][41], src_vm_name, ipMetaData[p][2], ipMetaData[p][3], dst_vm_name, ipMetaData[q][2], ipMetaData[q][3], ipMetaData[p][42], ipMetaData[p][43], ipMetaData[p][44], ipMetaData[q][42], ipMetaData[q][43], ipMetaData[q][44], ipMetaData[p][45], ipMetaData[p][46], ipMetaData[p][47], ipMetaData[q][45], ipMetaData[q][46], ipMetaData[q][47], ipMetaData[p][48], ipMetaData[p][49], ipMetaData[p][50], ipMetaData[q][48], ipMetaData[q][49], ipMetaData[q][50], ipMetaData[p][51], ipMetaData[p][52], ipMetaData[p][53], ipMetaData[q][51], ipMetaData[q][52], ipMetaData[q][53], ipMetaData[p][54], ipMetaData[p][55], ipMetaData[p][56], ipMetaData[q][54], ipMetaData[q][55], ipMetaData[q][56], ipMetaData[p][57], ipMetaData[p][58], ipMetaData[p][59], ipMetaData[q][57], ipMetaData[q][58], ipMetaData[q][59], ipMetaData[p][60], ipMetaData[p][61], ipMetaData[p][62], ipMetaData[q][60], ipMetaData[q][61], ipMetaData[q][62], ipMetaData[p][63], ipMetaData[p][64], ipMetaData[p][65], ipMetaData[q][63], ipMetaData[q][64], ipMetaData[q][65], ipMetaData[p][16], ipMetaData[p][17], ipMetaData[p][18], ipMetaData[q][16], ipMetaData[q][17], ipMetaData[q][18], dst_ip + port_display, 6065, srvcEP_oid_range[total_inserted_events], ipMetaData[p][66], ipMetaData[p][67], ipMetaData[p][68], ipMetaData[q][66], ipMetaData[q][67], ipMetaData[q][68], 'GLOBAL', 658, flowdomain_modelkey_oid_range[total_inserted_events], ipMetaData[p][69], ipMetaData[p][70], ipMetaData[p][71], ipMetaData[q][69], ipMetaData[q][70], ipMetaData[q][71], ipMetaData[p][72], ipMetaData[p][73], ipMetaData[p][74], ipMetaData[q][72], ipMetaData[q][73], ipMetaData[q][74], ipMetaData[p][75], ipMetaData[p][76], ipMetaData[p][77], ipMetaData[q][75], ipMetaData[q][76], ipMetaData[q][77], ipMetaData[p][78], ipMetaData[p][79], ipMetaData[p][80], ipMetaData[q][78], ipMetaData[q][79], ipMetaData[q][80], ipMetaData[p][78], ipMetaData[p][79], ipMetaData[p][80], ipMetaData[q][81], ipMetaData[q][82], ipMetaData[q][83]]

    return flow_version_data



k = inserter_config.numFourtuples

t = inserter_config.numVersionsPerHour

s = inserter_config.recordsPerFile


if __name__ == '__main__':
    start = time.time()
    print("inserter started at", time.ctime(start))
    events = []
    for i in range(1):
        with open('4Tuple_final_all_at_once.csv', 'r') as f:
            j = 0
            h = 0
            for eachTuple in csv.reader(f):
                event = fetch_metadata(eachTuple,j)
                all_active_timestamp = []
                all_metrics_active = []
                for v in range(t):
                    event_datetime = event_date.replace(minute=random.randint(0, 59), second=random.randint(0, 59))
                    all_active_timestamp.append(int(event_datetime.timestamp()))
                    srcBytes = random.randint(2500000, 28000000)
                    dstBytes = random.randint(2500000, 28000000)
                    totalBytes = srcBytes + dstBytes
                    totalPackets = random.randint(1, 100)
                    sessionCount = random.randint(100, 300)
                    rttMax = random.randint(20000, 70000)
                    rttAvg = (rttMax * 2) // 3
                    all_metrics_active.append([totalBytes, srcBytes, dstBytes, totalPackets, sessionCount, rttMax, rttAvg])
                all_active_timestamp.sort()
                sch_version = random.randint(1, 9)
                z = fetch_metadata(eachTuple,j)
                for l in range(t):
                    x = z
                    if (l == 0):
                        lastactivity = 0
                    else:
                        lastactivity = all_active_timestamp[l - 1]
                    x.insert(1,all_active_timestamp[l])
                    x.insert(95,sch_version)
                    x.insert(96,lastactivity)
                    x.insert(97,all_active_timestamp[l]+lastactivity)
                    x = x + all_metrics_active[l]
                    events.append(x)
                    total_inserted_events = total_inserted_events + 1
                    if (total_inserted_events/s == total_inserted_events//s):
                        h = h + 1
                        csv_file = f'flowinfo{i}_{h}.csv'
                        with open(csv_file,'w') as g:
                            writer = csv.writer(g)
                            writer.writerows(events)
                            print(f'a file created with {s} rows')
                        events = events[s:]
                j = j+1
                if (j == 500000): break
    if (len(events) < s):
        csvfilename = f'last set of data.csv'
        with open(csvfilename, 'w') as g:
            writer = csv.writer(g)
            writer.writerows(events)

    end = time.time()
    took = end - start
    print(f"inserter ended at {time.ctime(end)}; took: {took} seconds")