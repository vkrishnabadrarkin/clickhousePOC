#!/usr/bin/env bash

export numVersionsPerHour=6
export recordsPerFile=300000
export numFourtuples=50000000
# max can be 2.4 billion(2450000000)
python3 ipmetadatalist.py
python3 4Tuplelist.py
python3 fowinfodo_final.py