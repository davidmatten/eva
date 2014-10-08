# This script accepts a path to the file: labdata_2014-07-10.csv, and adds a column, differences between dates, for a patient, for a lab_id.
import os, sys, datetime


def main(argv):
    # Confirm the file exists.
#{{{
    if len(argv) != 2:
        sys.exit("Only supply the path to file: labdata_2014-07-10.csv")
    if not os.path.exists(argv[1]):
        sys.exit("it appears the supplied file path does not exist.")
#}}}

# first pass over the data builds the dictionary of dates associated with the patient id + lab_id
    dct = {}
    # read into dictionary
# dct[pt_id__lab_id] = [date1, date2, date3]
    in_fn = argv[1]
    with open(in_fn, "r") as fh:
        for line in fh:
            row = line.strip().split(",")
            key = row[3] + "_" + row[5]
            date = row[4]
            if key not in dct.keys():
                dct[key] = [date]
            else:
                dct[key].append(date)

    print "built the dictionary"

# second pass over the data, writes to file, for line (reading, then writing), difference between row time, and min time in dct for the combo of pt_id and lab_id
    i = 0
    out_fn = os.path.split(in_fn)[0] + "/out.csv"
    with open(out_fn, "w") as fw:
        with open(in_fn, "r") as fh:
            for line in fh:
                i += 1
                print i
                row = line.strip().split(",")
                k = row[3] + "_" + row[5]
                mn = min(dct[k])
                date_dif = ( datetime.datetime.strptime(row[4], "%Y-%m-%d").date() - datetime.datetime.strptime(mn, "%Y-%m-%d").date() ).days
                new_row = row[:5] + [str(date_dif)] + row[5:]
                fw.write(",".join(new_row) + "\n")


if __name__ == "__main__":
    main(sys.argv)
    print "end"



