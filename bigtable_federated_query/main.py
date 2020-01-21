import json
import csv
import argparse

def readCommonJson():
    with open("./common/base.json") as js:
        data = json.load(js)
    return data

def getColumnQualifiers(column_array):
    element = column_array[0]
    final_arr = []
    with open("./input/coredep4.csv") as fl:
        line = csv.reader(fl)
        for row in line:
            # print(row[0])
            # print(element)
            if not "-" in row[0]:
                element["qualifierString"] = row[0]
                # print(element)
                final_arr.append(element.copy())
            else:
                continue
    return final_arr


def run(family):
    data = readCommonJson()
    data["bigtableOptions"]["columnFamilies"][0]["familyId"]=family
    data["bigtableOptions"]["columnFamilies"][0]["columns"] = getColumnQualifiers(data["bigtableOptions"]["columnFamilies"][0]["columns"])
    with open('./output/coredep4.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)



if __name__ == '__main__':
    family = "dep4"
    run(family)