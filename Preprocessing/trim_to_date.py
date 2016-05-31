#!/usr/bin/python

import csv
import os
from csv import reader, writer

TRIM_DATE = '2016-02-22 16:29:54'
CSV_DIR = "/Users/denislavrov/Desktop/dump/"
OUT_DIR = "/Users/denislavrov/Desktop/trimmed/"

dir_list = os.listdir(CSV_DIR)

csvs = filter(lambda x: x.endswith(".csv"), dir_list)

for csv in csvs:
	with open(CSV_DIR + csv, 'r') as csv_file:
		reached = False
		print(csv)
		csv_reader = reader(csv_file)
		with open(OUT_DIR + csv, 'w') as out_file:
			csv_writer = writer(out_file)
			for row in csv_reader:
				if not reached and row[1] == TRIM_DATE:
					reached = True
				if reached:
					csv_writer.writerow(row)
