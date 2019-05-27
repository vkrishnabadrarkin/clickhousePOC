ATTACH TABLE wikistat
(
    name String, 
    rollnum UInt16, 
    dept String
)
ENGINE = MergeTree()
ORDER BY name
SETTINGS index_granularity = 8192
