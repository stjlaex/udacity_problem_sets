#
#
import os
import csv
import pprint

DATADIR = ""
DATAFILE = "beatles_discography.csv"


def parse_csv(datafile):
    data = []

    with open(datafile, "r") as f:
        r = csv.DictReader(f)
        for line in r:
            data.append(line)

    return data


if __name__ == '__main__':
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_csv(datafile)
    pprint.pprint(d)
