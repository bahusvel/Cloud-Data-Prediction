#!/usr/bin/python

import csv
import os
from csv import reader, writer

SIZE = 50001
CSV_IN = "removed.csv"
CSV_OUT = "50000.csv"

with open(CSV_IN, 'r') as csv_file:
	csv_reader = reader(csv_file)
	with open(CSV_OUT, 'w') as out_file:
		csv_writer = writer(out_file)
		count = 0
		for row in csv_reader:
			if count == SIZE:
				break
			csv_writer.writerow(row)
			count += 1