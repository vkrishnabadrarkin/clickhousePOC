ATTACH TABLE something
(
    naame String, 
    whatever UInt8, 
    `money.kick` Array(String), 
    `money.rey` Array(String)
)
ENGINE = MergeTree()
ORDER BY naame
SETTINGS index_granularity = 8192
