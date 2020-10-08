import csv

def print_header():
	print("\n-------------------------------------")
	print ("{:<10}{:>20}".format(row[0], row[1]))
	print("-------------------------------------")

def main():
	with open('records.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter = ',')
		line_count = 0

		for row in csv_reader:
			if line_count == 0:
				print_header()
				line_count += 1
			else:
				print ("{:<10}{:>20}".format(row[0], row[1]))

		print("\nThere were {} examples.\n".format(line_count))

if __name__ == "__main__":
	main()
