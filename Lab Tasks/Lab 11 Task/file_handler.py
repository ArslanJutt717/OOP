import csv
from manager import Manager
from worker import Worker

class FileHandler:
    @staticmethod
    def save_employees(employees):
        with open("employees.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Age", "Salary", "Department", "Hours Worked"])
            for employee in employees:
                if isinstance(employee, Manager):
                    writer.writerow([employee.get_name(), employee.get_age(), employee.get_salary(), employee.get_department(), ''])
                elif isinstance(employee, Worker):
                    writer.writerow([employee.get_name(), employee.get_age(), employee.get_salary(), '', employee.get_hours_worked()])



    @staticmethod
    def load_employees(filename):
        employees = []
        try:
            with open("filename", mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row["Name"]
                    age = int(row["Age"])
                    salary = int(row["Salary"])
                    
                    if row["Department"]:
                        employees.append(Manager(name, age, salary, row["Department"]))
                    elif row["Hours Worked"]:
                        employees.append(Worker(name, age, salary, int(row["Hours Worked"])))
        except FileNotFoundError:
            print(f"{filename} not found. Starting with an empty employee list.")
        return employees
    
    def add_employee(employees):
            employee_type = input("Enter employee type (manager/worker): ").strip().lower()
            name = input("Enter name: ")
            try:
                age = int(input("Enter age: "))
                salary = int(input("Enter salary: "))
                if employee_type == 'manager':
                    department = input("Enter department: ")
                    employees.append(Manager(name, age, salary, department))
                elif employee_type == 'worker':
                    hours_worked = int(input("Enter hours worked: "))
                    employees.append(Worker(name, age, salary, hours_worked))
                    print("New employee added successfully!")
                else:
                    print("Invalid employee type entered.")
            except ValueError:
                print("Please enter valid numeric values for age, salary, and hours worked.")


    @staticmethod
    def display_employees(employees):        
        if not employees:
            print("No employees to display.")
            return
        for employee in employees:
            employee.display_info()
            print('-' * 20)

    @staticmethod
    def update_employee(employees):
        name = input("\nEnter the name of the employee to update:").lower().strip()
        for employee in employees:
            if employee.get_name().lower() == name:
                if isinstance(employee, Manager):
                    employee.set_name(input("Enter new name:"))
                    employee.set_age(int(input("Enter new age:")))
                    employee.set_salary(int(input("Enter new salary:")))
                    employee.set_department(input("Enter new department:"))
                elif isinstance(employee, Worker):
                    employee.set_name(input("Enter new name:"))
                    employee.set_age(int(input("Enter new age:")))
                    employee.set_salary(int(input("Enter new salary:")))
                    employee.set_hours_worked(int(input("Enter new hours worked:")))
                    print("Employee updated successfully!")
                    return
            print("Employee not found!")


      
    @staticmethod
    def delete_employee(employees):
        name = input("Enter the name of the employee to delete: ").strip().lower()
        for employee in employees:
            if employee.get_name().lower() == name:
                employees.remove(employee)
                print(f"Employee '{employee.get_name()}' deleted successfully.")
                return
        print(f"Employee '{name}' not found!")