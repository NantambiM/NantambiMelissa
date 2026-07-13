import os
import csv
import json

# working with a txt file
# with open('report.txt','w') as file:
#     file.write('I love Python programming\n')
#     file.write('I am becoming a data scientist\n')

# print('Done')

# with open('report.txt','a') as file:
#     file.write('Every data scientist must learn python\n')

with open('report.txt','r') as file:
    content=file.read(6)
print(content)


# # working with a csv file
# import csv
# # opening the file
# with open('students.csv','r') as file:
#     reader=csv.reader(file)

#     # loop through each row
#     for row in reader:
#         print(row)

# # how to write to a csv file???
# # use a dictionary



# working with a json file
# import json

# student={
#     'name':'Melissa',
#     'age':'24',
#     'course':'BSSE'
# }
# with open('students.json','w') as file:
#     json.dump(student,file,indent=4)

# with open('students.json','w') as file:
#     student=json.load(file)
# print(student)
def create_text_file(path: str, lines=None):
    """Create a text file with optional lines."""
    lines = lines or []
    with open(path, 'w') as file:
        for line in lines:
            file.write(line + '\n')
    print(f'Text file created: {path}')


def append_text_file(path: str, text: str):
    """Append text to a text file."""
    with open(path, 'a') as file:
        file.write(text + '\n')
    print(f'Text appended to: {path}')


def read_text_file(path: str):
    """Read and return the full contents of a text file."""
    with open(path, 'r') as file:
        return file.read()


def read_csv_file(path: str):
    """Read a CSV file and return its rows."""
    with open(path, 'r', newline='') as file:
        reader = csv.reader(file)
        return list(reader)


def write_csv_file(path: str, rows):
    """Write rows to a CSV file."""
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print(f'CSV file written: {path}')


def read_json_file(path: str):
    """Read a JSON file and return the parsed object."""
    with open(path, 'r') as file:
        return json.load(file)


def write_json_file(path: str, data):
    """Write Python object data to a JSON file."""
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)
    print(f'JSON file written: {path}')


# Ensure sample files are created from code
report_path = 'report.txt'
if not os.path.exists(report_path):
    with open(report_path, 'w') as file:
        file.write('I love Python programming\n')
        file.write('I am becoming a data scientist\n')
        file.write('Every data scientist must learn python\n')
    print(f'Text file created: {report_path}')

students_csv_path = 'students.csv'
if not os.path.exists(students_csv_path):
    write_csv_file(students_csv_path, [
        ['Name', 'Age', 'Course'],
        ['Melissa', '24', 'BSSE'],
        ['Alice', '22', 'BSc IT'],
        ['John', '23', 'BBA']
    ])

students_json_path = 'students.json'
if not os.path.exists(students_json_path):
    write_json_file(students_json_path, {
        'name': 'Melissa',
        'age': '24',
        'course': 'BSSE'
    })

# Example usage for the new helpers
create_text_file('example_report.txt', [
    'This is an example report.',
    'It was created from Python code.'
])
append_text_file('example_report.txt', 'This line was appended later.')
print('example_report.txt contents:')
print(read_text_file('example_report.txt'))

print('students.csv contents:')
for row in read_csv_file(students_csv_path):
    print(row)

print('students.json contents:')
print(read_json_file(students_json_path))
