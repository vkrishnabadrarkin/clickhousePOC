ATTACH TABLE nested
(
    name String, 
    rollnum UInt16, 
    dept String, 
    `parents.father` Array(String), 
    `parents.mother` Array(String), 
    phone Int64
)
ENGINE = MergeTree()
ORDER BY name
SETTINGS index_granularity = 8192
