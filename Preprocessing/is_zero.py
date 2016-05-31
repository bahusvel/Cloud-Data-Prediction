#!/usr/bin/python

import csv
import os
from csv import reader, writer

CSV_IN = "/Users/denislavrov/Desktop/filled.csv"
DIMS = 235

with open(CSV_IN, 'r') as in_file:
	csv_reader = reader(in_file)
	header = next(csv_reader)
	vals = list([True for x in range(0, DIMS)])
	for row in csv_reader:
		for i, val in enumerate(row[1:]):
			if float(val) != 0:
				vals[i] = True
	print(vals)