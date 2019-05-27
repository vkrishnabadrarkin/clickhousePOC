ATTACH TABLE trail
(
    id UInt16, 
    name String, 
    Department String, 
    Age UInt16
)
ENGINE = MergeTree()
ORDER BY id
SETTINGS index_granularity = 8192
