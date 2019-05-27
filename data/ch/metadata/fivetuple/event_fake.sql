ATTACH TABLE event_fake
(
    id UInt64, 
    time DateTime, 
    type UInt16, 
    flow_id UInt16
)
ENGINE = MergeTree()
PARTITION BY toYYYYMM(time)
ORDER BY (time, id)
SETTINGS index_granularity = 8192
