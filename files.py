# second argument takes the mode, can be
#  r, a, rw, w
employee_file = open("employees.txt","r")
company_name = "Domino Engineering"
# checking if it's readable
print(employee_file.readable())

for employee in employee_file.readlines():
    print(f"{employee} is an employee at {company_name}")

# reads entire file
# print(employee_file.read())

#  reads from a specific line
# print(employee_file.readline())

# reads from a particular index
# print(employee_file.readlines()[2])

employee_file.close()