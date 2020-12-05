import csv
import json
import sys

with open(sys.argv[1], 'r') as input:
    reader = csv.reader(input)
    next(reader)

    resorts = []

    for row in reader:
        resorts.append({
            "skiResortName": row[0],
            "resortWebsite": row[1],
            "region": row[3],
            "snowConditionLink": row[6],
            "uphillPolicy": row[7],
            "uphillPolicyLink": row[8]
        })

    print(json.dumps(resorts))

