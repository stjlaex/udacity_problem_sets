import sys
import string
import logging

#from util import mapper_logfile
logging.basicConfig(filename='mapper.log', format='%(message)s', level=logging.INFO, filemode='w')

def mapper():

    """
    In this exercise, for each turnstile unit, you will determine the date and time
    (in the span of this data set) at which the most people entered through the unit.

    The input to the mapper will be the final Subway-MTA dataset, the same as
    in the previous exercise. You can check out the csv and its structure below:
    https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/turnstile_data_master_with_weather.csv

    For each line, the mapper should return the UNIT, ENTRIESn_hourly, DATEn, and
    TIMEn columns, separated by tabs. For example:
    'R001\t100000.0\t2011-05-01\t01:00:00'
    """

    for line in sys.stdin:

        items=line.strip().split(",")

        if items[1] == 'UNIT' or len(items) != 22:
            continue

        print("{0}\t{1}\t{2}\t{3}".format(items[1], items[6], items[2], items[3]))
        #UNIT/ENTRIESn_hourly/Daten/Timen

mapper()
