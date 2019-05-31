#!/usr/bin/env bash

#export TABLE_NAME=FLOWINFODOfinal2
#export BULK_SIZE=10
#export DB_NAME=flows
##export EVENTS_PER_DAY=10
#python3 test.py

export TABLE_NAME= data_csv
export BULK_SIZE=10
export DB_NAME= csv_data_gen
#export EVENTS_PER_DAY=10
python3 withoutasync.py

#FILES=/path/to/*
#for f in $FILES
#do
#  echo "Processing $f file..."
#  cat $f
#done

#for f in *.csv
#do
#	echo "Processing $f file..."
#	head -n 500000 $f | clickhouse-client --password ubuntu --query="INSERT INTO flows.FLOWMETRICSTimeASInt FORMAT CSV"
#done
#for f in *.csv
#do
#	echo "Processing $f file..."
#	tail -n 500000 $f | clickhouse-client --password ubuntu --query="INSERT INTO flows.FLOWMETRICSTimeASInt FORMAT CSV"
#done

#for i in 1 2 3 4
#do
#    python3 createdatacsv.py
#done
#cat first100.csv | docker-compose run --rm client --host ch  --query="INSERT INTO flows.FLOWINFODOfinal3 FORMAT CSV"


# export TABLE_NAME=event_time_batchsr
# export BULK_SIZE=10 #10000000
# export DB_NAME=merge_tree
# export EVENTS_PER_DAY=10 #100000000
# python3 realinserter.py



# export TABLE_NAME=event_time_single
# export BULK_SIZE=1000
# export DB_NAME=merge_tree
# export HAS_DATE_COLUMN=0
# export EVENTS_PER_DAY=1000000
# python3 inserter.py

# export TABLE_NAME=event_time_order_func_batch
# export BULK_SIZE=100000
# export DB_NAME=merge_tree
# export HAS_DATE_COLUMN=0
# export EVENTS_PER_DAY=1000000
# python3 inserter.py

# export TABLE_NAME=event_time_order_func_single
# export BULK_SIZE=1000
# export DB_NAME=merge_tree
# export HAS_DATE_COLUMN=0
# export EVENTS_PER_DAY=1000000
# python3 inserter.py

# export TABLE_NAME=event_date_batch
# export BULK_SIZE=100000
# export DB_NAME=merge_tree
# export HAS_DATE_COLUMN=1
# export EVENTS_PER_DAY=1000000
# python3 inserter.py

# export TABLE_NAME=event_date_single
# export BULK_SIZE=1000
# export DB_NAME=merge_tree
# export HAS_DATE_COLUMN=1
# export EVENTS_PER_DAY=1000000
# python3 inserter.py