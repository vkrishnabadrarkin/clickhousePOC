ATTACH TABLE FIVEMAIN
(
    srcip UInt32, 
    destip UInt32, 
    flowprotocol String, 
    srcport UInt8, 
    destport UInt8
)
ENGINE = MergeTree()
ORDER BY srcip
SETTINGS index_granularity = 8192
