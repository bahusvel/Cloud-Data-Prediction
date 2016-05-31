from csv import reader, writer
import statistics

resample = 60

CSV_IN = "/Users/denislavrov/Desktop/Cloud Data Prediction/removed.csv"
CSV_OUT = "/Users/denislavrov/Desktop/Cloud Data Prediction/resampled.csv"

temps = []

with open(CSV_IN, 'r') as csv_file:
	csv_reader = reader(csv_file)
	with open(CSV_OUT, 'w') as out_file:
		header = next(csv_reader)
		for _ in range(0, len(header)-1, 1):
			temps.append([])
		csv_writer = writer(out_file)
		csv_writer.writerow(header)
		count = 0
		for row in csv_reader:
			if count == 60:
				nrow = []
				nrow.append(row[0])
				for i, nval in enumerate(temps):
					nrow.append(statistics.mean(nval))
					temps[i] = []
				count = 0
				csv_writer.writerow(nrow)
			count += 1
			for i, val in enumerate(row[1:]):
				temps[i].append(float(val))