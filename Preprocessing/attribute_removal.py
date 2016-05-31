import csv

REMOVE_FILE = "remove.txt"
IN_FILE = "filled.csv"
OUT_FILE = "removed.csv"

lines = set()
with open(REMOVE_FILE, 'r') as remove_file:
    lines = remove_file.readlines()
    lines = set(map(lambda x: x.strip(), lines))
    #print(lines)


with open(IN_FILE, 'r') as in_file:
    reader = csv.reader(in_file)
    
    header = next(reader)
    nheader = []
    delete_indexes = set()
    for i, attribute in enumerate(header):
        if attribute in lines:
            delete_indexes.add(i)
        else:
            nheader.append(attribute)
    print(delete_indexes)
    
    with open(OUT_FILE, 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(nheader)
        
        count = 0
        for row in reader:
            count += 1
            print(count)
            nrow = []
            for iv, value in enumerate(row):
                if iv not in delete_indexes:
                    nrow.append(value)
            writer.writerow(nrow)
