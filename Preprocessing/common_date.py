#!/usr/bin/python

import csv
import os

CSV_DIR = "/Users/denislavrov/Desktop/trimmed/"

from csv import reader
dir_list = os.listdir(CSV_DIR)

csvs = filter(lambda x: x.endswith(".csv"), dir_list)

dates = []

for csv in csvs:
	with open(CSV_DIR + csv, 'r') as csv_file:
		csv_reader = reader(csv_file)
		first_row = next(csv_reader)
		dates.append(first_row[1])

dates = sorted(dates)
print(dates)