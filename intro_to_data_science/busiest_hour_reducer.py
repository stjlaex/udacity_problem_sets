import sys
import logging

logging.basicConfig(filename='reducer.log', format='%(message)s',level=logging.INFO, filemode='w')

def reducer():
    '''
    Write a reducer that will compute the busiest date and time (that is, the
    date and time with the most entries) for each turnstile unit. Ties should
    be broken in favor of datetimes that are later on in the month of May. You
    may assume that the contents of the reducer will be sorted so that all entries
    corresponding to a given UNIT will be grouped together.

    The reducer should print its output with the UNIT name, the datetime (which
    is the DATEn followed by the TIMEn column, separated by a single space), and
    the number of entries at this datetime, separated by tabs.

    For example, the output of the reducer should look like this:
    R001    2011-05-11 17:00:00	   31213.0
    R002	2011-05-12 21:00:00	   4295.0
    R003	2011-05-05 12:00:00	   995.0
    R004	2011-05-12 12:00:00	   2318.0
    R005	2011-05-10 12:00:00	   2705.0
    R006	2011-05-25 12:00:00	   2784.0
    R007	2011-05-10 12:00:00	   1763.0
    R008	2011-05-12 12:00:00	   1724.0
    R009	2011-05-05 12:00:00	   1230.0
    R010	2011-05-09 18:00:00	   30916.0
    ...
    ...
    '''

    max_entries = 0
    old_key = None
    datetime = ''

    for line in sys.stdin:

        items=line.strip().split("\t")

        if len(items) != 4:
            continue

        entries= float(items[1])

        if old_key == None:
            old_key = items[0]
            max_entries = entries 
            datetime = items[2] + ' ' + items[3]

        elif old_key == items[0]:
            if entries >= max_entries:
                datetime = items[2] + ' ' + items[3]
                max_entries = entries

        else:
            print("{0}\t{1}\t{2}".format(old_key, datetime, max_entries))
            old_key = items[0]
            max_entries = entries
            datetime = items[2] + ' ' + items[3]


    print("{0}\t{1}\t{2}".format(old_key, datetime, max_entries))



reducer()

