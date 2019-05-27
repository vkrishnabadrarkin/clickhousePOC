ATTACH TABLE FIVEMAIN2
(
    srcip String, 
    destip String, 
    flowprotocol String, 
    srcport UInt8, 
    destport UInt8, 
    flowhost String
)
ENGINE = MergeTree()
ORDER BY srcip
SETTINGS index_granularity = 8192
