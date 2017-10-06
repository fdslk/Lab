import sys
import pandas as pd
import csv

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
print(data_frame)
data_frame.to_csv(output_file, index=False)

#with open(input_file, 'r') as csv_in_file:
#	with open(output_file, 'w') as csv_out_file:
#		filereader = csv.reader(csv_in_file, delimiter=',')
#		filewriter = csv.writer(csv_out_file, delimiter=',')
#		for row_list in filereader:
#			print(row_list)
#			filewriter.writerow(row_list)