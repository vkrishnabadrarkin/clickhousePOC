import csv
import time
import datetime
import random
from ipaddress import ip_network, ip_address
import inserter_config
import pandas as pd


total_inserted_events = 0
total_flows_rows = 7200000000
modelkey_oid_range = range(9876543219876,9883743219876)
collector_id_range = range(9883743219876,9890943219876)
attribute_model_oid_range = range(9890943219876,9898143219876)
firewall_manager_model_oid_range = range(9898143219876,9905343219876)
reporter_entity_oid_range = range(9905343219876,9912543219876)
flowdomain_modelkey_oid_range = range(9912543219876,9919743219876)
srvcEP_oid_range = range(9919743219876,9926943219876)



event_date = datetime.datetime(2019, 6, 3)

metaDataFile = 'ipMetaDataInsertAtOneTime.csv'
ipMetaData = pd.read_csv(metaDataFile,header=None)


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
    src_vm_name = ipMetaData[1][p]
    dst_vm_name = ipMetaData[1][q]
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
    if (ipMetaData[7][p] == ipMetaData[7][q]):
        networkLayer = 'LAYER_2'
        shared = 1
    else:
        networkLayer = 'LAYER_3'

    flow_version_data = [flow_name, 8912345, 515, modelKey, port, port, str(port), port_name, port_display, protocol, 32, int(src_ip), '255.255.255.255', str(ip_address(int(src_ip))), str(ip_network(int(src_ip))), src_ip, src_ip, 'ENDPOINT', 1, 'TBD', 'TBD', 'TBD', 32, dst_ip, '255.255.255.255', str(ip_address(int(dst_ip))), str(ip_network(int(dst_ip))), dst_ip, dst_ip, 'ENDPOINT', 1, 'TBD', 'TBD', 'TBD', 'EAST_WEST_TRAFFIC', shared, networkLayer, ipMetaData[6][p], ipMetaData[4][p], ipMetaData[5][p], ipMetaData[7][p], ipMetaData[8][p], ipMetaData[9][p], ipMetaData[10][p], 'SUBNET', 1, ipMetaData[13][p], ipMetaData[14][p], ipMetaData[15][p], ipMetaData[6][q], ipMetaData[4][q], ipMetaData[5][q], ipMetaData[7][q], ipMetaData[8][q], ipMetaData[9][q], ipMetaData[10][q], 'SUBNET', 1, ipMetaData[13][q], ipMetaData[14][q], ipMetaData[15][q], int(ipMetaData[16][p] == ipMetaData[16][q]), random.sample(flow_tag_list, 4), [flow_name, src_vm_name, dst_vm_name], ['flows', 'traffic'], ['admin@vmware.com', 'root@vmware.com'], ['vmware@vmware.com', 'vrni@vmware.com'], 'ALLOW', 'RID-' + str(modelKey), collector_id, 'AT_RULE' + str(modelKey), 7, attribute_model_oid_range[total_inserted_events], 'AT_firewall_manager' + str(modelKey), 8, firewall_manager_model_oid_range[total_inserted_events], collector_id, 'KCC0IABACBAA', 'PROTECTED', 'ALLOW', ipMetaData[19][p], ipMetaData[20][p], ipMetaData[21][p], ipMetaData[22][p], ipMetaData[23][p], ipMetaData[19][q], ipMetaData[20][q], ipMetaData[21][q], ipMetaData[22][q], ipMetaData[23][q], collector_id, 'reporter' + str(modelKey), 603, reporter_entity_oid_range[total_inserted_events], collector_id, ipMetaData[24][p], ipMetaData[25][p], ipMetaData[26][p], ipMetaData[27][p], ipMetaData[28][p], ipMetaData[29][p], ipMetaData[30][p], ipMetaData[31][p], ipMetaData[32][p], ipMetaData[33][p], ipMetaData[34][p], ipMetaData[35][p], collector_id, ipMetaData[24][q], ipMetaData[25][q], ipMetaData[26][q], ipMetaData[27][q], ipMetaData[28][q], ipMetaData[29][q], ipMetaData[30][q], ipMetaData[31][q], ipMetaData[32][q], ipMetaData[33][q], ipMetaData[34][q], ipMetaData[35][q], ipMetaData[36][p], ipMetaData[37][p], ipMetaData[38][p], ipMetaData[36][q], ipMetaData[37][q], ipMetaData[38][q], ipMetaData[39][p], ipMetaData[40][p], ipMetaData[41][p], ipMetaData[39][q], ipMetaData[40][q], ipMetaData[41][q], src_vm_name, ipMetaData[2][p], ipMetaData[3][p], dst_vm_name, ipMetaData[2][q], ipMetaData[3][q], ipMetaData[42][p], ipMetaData[43][p], ipMetaData[44][p], ipMetaData[42][q], ipMetaData[43][q], ipMetaData[44][q], ipMetaData[45][p], ipMetaData[46][p], ipMetaData[47][p], ipMetaData[45][q], ipMetaData[46][q], ipMetaData[47][q], ipMetaData[48][p], ipMetaData[49][p], ipMetaData[50][p], ipMetaData[48][q], ipMetaData[49][q], ipMetaData[50][q], ipMetaData[51][p], ipMetaData[52][p], ipMetaData[53][p], ipMetaData[51][q], ipMetaData[52][q], ipMetaData[53][q], ipMetaData[54][p], ipMetaData[55][p], ipMetaData[56][p], ipMetaData[54][q], ipMetaData[55][q], ipMetaData[56][q], ipMetaData[57][p], ipMetaData[58][p], ipMetaData[59][p], ipMetaData[57][q], ipMetaData[58][q], ipMetaData[59][q], ipMetaData[60][p], ipMetaData[61][p], ipMetaData[62][p], ipMetaData[60][q], ipMetaData[61][q], ipMetaData[62][q], ipMetaData[63][p], ipMetaData[64][p], ipMetaData[65][p], ipMetaData[63][q], ipMetaData[64][q], ipMetaData[65][q], ipMetaData[16][p], ipMetaData[17][p], ipMetaData[18][p], ipMetaData[16][q], ipMetaData[17][q], ipMetaData[18][q], dst_ip + port_display, 6065, srvcEP_oid_range[total_inserted_events], ipMetaData[66][p], ipMetaData[67][p], ipMetaData[68][p], ipMetaData[66][q], ipMetaData[67][q], ipMetaData[68][q], 'GLOBAL', 658, flowdomain_modelkey_oid_range[total_inserted_events], ipMetaData[69][p], ipMetaData[70][p], ipMetaData[71][p], ipMetaData[69][q], ipMetaData[70][q], ipMetaData[71][q], ipMetaData[72][p], ipMetaData[73][p], ipMetaData[74][p], ipMetaData[72][q], ipMetaData[73][q], ipMetaData[74][q], ipMetaData[75][p], ipMetaData[76][p], ipMetaData[77][p], ipMetaData[75][q], ipMetaData[76][q], ipMetaData[77][q], ipMetaData[78][p], ipMetaData[79][p], ipMetaData[80][p], ipMetaData[78][q], ipMetaData[79][q], ipMetaData[80][q], ipMetaData[78][p], ipMetaData[79][p], ipMetaData[80][p], ipMetaData[81][q], ipMetaData[82][q], ipMetaData[83][q]]
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
                j = j + 1
                if (j < (h*s)/t):
                    continue
                else:
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
                        x = z[:]
                        if (l == 0):
                            lastactivity = 0
                        else:
                            lastactivity = all_active_timestamp[l - 1]
                        x.insert(1,all_active_timestamp[l])
                        x.insert(95,sch_version)
                        x.insert(96,lastactivity)
                        x.insert(97,all_active_timestamp[l]+lastactivity)
                        x = x + all_metrics_active[l]
                        #print(x)
                        events.append(x)
                        total_inserted_events = total_inserted_events + 1
                        #print(total_inserted_events)
                        if (total_inserted_events/s == total_inserted_events//s):
                            h = h + 1
                            df = pd.DataFrame(events)
                            df.to_csv(f'flow_Data_{i+1}_{h}fake.csv.gz', header=False, index=False, compression='gzip')
                            print(f'a file created with {s} rows')
                            events = events[s:]
                    if (j == 500000): break
    #print(events)
    if (len(events) < s and len(events) > 0):
        df = pd.DataFrame(events)
        df.to_csv(f'remaining_data_versions.csv.gz', header=False, index=False, compression='gzip')
        print('last file also created')
    end = time.time()
    took = end - start
    print(f"inserter ended at {time.ctime(end)}; took: {took} seconds")