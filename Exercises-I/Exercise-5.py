'''
Exercise - 9

Create a data file data.txt with the following data:
empid, empname, emplocation, empsalary
e001,iniyal,chennai,20000.00
e002,aniyal,bangalore,25000.00
e003,indulekha,trivandrum,18000.00

open the file, read line by line
-extract data and put it in the following format
    {
        "employees":[
            {
                "empid":"e001",
                "empname":"iniyal",
                "emplocation":"chennai",
                "empsalary":20000.00
            },
            {
                "empid":"e002",
                "empname":"aniyal",
                "emplocation":"bangalore",
                "empsalary":25000.00
            },
            {
            etc.
            }
        ]
    }
'''

import json

file_path = 'data.txt'
with open(file_path, 'r') as f: # We open the file for reading
    lines = [line.strip().split(',') for line in f.readlines()] # Split the lines by ',' and start reading each line

headers = lines[0] # we set the header at index 0, which is the first line from our file.
employee_data = { # start declaring a dictionary with key-value
    "employees": [ # we declare the employees block
        {
            headers[0]: line[0], # headers[0] corresponds to the first column, 'empid', line[0] is the value from the first employee 'e001', located in the first column
            headers[1]: line[1],
            headers[2]: line[2],
            headers[3]: float(line[3])
        } for line in lines[1:] # looping only the employee entries, skipping the header, that's why we start from lines[1:] instead of lines[0:] as the first one is the header
    ]
}

print(json.dumps(employee_data, indent=4)) #we indent the data to make it visually more appealing in the console