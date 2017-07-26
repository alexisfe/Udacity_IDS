import sys
import logging

from util import reducer_logfile

logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')


def reducer():
    '''
    Given the output of the mapper for this assignment, the reducer should
    print one row per weather type, along with the average value of
    ENTRIESn_hourly for that weather type, separated by a tab. You can assume
    that the input to the reducer will be sorted by weather type, such that all
    entries corresponding to a given weather type will be grouped together.

    In order to compute the average value of ENTRIESn_hourly, you'll need to
    keep track of both the total riders per weather type and the number of
    hours with that weather type. That's why we've initialized the variable
    riders and num_hours below. Feel free to use a different data structure in
    your solution, though.

    An example output row might look like this:
    'fog-norain\t1105.32467557'

    Since you are printing the output of your program, printing a debug
    statement will interfere with the operation of the grader. Instead,
    use the logging module, which we've configured to log to a file printed
    when you click "Test Run". For example:
    logging.info("My debugging message")
    Note that, unlike print, logging.info will take only a single argument.
    So logging.info("my message") will work, but logging.info("my","message") will not.
    '''

    key = None
    sum_val = 0
    count_val = 1

    for line in sys.stdin:
        new_key, new_val = line.strip().split('\t')

        if not key:
            key = new_key

        if key and key != new_key:
            print '{0}\t{1}'.format(key, sum_val / count_val)
            key = new_key
            sum_val = 0.0
            count_val = 0.0

        sum_val += float(new_val)
        count_val += 1.0

    print '{0}\t{1}'.format(key, sum_val / count_val)


reducer()
