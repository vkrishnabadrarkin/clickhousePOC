ATTACH TABLE something2
(
    naame String, 
    whatever UInt8, 
    `money.kick` Array(String), 
    `money.rey` Array(String), 
    `double.jo` Array(String), 
    `double.op` Array(String)
)
ENGINE = MergeTree()
ORDER BY naame
SETTINGS index_granularity = 8192
