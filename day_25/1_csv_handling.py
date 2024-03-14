# CSV stands for Comma Separated Values
# It is also one of the file formats like JSON to share information among the entities.
# Python has a default package for generating and parsing CSVs.
# Extension for a CSV file is .csv

import csv
filename = "day_25/students.csv"

result = []
with open(filename, "r") as cr:
    # print(csv.reader(cr))  # Parsing the students.csv file
    # print(list(csv.reader(cr)))  # [[], [], [], []]

    for count, each in enumerate(csv.reader(cr)):  # [(), (), ()]
        if count == 0:
            continue
        student = dict(id=each[0], name=each[1], age=each[2], address=each[3])
        result.append(student)

print(result)  # [{"id": 1, "name": "Jon"}, {"id": 1, "name", "Jon"}, {"id": 1, "name", "Jon"}]


result = []
with open(filename, "r") as cr:
    # print(csv.reader(cr))  # Parsing the students.csv file
    # print(list(csv.reader(cr)))  # [[], [], [], []]

    students = list(csv.reader(cr))  # [[], [], []]
    keys = students.pop(0)  
    for each in students:  # [[], []]
        student = dict(zip(keys, each))
        result.append(student)

print(result)  


# MCQ famous question about zip(), zip() is used to convert list into dictionary and tuple,  and took two input  like zip(a, b) 