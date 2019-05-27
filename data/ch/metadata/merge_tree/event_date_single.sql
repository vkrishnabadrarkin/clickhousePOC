ATTACH TABLE event_date_single
(
    id UInt64, 
    time DateTime, 
    date Date, 
    type UInt16, 
    pokemon_id UInt16
)
ENGINE = MergeTree()
PARTITION BY date
ORDER BY (date, id)
SETTINGS index_granularity = 8192
