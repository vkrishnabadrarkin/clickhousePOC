ATTACH TABLE event_time_single
(
    id UInt64, 
    time DateTime, 
    type UInt16, 
    pokemon_id UInt16
)
ENGINE = MergeTree()
PARTITION BY toYYYYMM(time)
ORDER BY (time, id)
SETTINGS index_granularity = 8192
