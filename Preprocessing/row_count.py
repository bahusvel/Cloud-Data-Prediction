#!/usr/bin/python

import csv
import os

CSV_DIR = "/Users/denislavrov/Desktop/sized/"

from csv import reader
dir_list = os.listdir(CSV_DIR)

csvs = filter(lambda x: x.endswith(".csv"), dir_list)

counts = []

for csv in csvs:
	count = 0
	with open(CSV_DIR + csv, 'r') as csv_file:
		csv_reader = reader(csv_file)
		for row in csv_reader:
			count += 1
		print(count)
		counts.append(count)

counts = sorted(counts)
print(counts)