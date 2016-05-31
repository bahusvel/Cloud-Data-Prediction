#!/usr/bin/python

import csv
import os
from csv import reader, writer

CSV_IN = "/Users/denislavrov/Desktop/joined.csv"
CSV_OUT = "/Users/denislavrov/Desktop/filled.csv"

with open(CSV_IN, 'r') as in_file:
	csv_reader = reader(in_file)
	with open(CSV_OUT, 'w') as out_file:
		csv_writer = writer(out_file)
		csv_writer.writerow(next(csv_reader)) # header
		prow = next(csv_reader)
		# prefil the first row just in case if it has Nones
		for i, val in enumerate(prow):
			if val == "":
				prow[i] = 0
		count = 0
		for row in csv_reader:
			count += 1
			if count % 1000 == 0:
				print(count)
			
			for i, val in enumerate(row):
				if val == "":
					row[i] = prow[i]
			csv_writer.writerow(row)
			prow = row