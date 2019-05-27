ATTACH TABLE referencedo
(
    CounterID UInt32, 
    StartDate Date, 
    Sign Int8, 
    IsNew UInt8, 
    VisitID UInt64, 
    UserID UInt64, 
    `Goals.ID` Array(UInt32), 
    `Goals.Serial` Array(UInt32), 
    `Goals.EventTime` Array(DateTime), 
    `Goals.Price` Array(Int64), 
    `Goals.OrderID` Array(String), 
    `Goals.CurrencyID` Array(UInt32)
)
ENGINE = CollapsingMergeTree(StartDate, intHash32(UserID), (CounterID, StartDate, intHash32(UserID), VisitID), 8192, Sign)
