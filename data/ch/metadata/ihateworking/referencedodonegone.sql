ATTACH TABLE referencedodonegone
(
    CounterID UInt32, 
    Sign Int8, 
    IsNew UInt8, 
    VisitID UInt64, 
    UserID UInt64, 
    `Goals.ID` Array(UInt32), 
    `Goals.Serial` Array(UInt32), 
    `Goals.Price` Array(Int64), 
    `Goals.OrderID` Array(String), 
    `Goals.CurrencyID` Array(UInt32)
)
ENGINE = MergeTree()
ORDER BY UserID
SETTINGS index_granularity = 8192
