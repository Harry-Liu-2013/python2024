import csv

def demo():
    '''
  What is a CSV file
  CSV stands for comma-separated values. A CSV file is a delimited text file that uses a comma to separate values.

  A CSV file consists of one or more lines. Each line is a data record. And each data record consists of one or more values separated by commas. In addition, all the lines of a CSV file have the same number of values.

  Typically, you use a CSV file to store tabular data in plain text. The CSV file format is quite popular and supported by many software applications such as Microsoft Excel and Google Spreadsheet.
  '''
    '''
  Example read csv file
  '''
    import csv

    with open('country.csv', encoding="utf8") as f:
        # csv.reader(file) will create a csv file object (it's iterable)
        csv_reader = csv.reader(f)
        for line in csv_reader:
            print(line)
    '''
  Each line is a list of values. To access each value, you use the square bracket notation []. The first value has an index of 0. The second value has an index of 1, and so on.

  For example, the following accesses the first value of a particular line:
  line[0]
  
  '''
    '''
  Example 2 - read csv file with header and data using enumerate()
  '''
    import csv

    with open('country.csv', encoding="utf8") as f:
        csv_reader = csv.reader(f)
        for line_no, line in enumerate(csv_reader, 1):
            if line_no == 1:
                print('Header:')
                print(line)  # header
                print('Data:')
            else:
                print(line)  # data
    '''
  Example 3 - read csv file with header and data using next()
  '''
    import csv

    with open('country.csv', encoding="utf8") as f:
        csv_reader = csv.reader(f)

        # skip the first row
        next(csv_reader)

        # show the data
        for line in csv_reader:
            print(line)
    '''
  Example 4 - read csv file to get specific column
  '''
    import csv

    total_area = 0

    # calculate the total area of all countries

    with open('country.csv', encoding="utf8") as f:
        csv_reader = csv.reader(f)

        # skip the header
        next(csv_reader)

        # calculate total
        for line in csv_reader:
            total_area += float(line[1])

    print(total_area)
    '''
  DictReader

  When you use the csv.reader() function, you can access values of the CSV file using the bracket notation such as line[0], line[1], and so on. However, using the csv.reader() function has two main limitations:

  First, the way to access the values from the CSV file is not so obvious. For example, the line[0] implicitly means the country name. It would be more expressive if you can access the country name like line['country_name'].
  Second, when the order of columns from the CSV file is changed or new columns are added, you need to modify the code to get the right data.
  This is where the DictReader class comes into play. The DictReader class also comes from the csv module.
  '''

    import csv

    with open('country.csv', encoding="utf8") as f:
        csv_reader = csv.DictReader(f)
        # skip the header
        next(csv_reader)
        # show the data
        for line in csv_reader:
            # By using DictReader, it access the column by the column name
            print(f"The area of {line['name']} is {line['area']} km2")


    '''
    Rename column names when constructing DictReader
    '''
    import csv
    
    fieldnames = ['country_name', 'area', 'code2', 'code3']
    
    with open('country.csv', encoding="utf8") as f:
        csv_reader = csv.DictReader(f, fieldnames)
        next(csv_reader)
        for line in csv_reader:
            print(f"The area of {line['country_name']} is {line['area']} km2")
    '''
    Steps for writing a CSV file
    To write data into a CSV file, you follow these steps:
    
    - First, open the CSV file for writing (w mode) by using the open() function.
    - Second, create a CSV writer object by calling the writer() function of the csv module.
    - Third, write data to CSV file by calling the writerow() or writerows() method of the CSV writer object.
    - Finally, close the file once you complete writing data to it.
    '''
    import csv
    
    # open the file in the write mode
    with open('csv_output', 'w') as f:
        # create the csv writer
        writer = csv.writer(f)
        row = [1, 2, 3, 4]
        # write a row to the csv file
        writer.writerow(row)
    '''
    Example 1 - writing to csv file
    '''
    import csv
    
    header = ['name', 'area', 'country_code2', 'country_code3']
    data = ['Afghanistan', 652090, 'AF', 'AFG']
    
    with open('csv_output.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
    
        # write the header
        writer.writerow(header)
    
        # write the data
        writer.writerow(data)
    
    '''
    Example 2 - improvement - removing addition blank line
    '''
    import csv
    
    header = ['name', 'area', 'country_code2', 'country_code3']
    data = ['Afghanistan', 652090, 'AF', 'AFG']
    
    with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
    
        # write the header
        writer.writerow(header)
    
        # write the data
        writer.writerow(data)
    '''
    Example 3 - writing multiple rows
    '''
    import csv
    
    header = ['name', 'area', 'country_code2', 'country_code3']
    data = [['Albania', 28748, 'AL', 'ALB'], ['Algeria', 2381741, 'DZ', 'DZA'],
            ['American Samoa', 199, 'AS', 'ASM'], ['Andorra', 468, 'AD', 'AND'],
            ['Angola', 1246700, 'AO', 'AGO']]
    
    with open('csv_output.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
    
        # write the header
        writer.writerow(header)
    
        # write multiple rows
        writer.writerows(data)
    
    '''
    Example 4 - writing to CSV files using DictWriter
    '''
    import csv
    
    # csv header
    fieldnames = ['name', 'area', 'country_code2', 'country_code3']
    
    # csv data
    rows = [
        {'name': 'Albania',
        'area': 28748,
        'country_code2': 'AL',
        'country_code3': 'ALB'},
        {'name': 'Algeria',
        'area': 2381741,
        'country_code2': 'DZ',
        'country_code3': 'DZA'},
        {'name': 'American Samoa',
        'area': 199,
        'country_code2': 'AS',
        'country_code3': 'ASM'}
    ]
    
    with open('csv_output.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    

'''
Practice 1
You are given a cvs file named students.csv that contains multiple lines of text. Each line consists of a student's name followed by their score, separated by a comma. For example:

Alice,85
Bob,78
Charlie,92
Diana,88

Write a Python program to do the following:

1. Read the content of the file students.csv.
2. Calculate the average score of the students.
3. Write the names of the students who scored above the average into a new file named above_average.txt.
Requirements:

Your program should handle the case where the input file might be empty.
Ensure that the output file contains one name per line.
Include proper error handling for file operations.

Example students.csv:

Alice,85
Bob,78
Charlie,92
Diana,88

The output file above_average.txt should contain:

Alice
Charlie
Diana
'''

# read students.csv
def read_file_prac_1(file_name):
    lines = []
    with open("students.csv", 'r', encoding='UTF8') as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            lines.append(line)
        return lines
        

# calculate average score
def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)


# write data into above_average.txt
def write_above_average_students(file_name, students):
    with open("above_average_students.txt", "w") as f:
        for student in students:
            f.write(f"{student}\n")
    pass

# main function and call above 3 helper functions to get everything working
def main_prac_1():
    input_file = 'students.csv'
    output_file = 'above_average.txt'
    lines = read_file_prac_1(input_file)
    if not lines:
        return
    
    students = []
    scores = []

    # use enumerate to get line #, because we need to skip the header (1st line)
    for index, line in enumerate(lines):
        try:
          # name, score = line.strip().split(',')
          # score = int(score)
          # students.append((name, score))
          # scores.append(score)
            if index > 0:
                name = line[0]
                score = line[1]
                students.append((name, int(score)))
                scores.append(int(score))
        except ValueError:
          print(f"Skipping invalid line: {line}")
          continue
        
    average_score = calculate_average(scores)
    above_average_students = [
      name for name, score in students if score > average_score
    ]
        
    write_above_average_students(output_file, above_average_students)
    print(
      f"Names of students who scored above average have been written to {output_file}"
    )


'''
Practice 2

You are given a CSV file named employees.csv that contains information about employees' names, departments, and salaries. The file has the following format:


Name,Department,Salary
Alice,HR,60000
Bob,Engineering,80000
Charlie,HR,65000
Diana,Marketing,70000
Eve,Engineering,85000
Frank,Marketing,75000
Write a Python program to do the following:

Read the content of the file employees.csv.
Calculate the total and average salary for each department.
Write the total and average salaries for each department into a new CSV file named department_salaries.csv with the format:

Department,TotalSalary,AverageSalary
HR,125000,62500.00
Engineering,165000,82500.00
Marketing,145000,72500.00
Requirements:

Your program should handle the case where the input file might be empty.
Ensure that the output file contains one department and its total and average salary per line.
Include proper error handling for file operations.

Example:

Given the input file employees.csv with the following content:

Name,Department,Salary
Alice,HR,60000
Bob,Engineering,80000
Charlie,HR,65000
Diana,Marketing,70000
Eve,Engineering,85000
Frank,Marketing,75000

The output file department_salaries.csv should contain:

Department,TotalSalary,AverageSalary
HR,125000,62500.00
Engineering,165000,82500.00
Marketing,145000,72500.00
'''

# read the employee.csv file and return the file content
def read_employee_csv(file_name):
    with open("employee.csv", 'r', encoding='UTF8') as f:
        csv_reader = csv.DictReader(f)
        # TODO: should return lines instead of print
        return list(csv_reader)
        '''
        [
            {
                "Name": "Alice"
                "Department": "HR"
                "Salary": "60000"
            }
            ...

        ]
        '''


# calculate department salaries 
def calculate_department_salaries(data):
    # data should be a collection of records
    '''
    [
        {
            "Name": "Alice"
            "Department": "HR"
            "Salary": "60000"
        }
        ...
    
    ]
    '''

    # output date is dictionary
    # data should already been cleaned up without the header
    # key should be department
    # value should be a list of salary
    # {"HR": [100000, 60000, ....]}
    department_salaries = {}
    for line in data:
        depart = line["Department"]
        salary = line["Salary"]
        # add depart and salary into the dict department_salaries
        if depart not in department_salaries:
            department_salaries[depart] = [salary]
        else: 
            department_salaries[depart] = department_salaries[depart].append(salary)
    return department_salaries

# write data to department_salaries.csv
def write_department_salaries(file_name, department_salaries):
    with open(department_salaries.csv, "w") as f:
        # create csv writer
        writer = csv.writer(f)
        # write header first
        writer.writerow(["Department", "TotalSalary", "AverageSalary"])
        for depart, salaries in department_salaries.items():
            total_salary = sum(salaries)
            average_salary = total_salary / len(salaries)
            # TODO: because it write to a csv file
            # use csv.writer() or csv.DictWriter, not f.write()
            #f.write(f"{depart},{total_salary},{average_salary}\n")
            writer.writerow([depart, total_salary, average_salary])
        

# main function
def main_employee():
    input_file = "employee.csv"
    outfile_file = "department_salaries.csv"
    data = read_employee_csv(input_file)
    department_salaries = calculate_department_salaries(data)
    write_department_salaries(outfile_file, department_salaries)
    print(f"Department salary has been written to {outfile_file}")