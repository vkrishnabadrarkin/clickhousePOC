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
