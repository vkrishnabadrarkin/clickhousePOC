--to get details about all the tables (number of rows and size)
SELECT table, formatReadableSize(size) as size, rows FROM (
    SELECT
        table,
        sum(bytes) AS size,
        sum(rows) AS rows,
        min(min_date) AS min_date,
        max(max_date) AS max_date
    FROM system.parts
    WHERE active
    GROUP BY table
    ORDER BY rows DESC
)


--to delete table entirely
DROP table merge_tree.event_time_batch

--add column to existing table
ALTER TABLE fivetuple.FIVEMAIN2 ADD COLUMN flowhost String

-- update value to column
ALTER TABLE FIVEMAIN2 UPDATE flowhost = 'hs1-webapp-vmware.com' WHERE srcip = '192.168.1.2'

--count of name number of time repeated
select name, count() from experiment.wikistat GROUP BY (name)
--delete column
AlTER TABLE experiment.nested DROP COLUMN parents.phone
---add row individually
insert into flows.FLOWINFODOfinal FORMAT JSONEachRow {"name": "10.0.1.77VM33310.0.29.193", "modelkey_cid": 12345, "modelkey_otype": 515, "modelkey_oid": 1000000, "port.fstart": [2055], "port.fend": [2055], "port.display": ["2055"], "port.ianaName": ["other"], "port.ianaPortDisplay": ["[2055]other"], "fProtocol": "UDP", "srcIP.prefixLength": [27], "srcIP.ipAddress": ["10.0.1.77"], "srcIP.netMask": ["255.255.255.224"], "srcIP.networkAddress": ["10.0.1.6"], "srcIP.cidr": ["10.0.1.64/27"], "srcIP.fstart": [167772480], "srcIP.fend": [167772511], "srcIP.ipaddresstype": ["SUBNET"], "srcIP.privateaddress": [1], "srcIP.Source": ["UNKNOWN"], "srcIP.Ipmetadata_domain": ["UNKNOWN"], "srcIP.Ipmetadata_isp": ["UNKNOWN"], "dstIP.prefixLength": [27], "dstIP.ipAddress": ["10.0.29.193"], "dstIP.netMask": ["255.255.255.224"], "dstIP.networkAddress": ["10.0.29.19"], "dstIP.cidr": ["10.0.29.192/27"], "dstIP.fstart": [167779776], "dstIP.fend": [167779807], "dstIP.ipaddresstype": ["SUBNET"], "dstIP.privateaddress": [1], "dstIP.Source": ["UNKNOWN"], "dstIP.Ipmetadata_domain": ["UNKNOWN"], "dstIP.Ipmetadata_isp": ["UNKNOWN"], "TrfficType": "INTERNET_TRAFFIC", "shared": 1, "networkLayer": "LAYER_3", "srcsubnet.prefixLength": [19], "srcsubnet.ipAddress": ["10.0.1.77/19"], "srcsubnet.netMask": ["255.255.224.0"], "srcsubnet.networkAddress": ["10.0.0."], "srcsubnet.cidr": ["10.0.0.0/19"], "srcsubnet.fstart": [167772160], "srcsubnet.fend": [167780351], "srcsubnet.ipaddresstype": ["SUBNET"], "srcsubnet.privateaddress": [1], "srcsubnet.Source": ["UNKNOWN"], "srcsubnet.Ipmetadata_domain": ["UNKNOWM"], "srcsubnet.Ipmetadata_isp": ["UNKNOWM"], "dstsubnet.prefixLength": [19], "dstsubnet.ipAddress": ["10.0.29.193/19"], "dstsubnet.netMask": ["255.255.224.0"], "dstsubnet.networkAddress": ["10.0.0."], "dstsubnet.cidr": ["10.0.0.0/19"], "dstsubnet.fstart": [167772160], "dstsubnet.fend": [167780351], "dstsubnet.ipaddresstype": ["SUBNET"], "dstsubnet.privateaddress": [1], "dstsubnet.Source": ["UNKNOWN"], "dstsubnet.Ipmetadata_domain": ["UNKNOWM"], "dstsubnet.Ipmetadata_isp": ["UNKNOWM"], "withinhost": 0, "typetag": "TAG_DNAT_IP_MULTI_NAT_RULE", "__searchTags": ["10.0.1.77VM33310.0.29.193", "VM333", "VM7617"], "__related_entities": ["flows", "traffic"], "srcVmTags": ["admin@vmware.com", "badri@vmware.com"], "dstVmTags": ["vamsi@vmware.com", "krishna@vmware.com"], "attribute.reportedaction": ["DENY"], "attribute.reportedRuleId": ["RULE4762"], "attribute.collectorId": [125000], "attribute_rule.name": ["AT_RULE1000000"], "attribute_rule.modelkey_otype": [5200], "attribute_rule.modelkey_oid": [1000000], "attribute_firewallmanager.name": ["AT_firewall_manager1000000"], "attribute_firewallmanager.modelkey_otype": [8], "attribute_firewallmanager.modelkey_oid": [1000000], "activedpIds": [125000], "typeTagsPacked": "KCC0IABACBAA", "protectionStatus": "UNKNOWN_STATUS", "flowAction": "ALLOW", "srcDnsInfo.ipDomain": [167772480], "srcDnsInfo.ip": [167772160], "srcDnsInfo.domainName": ["domain10.0.1.77"], "srcDnsInfo.hostName": ["HOST20"], "srcDnsInfo.source": ["UNKNOWN"], "dstDnsInfo.ipDomain": [167779776], "dstDnsInfo.ip": [167772160], "dstDnsInfo.domainName": ["domain10.0.29.193"], "dstDnsInfo.hostName": ["HOST476"], "dstDnsInfo.source": ["UNKNOWN"], "reporterEntity.collectorId": [125000], "reporterEntity_reporter.name": ["reporter1000000"], "reporterEntity_reporter.modelkey_otype": [917], "reporterEntity_reporter.modelkey_oid": [1000000], "SchemaVersion": 7, "lastActivity": 1559023522, "activity": 779511761, "srck8Info.k8scollectorId": [125000], "srck8Info_k8sservice.name": ["service16"], "srck8Info_k8sservice.modelkey_otype": [1504], "srck8Info_k8sservice.modelkey_oid": [16], "srck8Info_k8scluster.name": ["cluster33"], "srck8Info_k8scluster.modelkey_otype": [1501], "srck8Info_k8scluster.modelkey_oid": [33], "srck8Info_k8snamespace.name": ["namespace13"], "srck8Info_k8snamespace.modelkey_otype": [503], "srck8Info_k8snamespace.modelkey_oid": [13], "srck8Info_k8snode.name": ["node33"], "srck8Info_k8snode.modelkey_otype": [1502], "srck8Info_k8snode.modelkey_oid": [33], "dstk8Info.k8scollectorId": [125000], "dstk8Info_k8sservice.name": ["service380"], "dstk8Info_k8sservice.modelkey_otype": [1504], "dstk8Info_k8sservice.modelkey_oid": [380], "dstk8Info_k8scluster.name": ["cluster761"], "dstk8Info_k8scluster.modelkey_otype": [1501], "dstk8Info_k8scluster.modelkey_oid": [761], "dstk8Info_k8snamespace.name": ["namespace304"], "dstk8Info_k8snamespace.modelkey_otype": [503], "dstk8Info_k8snamespace.modelkey_oid": [304], "dstk8Info_k8snode.name": ["node761"], "dstk8Info_k8snode.modelkey_otype": [1502], "dstk8Info_k8snode.modelkey_oid": [761], "lbflowtype": "LOGICAL", "loadBalancerInfo.type": ["LOGICAL"], "loadBalancerInfo.collectorId": [125000], "loadBalancerInfo.relevantPort": [2099], "loadBalancerInfo_loadbalancervIP.prefixLength": [27], "loadBalancerInfo_loadbalancervIP.ipAddress": ["10.0.1.77"], "loadBalancerInfo_loadbalancervIP.netMask": ["255.255.255.224"], "loadBalancerInfo_loadbalancervIP.networkAddress": ["10.0.1.6"], "loadBalancerInfo_loadbalancervIP.cidr": ["10.0.1.64/27"], "loadBalancerInfo_loadbalancervIP.fstart": [167772480], "loadBalancerInfo_loadbalancervIP.fend": [167772511], "loadBalancerInfo_loadbalancervIP.ipaddresstype": ["SUBNET"], "loadBalancerInfo_loadbalancervIP.privateaddress": [1], "loadBalancerInfo_loadbalancervIP.Source": ["UNKNOWN"], "loadBalancerInfo_loadbalancervIP.Ipmetadata_domain": ["UNKNOWN"], "loadBalancerInfo_loadbalancervIP.Ipmetadata_isp": ["UNKNOWN"], "loadBalancerInfo_loadbalancerinternalIP.prefixLength": [27], "loadBalancerInfo_loadbalancerinternalIP.ipAddress": ["10.0.29.193"], "loadBalancerInfo_loadbalancerinternalIP.netMask": ["255.255.255.224"], "loadBalancerInfo_loadbalancerinternalIP.networkAddress": ["10.0.29.19"], "loadBalancerInfo_loadbalancerinternalIP.cidr": ["10.0.29.192/27"], "loadBalancerInfo_loadbalancerinternalIP.fstart": [167779776], "loadBalancerInfo_loadbalancerinternalIP.fend": [167779807], "loadBalancerInfo_loadbalancerinternalIP.ipaddresstype": ["SUBNET"], "loadBalancerInfo_loadbalancerinternalIP.privateaddress": [1], "loadBalancerInfo_loadbalancerinternalIP.Source": ["UNKNOWN"], "loadBalancerInfo_loadbalancerinternalIP.Ipmetadata_domain": ["UNKNOWN"], "loadBalancerInfo_loadbalancerinternalIP.Ipmetadata_isp": ["UNKNOWN"], "srcIpEntity.name": ["10.0.1.77"], "srcIpEntity.modelkey_otype": [541], "srcIpEntity.modelkey_oid": [166666], "dstIpEntity.name": ["10.0.29.193"], "dstIpEntity.modelkey_otype": [541], "dstIpEntity.modelkey_oid": [200000], "srcNic.name": ["VNIC333"], "srcNic.modelkey_otype": [18], "srcNic.modelkey_oid": [333], "dstNic.name": ["VNIC7617"], "dstNic.modelkey_otype": [17], "dstNic.modelkey_oid": [7617], "srcVm.name": ["VM333"], "srcVm.modelkey_otype": [1601], "srcVm.modelkey_oid": [333], "dstVm.name": ["VM7617"], "dstVm.modelkey_otype": [1601], "dstVm.modelkey_oid": [7617], "srcSg.name": ["SG55"], "srcSg.modelkey_otype": [958], "srcSg.modelkey_oid": [55], "dstSg.name": ["SG1269"], "dstSg.modelkey_otype": [958], "dstSg.modelkey_oid": [1269], "srcIpSet.name": ["IPSET10"], "srcIpSet.modelkey_otype": [214], "srcIpSet.modelkey_oid": [10], "dstIpSet.name": ["IPSET7617"], "dstIpSet.modelkey_otype": [214], "dstIpSet.modelkey_oid": [238], "srcSt.name": ["securitytag55"], "srcSt.modelkey_otype": [99], "srcSt.modelkey_oid": [55], "dstSt.name": ["securitytag1269"], "dstSt.modelkey_otype": [99], "dstSt.modelkey_oid": [1269], "srcL2Net.name": ["Vlan10"], "srcL2Net.modelkey_otype": [13], "srcL2Net.modelkey_oid": [10], "dstL2Net.name": ["Vlan238"], "dstL2Net.modelkey_otype": [13], "dstL2Net.modelkey_oid": [238], "srcGroup.name": ["GROUP3"], "srcGroup.modelkey_otype": [81], "srcGroup.modelkey_oid": [3], "dstGroup.name": ["GROUP76"], "dstGroup.modelkey_otype": [81], "dstGroup.modelkey_oid": [76], "srcCluster.name": ["CLUSTER2"], "srcCluster.modelkey_otype": [66], "srcCluster.modelkey_oid": [2], "dstCluster.name": ["CLUSTER59"], "dstCluster.modelkey_otype": [66], "dstCluster.modelkey_oid": [59], "srcRp.name": ["RP41"], "srcRp.modelkey_otype": [79], "srcRp.modelkey_oid": [41], "dstRp.name": ["RP952"], "dstRp.modelkey_otype": [79], "dstRp.modelkey_oid": [952], "srcDc.name": ["DATACENTER101"], "srcDc.modelkey_otype": [105], "srcDc.modelkey_oid": [1], "dstDc.name": ["DATACENTER101"], "dstDc.modelkey_otype": [105], "dstDc.modelkey_oid": [1], "srcHost.name": ["HOST20"], "srcHost.modelkey_otype": [4], "srcHost.modelkey_oid": [20], "dstHost.name": ["HOST476"], "dstHost.modelkey_otype": [4], "dstHost.modelkey_oid": [476], "svcEP.name": ["10.0.29.193[2055]other"], "svcEP.modelkey_otype": [605], "svcEP.modelkey_oid": [166666], "srcManagers.name": ["NSX0"], "srcManagers.modelkey_otype": [8], "srcManagers.modelkey_oid": [0], "dstManagers.name": ["NSX3"], "dstManagers.modelkey_otype": [612], "dstManagers.modelkey_oid": [3], "flowDomain.name": ["GLOBAL"], "flowDomain.modelkey_otype": [658], "flowDomain.modelkey_oid": [125000], "srcLookupDomain.name": ["GLOBAL"], "srcLookupDomain.modelkey_otype": [197], "srcLookupDomain.modelkey_oid": [125000], "dstLookupDomain.name": ["GLOBAL"], "dstLookupDomain.modelkey_otype": [197], "dstLookupDomain.modelkey_oid": [125000], "srcVpc.name": ["AWS-VPC0"], "srcVpc.modelkey_otype": [603], "srcVpc.modelkey_oid": [0], "dstVpc.name": ["AWS-VPC3"], "dstVpc.modelkey_otype": [603], "dstVpc.modelkey_oid": [3], "srcTransportNode.name": ["TN0"], "srcTransportNode.modelkey_otype": [843], "srcTransportNode.modelkey_oid": [0], "dstTransportNode.name": ["TN3"], "dstTransportNode.modelkey_otype": [843], "dstTransportNode.modelkey_oid": [3], "srcDvpg.name": ["DVPG83"], "srcDvpg.modelkey_otype": [3], "srcDvpg.modelkey_oid": [83], "dstDvpg.name": ["DVPG1904"], "dstDvpg.modelkey_otype": [3], "dstDvpg.modelkey_oid": [1904], "srcDvs.name": ["DVS2"], "srcDvs.modelkey_otype": [2], "srcDvs.modelkey_oid": [2], "dstDvs.name": ["DVS63"], "dstDvs.modelkey_otype": [2], "dstDvs.modelkey_oid": [63]}

-- select imp columns
select name, port.fstart,fProtocol,srcIP.ipAddress, dstIP.ipAddress, TrfficType from flows.FLOWINFODOfinal
--join columns
insert into experiment.something2 values ('badrasi',12387,['vamswwi','kriswwhna'],['lossl','ajssay'],['weee','wewe'],['king','swsas'])
select naame,whatever,mon2.rey,double.jo,double.op from experiment.something2
ARRAY JOIN money as mon2
WHERE mon2.kick = 'krishna'

--table with model key flattened
CREATE TABLE flows.FLOWINFODOfinal
(
    name String,
    modelkey_cid Int32,
    modelkey_otype Int16,
    modelkey_oid Int32,
    port Nested
    (
        fstart UInt32,
        fend UInt32,
        display String,
        ianaName String,
        ianaPortDisplay String
    ),
    fProtocol Enum8('TCP' = 0, 'UDP' = 1, 'OTHER' = 2),--protocol entity
    srcIP Nested
    (
        prefixLength UInt32,
        ipAddress String,
        netMask String,
        networkAddress String,
        cidr String,
        fstart UInt64,
        fend UInt64,
        ipaddresstype String,
        privateaddress Int8,
        Source String,
        --IPmetadata_Geolocation, these tree belong to ipdetails entity
        Ipmetadata_domain String,--geolocation omitted as of now(has many unimportant parameteres)
        Ipmetadata_isp String
    ),
    dstIP Nested--ipaddress entity
    (
        prefixLength UInt32,
        ipAddress String,
        netMask String,
        networkAddress String,
        cidr String,
        fstart UInt64,
        fend UInt64,
        ipaddresstype String,
        privateaddress Int8,
        Source String,
        --IPmetadata_Geolocation, these tree belong to ipdetails entity
        Ipmetadata_domain String,--geolocation omitted as of now(has many unimportant parameteres)
        Ipmetadata_isp String
    ),
    TrfficType Enum8('EAST_WEST_TRAFFIC' = 1, 'INTERNET_TRAFFIC' = 2),
    shared Int8,
    networkLayer Enum8('UNKNOWN_LAYER' = 1, 'LAYER_2' = 2, 'LAYER_3' = 3),
    srcsubnet Nested--ipaddress entity
    (
        prefixLength UInt32,
        ipAddress String,
        netMask String,
        networkAddress String,
        cidr String,
        fstart UInt64,
        fend UInt64,
        ipaddresstype String,
        privateaddress Int8,
        Source String,
        --IPmetadata_Geolocation, these tree belong to ipdetails entity
        Ipmetadata_domain String,--geolocation omitted as of now(has many unimportant parameteres)
        Ipmetadata_isp String
    ),
    dstsubnet Nested--ipaddress entity
    (
        prefixLength UInt32,
        ipAddress String,
        netMask String,
        networkAddress String,
        cidr String,
        fstart UInt64,
        fend UInt64,
        ipaddresstype String,
        privateaddress Int8,
        Source String,
        --IPmetadata_Geolocation, these tree belong to ipdetails entity
        Ipmetadata_domain String,--geolocation omitted as of now(has many unimportant parameteres)
        Ipmetadata_isp String
    ),
    withinhost Int8,
    typetag Enum8('TAG_TRAFFIC_TYPE_UNKNOWN' = 1, 'TAG_INTERNET_TRAFFIC' = 2,'TAG_EAST_WEST_TRAFFIC' = 3, 'TAG_VM_VM_TRAFFIC'= 4, 'TAG_VM_PHY_TRAFFIC' = 5, 'TAG_PHY_PHY_TRAFFIC' = 6, 'TAG_SRC_IP_VMKNIC' = 7,'TAG_DST_IP_VMKNIC' = 8, 'TAG_SRC_IP_ROUTER_INT' = 11, 'TAG_DST_IP_ROUTER_INT'= 12, 'TAG_SRC_IP_VM'= 13,'TAG_DST_IP_VM'= 14, 'TAG_SRC_IP_INTERNET'= 15,'TAG_DST_IP_INTERNET'= 16, 'TAG_SRC_IP_PHYSICAL'= 17, 'TAG_DST_IP_PHYSICAL'= 18, 'TAG_SAME_HOST' = 19, 'TAG_DIFF_HOST' = 20, 'TAG_COMMON_HOST_INFO_UNKNOWN' = 28, 'TAG_SHARED_SERVICE' = 21, 'TAG_NOT_SHARED_SERVICE' = 22, 'TAG_NETWORK_SWITCHED' = 23, 'TAG_NETWORK_ROUTED' = 24, 'TAG_NETWORK_UNKNOWN' = 25, 'TAG_SRC_IP_VTEP' = 26, 'TAG_DST_IP_VTEP' = 27, 'TAG_UNICAST' = 29, 'TAG_BROADCAST' = 30, 'TAG_MULTICAST' = 31, 'TAG_SRC_IP_LINK_LOCAL' = 32, 'TAG_DST_IP_LINK_LOCAL' = 33, 'TAG_SRC_IP_CLASS_E' = 35, 'TAG_DST_IP_CLASS_E' = 36, 'TAG_SRC_IP_CLASS_A_RESERVED' = 37, 'TAG_DST_IP_CLASS_A_RESERVED' = 38, 'TAG_INVALID_IP_PACKETS' = 39, 'TAG_NOT_ANALYZED' = 40, 'TAG_GENERIC_INTERNET_SRC_IP' = 41, 'TAG_SNAT_DNAT_FLOW' = 42, 'TAG_NATTED' = 43, 'TAG_MULTINICS' = 44, 'TAG_MULTI_NATRULE' = 45, 'TAG_SRC_VC' = 46, 'TAG_DST_VC' = 47, 'TAG_SRC_AWS' = 48, 'TAG_DST_AWS' = 49, 'TAG_WITHIN_DC' = 50, 'TAG_DIFF_DC' = 51, 'TAG_SRC_IP_IN_SNAT_RULE_TARGET' = 52, 'TAG_DST_IP_IN_DNAT_RULE_ORIGINAL' = 53, 'TAG_SRC_IP_MULTI_NAT_RULE' = 54, 'TAG_DNAT_IP_MULTI_NAT_RULE' = 55, 'DEPRECATED_TAG_DST_IP_IN_SNAT_RULE_TARGET' = 56, 'DEPRECATED_TAG_SRC_IP_IN_DNAT_RULE_ORIGINAL' = 57, 'TAG_INVALID_IP_DOMAIN' = 58, 'TAG_WITHIN_VPC' = 59, 'TAG_DIFF_VPC' = 60, 'TAG_SRC_IP_IN_MULTIPLE_SUBNETS' = 61, 'TAG_DST_IP_IN_MULTIPLE_SUBNETS' = 62, 'TAG_SFLOW' = 63, 'TAG_PRE_NAT_FLOW' = 64, 'TAG_POST_NAT_FLOW' = 65, 'TAG_LOGICAL_FLOW' = 66, 'TAG_SRC_K8S_POD' = 67, 'TAG_DST_K8S_POD' = 68, 'TAG_POD_POD_TRAFFIC' = 69, 'TAG_VM_POD_TRAFFIC' = 70, 'TAG_POD_PHYSICAL_TRAFFIC' = 71),--9,10,34 arent there
    __searchTags Array(String),
    __related_entities Array(String),
    srcVmTags Array(String),
    dstVmTags Array(String),
    attribute Nested
    (
        reportedaction Enum8('ALLOW' = 0, 'DENY' = 1, 'DROP' = 2, 'REJECT' = 3, 'REDIRECT' = 4, 'DONT_REDIRECT' = 5),
        reportedRuleId String,
        collectorId UInt32
        --refDO rule

        --refDO firewallmanager
    ),
    attribute_rule Nested
    (
        name String,
        modelkey_otype Int16,
        modelkey_oid Int32
    ),
    attribute_firewallmanager Nested
    (
        name String,
        modelkey_otype Int16,
        modelkey_oid Int32
    ),
    activedpIds Array(UInt32),
    typeTagsPacked String,
    protectionStatus Enum8('UNKNOWN_STATUS' = 1, 'PROTECTED' = 2, 'ANY_ANY' = 3, 'UN_PROTECTED' = 4),
    flowAction Enum8('ALLOW' = 0, 'DENY' = 1, 'DROP' = 2, 'REJECT' = 3, 'REDIRECT' = 4, 'DONT_REDIRECT' = 5),
    srcDnsInfo Nested
    (
        ipDomain UInt64,
        ip UInt64,
        domainName String,
        hostName String,
        source String
    ),
    dstDnsInfo Nested
    (
        ipDomain UInt64,
        ip UInt64,
        domainName String,
        hostName String,
        source String
    ),
    reporterEntity Nested
    (
        --refDO reporter
        collectorId UInt32
    ),
    reporterEntity_reporter Nested
    (
        name String,
        modelkey_otype Int16,
        modelkey_oid Int32
    ),
    SchemaVersion UInt32,
    lastActivity UInt64,
    activity UInt32,
    srck8Info Nested
    (
        k8scollectorId UInt32
        --refDO k8sservice
        --refDO k8scluster
        --refDO k8snamespace
        --refDO k8snode
    ),
    srck8Info_k8sservice Nested
    (
        name String,
        modelkey_otype Int16,
        modelkey_oid Int32
    ),
    srck8Info_k8scluster Nested
    (
        name String,
        modelkey_otype Int16,
        modelkey_oid Int32
    ),
    srck8Info_k8snamespace Nested
    (
        name String,
        modelkey_otype Int16,
        modelkey_oid Int32
    ),
    srck8Info_k8snode Nested
    (
        name String,
        modelkey_otype Int16,
        modelkey_oid Int32
    ),

    dstk8Info Nested
    (
        k8scollectorId UInt32
        --refDO k8sservice
        --refDO k8scluster
        --refDO k8snamespace
        --refDO k8snode
    ),
    dstk8Info_k8sservice Nested
    (
        name String,
        modelkey_otype Int16,
        modelkey_oid Int32
    ),
    dstk8Info_k8scluster Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    dstk8Info_k8snamespace Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    dstk8Info_k8snode Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    lbflowtype Enum8('PRE_NAT' = 0, 'POST_NAT' = 1, 'LOGICAL' = 2),
    loadBalancerInfo Nested
    (
        type Enum8('PRE_NAT' = 0, 'POST_NAT' = 1, 'LOGICAL' = 2),
        --loadbalancerVIp can be specified out side or can be done here using extra tag
        --loadbalancerinternalIp
        collectorId UInt32,
        relevantPort UInt32
    ),
    loadBalancerInfo_loadbalancervIP Nested--ipaddress entity
    (
        prefixLength UInt32,
        ipAddress String,
        netMask String,
        networkAddress String,
        cidr String,
        fstart UInt64,
        fend UInt64,
        ipaddresstype String,
        privateaddress Int8,
        Source String,
        --IPmetadata_Geolocation, these tree belong to ipdetails entity
        Ipmetadata_domain String,--geolocation omitted as of now(has many unimportant parameteres)
        Ipmetadata_isp String
    ),
    loadBalancerInfo_loadbalancerinternalIP Nested--ipaddress entity
    (
        prefixLength UInt32,
        ipAddress String,
        netMask String,
        networkAddress String,
        cidr String,
        fstart UInt64,
        fend UInt64,
        ipaddresstype String,
        privateaddress Int8,
        Source String,
        --IPmetadata_Geolocation, these tree belong to ipdetails entity
        Ipmetadata_domain String,--geolocation omitted as of now(has many unimportant parameteres)
        Ipmetadata_isp String
    ),
    ------------------------------------------------------------------

    srcIpEntity Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    dstIpEntity Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    srcNic Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    dstNic Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    srcVm Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    dstVm Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    srcSg Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    dstSg Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    srcIpSet Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    dstIpSet Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    srcSt Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    dstSt Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    srcL2Net Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    dstL2Net Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    srcGroup Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    dstGroup Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    srcCluster Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    dstCluster Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    srcRp Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    dstRp Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    srcDc Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    dstDc Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    srcHost Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    dstHost Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    ----newly addeddd
    svcEP Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    srcManagers Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    dstManagers Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    flowDomain Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    srcLookupDomain Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    dstLookupDomain Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    srcVpc Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    dstVpc Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    srcTransportNode Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    dstTransportNode Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    srcDvpg Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    dstDvpg Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    srcDvs Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    ),
    dstDvs Nested
    (
        name String,
        modelkey_otype Int16, modelkey_oid Int32
    )
)
ENGINE = MergeTree()
order by (name)
---table with model key as string
CREATE TABLE flows.FLOWINFOnosearchtag
(
    name String,
    modelkey String,
    port Nested
    (
        fstart UInt32,
        fend UInt32,
        display String,
        ianaName String,
        ianaPortDisplay String
    ),
    fProtocol Enum8('TCP' = 0, 'UDP' = 1, 'OTHER' = 2),--protocol entity
    srcIP Nested
    (
        prefixLength UInt32,
        ipAddress String,
        netMask String,
        networkAddress String,
        cidr String,
        fstart UInt64,
        fend UInt64,
        ipaddresstype String,
        privateaddress Int8,
        Source String,
        --IPmetadata_Geolocation, these tree belong to ipdetails entity
        Ipmetadata_domain String,--geolocation omitted as of now(has many unimportant parameteres)
        Ipmetadata_isp String
    ),
    dstIP Nested--ipaddress entity
    (
        prefixLength UInt32,
        ipAddress String,
        netMask String,
        networkAddress String,
        cidr String,
        fstart UInt64,
        fend UInt64,
        ipaddresstype String,
        privateaddress Int8,
        Source String,
        --IPmetadata_Geolocation, these tree belong to ipdetails entity
        Ipmetadata_domain String,--geolocation omitted as of now(has many unimportant parameteres)
        Ipmetadata_isp String
    ),
    TrfficType Enum8('EAST_WEST_TRAFFIC' = 1, 'INTERNET_TRAFFIC' = 2),
    shared Int8,
    networkLayer Enum8('UNKNOWN_LAYER' = 1, 'LAYER_2' = 2, 'LAYER_3' = 3),
    srcsubnet Nested--ipaddress entity
    (
        prefixLength UInt32,
        ipAddress String,
        netMask String,
        networkAddress String,
        cidr String,
        fstart UInt64,
        fend UInt64,
        ipaddresstype String,
        privateaddress Int8,
        Source String,
        --IPmetadata_Geolocation, these tree belong to ipdetails entity
        Ipmetadata_domain String,--geolocation omitted as of now(has many unimportant parameteres)
        Ipmetadata_isp String
    ),
    dstsubnet Nested--ipaddress entity
    (
        prefixLength UInt32,
        ipAddress String,
        netMask String,
        networkAddress String,
        cidr String,
        fstart UInt64,
        fend UInt64,
        ipaddresstype String,
        privateaddress Int8,
        Source String,
        --IPmetadata_Geolocation, these tree belong to ipdetails entity
        Ipmetadata_domain String,--geolocation omitted as of now(has many unimportant parameteres)
        Ipmetadata_isp String
    ),
    withinhost Int8,
    typetag Enum8('TAG_TRAFFIC_TYPE_UNKNOWN' = 1, 'TAG_INTERNET_TRAFFIC' = 2,'TAG_EAST_WEST_TRAFFIC' = 3, 'TAG_VM_VM_TRAFFIC'= 4, 'TAG_VM_PHY_TRAFFIC' = 5, 'TAG_PHY_PHY_TRAFFIC' = 6, 'TAG_SRC_IP_VMKNIC' = 7,'TAG_DST_IP_VMKNIC' = 8, 'TAG_SRC_IP_ROUTER_INT' = 11, 'TAG_DST_IP_ROUTER_INT'= 12, 'TAG_SRC_IP_VM'= 13,'TAG_DST_IP_VM'= 14, 'TAG_SRC_IP_INTERNET'= 15,'TAG_DST_IP_INTERNET'= 16, 'TAG_SRC_IP_PHYSICAL'= 17, 'TAG_DST_IP_PHYSICAL'= 18, 'TAG_SAME_HOST' = 19, 'TAG_DIFF_HOST' = 20, 'TAG_COMMON_HOST_INFO_UNKNOWN' = 28, 'TAG_SHARED_SERVICE' = 21, 'TAG_NOT_SHARED_SERVICE' = 22, 'TAG_NETWORK_SWITCHED' = 23, 'TAG_NETWORK_ROUTED' = 24, 'TAG_NETWORK_UNKNOWN' = 25, 'TAG_SRC_IP_VTEP' = 26, 'TAG_DST_IP_VTEP' = 27, 'TAG_UNICAST' = 29, 'TAG_BROADCAST' = 30, 'TAG_MULTICAST' = 31, 'TAG_SRC_IP_LINK_LOCAL' = 32, 'TAG_DST_IP_LINK_LOCAL' = 33, 'TAG_SRC_IP_CLASS_E' = 35, 'TAG_DST_IP_CLASS_E' = 36, 'TAG_SRC_IP_CLASS_A_RESERVED' = 37, 'TAG_DST_IP_CLASS_A_RESERVED' = 38, 'TAG_INVALID_IP_PACKETS' = 39, 'TAG_NOT_ANALYZED' = 40, 'TAG_GENERIC_INTERNET_SRC_IP' = 41, 'TAG_SNAT_DNAT_FLOW' = 42, 'TAG_NATTED' = 43, 'TAG_MULTINICS' = 44, 'TAG_MULTI_NATRULE' = 45, 'TAG_SRC_VC' = 46, 'TAG_DST_VC' = 47, 'TAG_SRC_AWS' = 48, 'TAG_DST_AWS' = 49, 'TAG_WITHIN_DC' = 50, 'TAG_DIFF_DC' = 51, 'TAG_SRC_IP_IN_SNAT_RULE_TARGET' = 52, 'TAG_DST_IP_IN_DNAT_RULE_ORIGINAL' = 53, 'TAG_SRC_IP_MULTI_NAT_RULE' = 54, 'TAG_DNAT_IP_MULTI_NAT_RULE' = 55, 'DEPRECATED_TAG_DST_IP_IN_SNAT_RULE_TARGET' = 56, 'DEPRECATED_TAG_SRC_IP_IN_DNAT_RULE_ORIGINAL' = 57, 'TAG_INVALID_IP_DOMAIN' = 58, 'TAG_WITHIN_VPC' = 59, 'TAG_DIFF_VPC' = 60, 'TAG_SRC_IP_IN_MULTIPLE_SUBNETS' = 61, 'TAG_DST_IP_IN_MULTIPLE_SUBNETS' = 62, 'TAG_SFLOW' = 63, 'TAG_PRE_NAT_FLOW' = 64, 'TAG_POST_NAT_FLOW' = 65, 'TAG_LOGICAL_FLOW' = 66, 'TAG_SRC_K8S_POD' = 67, 'TAG_DST_K8S_POD' = 68, 'TAG_POD_POD_TRAFFIC' = 69, 'TAG_VM_POD_TRAFFIC' = 70, 'TAG_POD_PHYSICAL_TRAFFIC' = 71),--9,10,34 arent there
    __searchTags Array(String),
    __related_entities Array(String),
    srcVmTags Array(String),
    dstVmTags Array(String),
    attribute Nested
    (
        reportedaction Enum8('ALLOW' = 0, 'DENY' = 1, 'DROP' = 2, 'REJECT' = 3, 'REDIRECT' = 4, 'DONT_REDIRECT' = 5),
        reportedRuleId String,
        collectorId UInt32
        --refDO rule

        --refDO firewallmanager
    ),
    attribute_rule Nested
    (
        name String,
        modelkey String
    ),
    attribute_firewallmanager Nested
    (
        name String,
        modelkey String
    ),
    activedpIds Array(UInt32),
    typeTagsPacked String,
    protectionStatus Enum8('UNKNOWN_STATUS' = 1, 'PROTECTED' = 2, 'ANY_ANY' = 3, 'UN_PROTECTED' = 4),
    flowAction Enum8('ALLOW' = 0, 'DENY' = 1, 'DROP' = 2, 'REJECT' = 3, 'REDIRECT' = 4, 'DONT_REDIRECT' = 5),
    srcDnsInfo Nested
    (
        ipDomain UInt64,
        ip UInt64,
        domainName String,
        hostName String,
        source String
    ),
    dstDnsInfo Nested
    (
        ipDomain UInt64,
        ip UInt64,
        domainName String,
        hostName String,
        source String
    ),
    reporterEntity Nested
    (
        --refDO reporter
        collectorId UInt32
    ),
    reporterEntity_reporter Nested
    (
        name String,
        modelkey String
    ),
    SchemaVersion UInt32,
    lastActivity UInt64,
    activity UInt32,
    srck8Info Nested
    (
        k8scollectorId UInt32
        --refDO k8sservice
        --refDO k8scluster
        --refDO k8snamespace
        --refDO k8snode
    ),
    srck8Info_k8sservice Nested
    (
        name String,
        modelkey String
    ),
    srck8Info_k8scluster Nested
    (
        name String,
        modelkey String
    ),
    srck8Info_k8snamespace Nested
    (
        name String,
        modelkey String
    ),
    srck8Info_k8snode Nested
    (
        name String,
        modelkey String
    ),

    dstk8Info Nested
    (
        k8scollectorId UInt32
        --refDO k8sservice
        --refDO k8scluster
        --refDO k8snamespace
        --refDO k8snode
    ),
    dstk8Info_k8sservice Nested
    (
        name String,
        modelkey String
    ),
    dstk8Info_k8scluster Nested
    (
        name String,
        modelkey String
    ),
    dstk8Info_k8snamespace Nested
    (
        name String,
        modelkey String
    ),
    dstk8Info_k8snode Nested
    (
        name String,
        modelkey String
    ),
    lbflowtype Enum8('PRE_NAT' = 0, 'POST_NAT' = 1, 'LOGICAL' = 2),
    loadBalancerInfo Nested
    (
        type Enum8('PRE_NAT' = 0, 'POST_NAT' = 1, 'LOGICAL' = 2),
        --loadbalancerVIp can be specified out side or can be done here using extra tag
        --loadbalancerinternalIp
        collectorId UInt32,
        relevantPort UInt32
    ),
    loadBalancerInfo_loadbalancervIP Nested--ipaddress entity
    (
        prefixLength UInt32,
        ipAddress String,
        netMask String,
        networkAddress String,
        cidr String,
        fstart UInt64,
        fend UInt64,
        ipaddresstype String,
        privateaddress Int8,
        Source String,
        --IPmetadata_Geolocation, these tree belong to ipdetails entity
        Ipmetadata_domain String,--geolocation omitted as of now(has many unimportant parameteres)
        Ipmetadata_isp String
    ),
    loadBalancerInfo_loadbalancerinternalIP Nested--ipaddress entity
    (
        prefixLength UInt32,
        ipAddress String,
        netMask String,
        networkAddress String,
        cidr String,
        fstart UInt64,
        fend UInt64,
        ipaddresstype String,
        privateaddress Int8,
        Source String,
        --IPmetadata_Geolocation, these tree belong to ipdetails entity
        Ipmetadata_domain String,--geolocation omitted as of now(has many unimportant parameteres)
        Ipmetadata_isp String
    ),
    ------------------------------------------------------------------

    srcIpEntity Nested
    (
        name String,
        modelkey String
    ),
    dstIpEntity Nested
    (
        name String,
        modelkey String
    ),
    srcNic Nested
    (
        name String,
        modelkey String
    ),
    dstNic Nested
    (
        name String,
        modelkey String
    ),
    srcVm Nested
    (
        name String,
        modelkey String
    ),
    dstVm Nested
    (
        name String,
        modelkey String
    ),
    srcSg Nested
    (
        name String,
        modelkey String
    ),
    dstSg Nested
    (
        name String,
        modelkey String
    ),
    srcIpSet Nested
    (
        name String,
        modelkey String
    ),
    dstIpSet Nested
    (
        name String,
        modelkey String
    ),
    srcSt Nested
    (
        name String,
        modelkey String
    ),
    dstSt Nested
    (
        name String,
        modelkey String
    ),
    srcL2Net Nested
    (
        name String,
        modelkey String
    ),
    dstL2Net Nested
    (
        name String,
        modelkey String
    ),
    srcGroup Nested
    (
        name String,
        modelkey String
    ),
    dstGroup Nested
    (
        name String,
        modelkey String
    ),
    srcCluster Nested
    (
        name String,
        modelkey String
    ),
    dstCluster Nested
    (
        name String,
        modelkey String
    ),
    srcRp Nested
    (
        name String,
        modelkey String
    ),
    dstRp Nested
    (
        name String,
        modelkey String
    ),
    srcDc Nested
    (
        name String,
        modelkey String
    ),
    dstDc Nested
    (
        name String,
        modelkey String
    ),
    srcHost Nested
    (
        name String,
        modelkey String
    ),
    dstHost Nested
    (
        name String,
        modelkey String
    ),
    svcEP Nested
    (
        name String,
        modelkey String
    ),
    srcManagers Nested
    (
        name String,
        modelkey String
    ),
    dstManagers Nested
    (
        name String,
        modelkey String
    ),
    flowDomain Nested
    (
        name String,
        modelkey String
    ),
    srcLookupDomain Nested
    (
        name String,
        modelkey String
    ),
    dstLookupDomain Nested
    (
        name String,
        modelkey String
    ),
    srcVpc Nested
    (
        name String,
        modelkey String
    ),
    dstVpc Nested
    (
        name String,
        modelkey String
    ),
    srcTransportNode Nested
    (
        name String,
        modelkey String
    ),
    dstTransportNode Nested
    (
        name String,
        modelkey String
    ),
    srcDvpg Nested
    (
        name String,
        modelkey String
    ),
    dstDvpg Nested
    (
        name String,
        modelkey String
    ),
    srcDvs Nested
    (
        name String,
        modelkey String
    ),
    dstDvs Nested
    (
        name String,
        modelkey String
    )
)
ENGINE = MergeTree()
order by (name)