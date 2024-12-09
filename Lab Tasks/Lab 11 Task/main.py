from manager import Manager
from worker import Worker
from file_handler import FileHandler

def main():
    filename = "employees.csv"
    employees = FileHandler.load_employees('filename')

    while True:
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Save and Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            FileHandler.add_employee(employees)
        elif choice == 2:
            FileHandler.display_employees(employees)
        elif choice == 3:
            FileHandler.update_employee(employees)
        elif choice == 4:
            FileHandler.delete_employee(employees)
        elif choice == 5:
            FileHandler.save_employees(employees)
            print("Employees saved successfully. Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == '__main__':
    main()
