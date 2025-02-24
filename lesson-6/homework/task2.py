from random import randint
records={}
def add_employee(name, position, salary):
    ID=randint(10000, 99999)
    new_employee= {
        "name" : name,
        "position" : position,
        "salary" : salary


    }
    records[ID]=new_employee
    
    with open ("employee.txt", "a") as file:
        file.write(f"{ID} : {new_employee}\n")
        
    return f"Employee {name} added with ID {ID}"
while True:
    reply=int(input(("""
Option 1: Append a new employee record to "employees.txt".\n
Option 2: Display all employee records from "employees.txt".\n
Option 3: Allow the user to search for an employee by Employee ID and display their details.\n
Option 4: Update an employee's information (name, position, or salary) based on the Employee ID.\n
Option 5: Delete an employee's record from the file using the Employee ID.\n
Option 6: Exit the program.
>>> 
""")))
    if reply==1:
        name=input("Enter the name of the new employee: ")
        position=input("Enter the position of the new employee: ")
        salary=int(input("Enter the annual salary of the new employee:  "))
        add_employee(name, position, salary)
    elif reply == 2:
        try:
            with open("employee.txt", "r") as file:
                content = file.read()
                print(content if content else "No employee records found.")
        except FileNotFoundError:
            print("No employee records found. The file does not exist.")
        
        
    
    elif reply == 3:
        search_id=int(input("Enter the ID number of employee: "))
        if  search_id in records:
            print(records[search_id])
        


    elif reply == 4:
        employee_id=int(input("Enter new id of the employee you want to access: "))
        name=input("Enter the new of the new employee: ")
        position=input("Enter new  position of the new employee: ")
        salary=int(input("Enter new annual salary of the new employee:  "))
        records[employee_id] = {"name": name, "position": position, "salary": salary}
    
    elif reply == 5:
        records.clear()
        with open ("employee.txt", "r") as file:
            records=file.readlines()
        print(records)


    elif reply == 6:
        break
    



    



