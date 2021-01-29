employee_names = ['Vamsi', 'Rakesh', 'Aashrith', 'Gayathri', 'Badri', 'Sabari', 'Kiran']
for emp in employee_names:          #iterating through employee_names
    print(emp)
employee_names.insert(0, 'Amar')    #inserting at index 0
print(employee_names)
employee_names.append('jayasree')   #appending into the employee_names
print(employee_names)
employee_names.remove('Amar')       #removing element from the employee_names
employee_names.remove('jayasree')
print(employee_names)

