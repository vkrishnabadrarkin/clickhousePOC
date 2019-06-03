import os

numVersionsPerHour = int(os.getenv("numVersionsPerHour", 6))
recordsPerFile = int(os.getenv("recordsPerFile",300000))
numFourtuples = int(os.getenv("numFourtuples",50000000))

