import sys
import logging

logging.basicConfig(filename='reducer.log', format='%(message)s',level=logging.INFO, filemode='w')

def reducer():


    unit = ''
    entries_count = 0

    for line in sys.stdin:

        items=line.strip().split("\t")

        if len(items) != 2:
            continue

        if unit == items[0]:
            entries_count += float(items[1])
        else:
            print("{0}\t{1}".format(unit, entries_count))
            unit = items[0]
            entries_count = float(items[1])

    print("{0}\t{1}".format(unit, entries_count))

reducer()

