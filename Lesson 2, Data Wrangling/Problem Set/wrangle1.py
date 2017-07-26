import csv


def fix_turnstile_data(filenames):
    '''
    Filenames is a list of MTA Subway turnstile text files. A link to an example
    MTA Subway turnstile text file can be seen at the URL below:
    http://web.mta.info/developers/data/nyct/turnstile/turnstile_110507.txt

    As you can see, there are numerous data points included in each row of the
    a MTA Subway turnstile text file.

    You want to write a function that will update each row in the text
    file so there is only one entry per row. A few examples below:
    A002,R051,02-00-00,05-28-11,00:00:00,REGULAR,003178521,001100739
    A002,R051,02-00-00,05-28-11,04:00:00,REGULAR,003178541,001100746
    A002,R051,02-00-00,05-28-11,08:00:00,REGULAR,003178559,001100775

    Write the updates to a different text file in the format of "updated_" + filename.
    For example:
        1) if you read in a text file called "turnstile_110521.txt"
        2) you should write the updated data to "updated_turnstile_110521.txt"

    The order of the fields should be preserved. Remember to read through the
    Instructor Notes below for more details on the task.

    In addition, here is a CSV reader/writer introductory tutorial:
    http://goo.gl/HBbvyy

    You can see a sample of the turnstile text file that's passed into this function
    and the the corresponding updated file in the links below:

    Sample input file:
    https://www.dropbox.com/s/mpin5zv4hgrx244/turnstile_110528.txt
    Sample updated file:
    https://www.dropbox.com/s/074xbgio4c39b7h/solution_turnstile_110528.txt
    '''
    num_cols_head = 3
    num_cols_val = 5
    for name in filenames:
        with open(name, 'r') as fin:
            freader = csv.reader(fin)
            with open('updated_'+name, 'w') as fout:
                fwriter = csv.writer(fout)
                for rin in freader:
                    head = rin[:num_cols_head]
                    #Calculate & loop on the number of items available besides the header columns
                    for i in range(0, int((len(rin)-num_cols_head)/num_cols_val)):
                        index_start = num_cols_head+i*num_cols_val
                        index_end = num_cols_head+num_cols_val+i*num_cols_val
                        rout = head + rin[index_start:index_end]
                        fwriter.writerow(rout)

ex_in_file = 'https://www.dropbox.com/s/mpin5zv4hgrx244/turnstile_110528.txt'
ex_out_file = 'https://www.dropbox.com/s/074xbgio4c39b7h/solution_turnstile_110528.txt'
fix_turnstile_data(['wrangle1.txt'])
