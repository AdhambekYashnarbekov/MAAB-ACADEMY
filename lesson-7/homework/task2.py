import json 

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

class EmployeeManager:
    def __init__(self):
        self.load_records()
    
    def load_records(self):
        """Load employee records to file"""
        try:
            with open("employee.txt", "r") as f:
                self.employee_records = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.employee_records = {}
    
    def save_records(self):
        """Save employee records"""
        with open("employee.txt", "w") as f:
            json.dump(self.employee_records, f, indent=4)
    
    def add_employee(self):
        employee_id = int(input("Employee ID: "))
        name = input("Employee name: ")
        position = input("Employee Position: ")
        salary = float(input("Employee's salary: "))
    
        self.employee_records[employee_id] = {
            "name": name,
            "position": position,
            "salary": salary
        }
        
        self.save_records()
        print("Employee added successfully!")
    
    def view_employee_records(self):
        """View employee records"""
        if self.employee_records:
            for emp_id, details in self.employee_records.items():
                print(f"ID: {emp_id}\nName: {details['name']}\nPosition: {details['position']}\nSalary: {details['salary']} ")
        else:
            print("No employee records found.")
    
    def search_employee_records(self):
        """Search for employee by ID."""
        employee_id = int(input("Enter employee ID: "))
        if employee_id in self.employee_records:
            details = self.employee_records[employee_id]
            return f"ID: {employee_id},\nName: {details['name']},\nPosition: {details['position']},\nSalary: {details['salary']}" 
        else:
            return "Employee not found"
    
    def update_employee(self):
        """Update an employee's information."""
        employee_id = int(input("Enter Employee ID to update: "))
        if employee_id in self.employee_records:
            name = input("Enter new name (leave blank to keep unchanged): ") or self.employee_records[employee_id]['name']
            position = input("Enter new position (leave blank to keep unchanged): ") or self.employee_records[employee_id]['position']
            salary_input = input("Enter new salary (leave blank to keep unchanged): ")
            salary = float(salary_input) if salary_input else self.employee_records[employee_id]['salary']
            
            self.employee_records[employee_id] = {
                "name": name,
                "position": position,
                "salary": salary
            }
            self.save_records()
            print("Employee information updated successfully!")
        else:
            print("Employee not found.")
    
    def delete_employee(self):
        """Delete an employee record."""
        employee_id = int(input("Enter Employee ID to delete: "))
        if employee_id in self.employee_records:
            del self.employee_records[employee_id]
            self.save_records()
            print("Employee record deleted successfully!")
        else:
            print("Employee not found.")

if __name__ == "__main__":
    manager = EmployeeManager()
    
    while True:
        print("\n1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee Information")
        print("5. Delete Employee Record")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_employee()
        elif choice == "2":
            manager.view_employee_records()
        elif choice == "3":
            print(manager.search_employee_records())
        elif choice == "4":
            manager.update_employee()
        elif choice == "5":
            manager.delete_employee()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")