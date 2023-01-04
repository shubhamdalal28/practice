import numpy as np
import csv

# file handling
with open("D:\\SOFTWARE TESTING\\Python\\xyz.csv", "r") as file:
    csv_file = csv.DictReader(file)
    print(csv_file)
    # insert data from csv file
    fname = []
    for row in csv_file:
        dict_converter = dict(row)
        print(dict_converter)
        f = dict_converter["fname"]
        fname.append(f)
        print(fname)

with open("D:\\SOFTWARE TESTING\\Python\\xyz.csv", "r") as file:
    csv_file = csv.DictReader(file)
    print(csv_file)
    lname = []
    for x in csv_file:
        dict_converter = dict(x)
        print(dict_converter)
        l = dict_converter["lname"]
        lname.append(l)
        print(lname)

domain = "@amazon.com"
fname_total = len(fname)
print(fname_total)
fname_count_variable = fname_total
if fname_total == fname_count_variable:
    print("fname count is:-", fname_count_variable)
else:
    print("Source system count error")

lname_total = len(lname)
print(lname_total)
lname_count_variable = lname_total
if lname_total == lname_count_variable:
    print("lname count is:-", lname_count_variable)
else:
    print("Source system count error")

mapping_dot = list(map(lambda x, y: x + '.' + y, fname, lname))
print(mapping_dot)

email = []
for i in mapping_dot:
    print(i)
    email_creation=i+domain
    print(email_creation)

    p=len(email_creation)
    if p<=53 :
        print("The length of email is perfect")
    else:
        print("The length of email is not perfect")

    email.append(email_creation)
    print(email)
count_email=len(email)
print("count of email:-",count_email)
# source and target system count check
if count_email == fname_total==lname_total:
    print("Count function is matched source and target")
else:
    print("Count function is not getting matched with source and target")
# checking avg salary
with open("D:\\SOFTWARE TESTING\\Python\\xyz.csv", "r") as file1:
    csv_file1 = csv.DictReader(file1)
    print(csv_file1)
    salary_new=[]
    for y in csv_file1:
        dict_converter=dict(y)
        print(dict_converter)
        s = dict_converter["payment"]
        salary_new.append(s)
        print(salary_new)
# Checking avg salary
for i in salary_new:
    print(salary_new)
test_list=list(map(int,salary_new))
mean_value1=np.mean(test_list)
print("The avg salary is :-", mean_value1)
