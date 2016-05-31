#!/usr/bin/python

import csv
import os
from csv import reader, writer

SIZE = 600922
CSV_DIR = "/Users/denislavrov/Desktop/sized/"
OUT_FILE = "/Users/denislavrov/Desktop/joined.csv"

dir_list = os.listdir(CSV_DIR)

csvs = filter(lambda x: x.endswith(".csv"), dir_list)

readers = []

for csv in csvs:
	csv_file = open(CSV_DIR + csv, 'r')
	readers.append(reader(csv_file))

with open(OUT_FILE, 'w') as out_file:
	csv_writer = writer(out_file)
	csv_writer.writerow(["date"] + csvs)
	for i in range(0, SIZE):
		if i % 1000 == 0:
			print(i)
		
		date = None
		row = []
		for ireader in readers:
			irow = next(ireader)
			date = irow[1]
			row.append(irow[2])
		csv_writer.writerow([date] + row)
	