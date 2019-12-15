import csv

d = open("prog_file.csv", "w")
writer = csv.writer(d)
writer.writerow(["Name", "Phone number", "Country", "Age"])

d.close()