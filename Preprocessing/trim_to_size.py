#!/usr/bin/python

import csv
import os
from csv import reader, writer

SIZE = 600922
CSV_DIR = "/Users/denislavrov/Desktop/trimmed/"
OUT_DIR = "/Users/denislavrov/Desktop/sized/"

dir_list = os.listdir(CSV_DIR)

csvs = filter(lambda x: x.endswith(".csv"), dir_list)

for csv in csvs:
	with open(CSV_DIR + csv, 'r') as csv_file:
		print(csv)
		csv_reader = reader(csv_file)
		rows = list(csv_reader)
		with open(OUT_DIR + csv, 'w') as out_file:
			csv_writer = writer(out_file)
			csv_writer.writerows(rows[:SIZE])