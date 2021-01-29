import json

employee_names = ['Vamsi', 'Rakesh', 'Aashrith', 'Gayathri', 'Badri', 'Sabari', 'Kiran']
emp = open('employee_names.txt', 'w')   #open employee_names.txt file in write mode
emp.write(json.dumps(employee_names))   #writing the employee_names into the text file
emp.close()

