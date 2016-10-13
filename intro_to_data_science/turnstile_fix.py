import csv

def fix_turnstile_data(filenames):

    for name in filenames:
        # your code here
        fin = open(name, 'r')
        fout = open('updated_' + name, 'w')

        reader_in = csv.reader(fin, delimiter=',')
        writer_out = csv.writer(fout, delimiter=',')
        for line in reader_in:
            starter = line[:3]
            length = len(line)
            pos=3
            row = starter
            while pos < length:
                chunk = line[pos:pos+5]
                row = starter + chunk
                pos+=5
                writer_out.writerow(row)

        fin.close()
        fout.close()



        wdate = datetime.datetime.strptime(date, '%m-%d-%y')
        date_formatted = wdate.strftime('%Y-%m-%d') # your code here
