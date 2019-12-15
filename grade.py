"""
grade calculation usingg csv
"""

import csv


with open("grade_rough.csv", "r") as rough_file:
    
    reader = csv.DictReader(rough_file)
    for row in reader:
        # getting the grades
        if row["Scores"] >= "70":
            grades = "A"
        elif row["Scores"] >= "60":
            grades = "B"
        elif row["Scores"] >= "50":
            grades = "C"
        else:
            grades = "fail"
        
        #writing the result to another csv file
        with open("grade.csv", "a") as grade:
            head = ["Subject", "Scores", "Grade"]
            grade_writer = csv.DictWriter(grade, fieldnames=head)
            grade_writer.writerow({"Subject":row["Subject"], "Scores":row["Scores"], "Grade":grades})
        
        print(row["Subject"])
