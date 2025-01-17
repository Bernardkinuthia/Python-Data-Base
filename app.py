import pymysql

# Database configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "xyz"
}

# Database operations
def get_employees():
    """Retrieve all employees fro m the database"""
    conn = pymysql.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee")
    employees = cursor.fetchall()
    conn.close()
    return employees

def add_employee(emp_name, hire_date, salary, dept_name):
    """Add  NEW EMPLOYEE TO THE DATABASE"""
    conn = pymysql.connect(**DB_CONFIG)
    cursor = conn.cursor()
    query = "INSERT INTO employee (emp_name, hire_date, salary, dept_name) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (emp_name, hire_date, salary, dept_name))
    conn.commit()
    conn.close()

def update_employee (emp_id, emp_name, hire_date, salary, dept_name):
    """"Updaing an existing employee details"""
    conn = pymysql.connect(**DB_CONFIG)
    cursor = conn.cursor()
    querry = "UPDATE employee SET emp_name=%s, hire_date=%s, salary=%s, dept_name=%s WHERE emp_id=%s"
    cursor.execute(querry, (emp_name, hire_date, salary, dept_name, emp_id))
    conn.commit()
    conn.close()

def delete_employee(emp_id):
    """Delete an employeefrom the database."""
    conn = pymysql.connect(**DB_CONFIG)
    cursor = conn.cursor()
    querry = "DELETE FROM employee WHERE emp_id=%s"
    cursor.execute(querry, (emp_id))
    conn.commit()
    conn.close()

# Meni-driven interface
def menu():
    while True:
        print("\n=== Employee Management System===")
        print("1. View all employees")
        print("2. Add a new employee")
        print("3. Update an employee")
        print("4. Delete an employee")
        print("5. Exit")

        choice = input("Enter your choice (1-5):")

        if choice == "1":
            employees = get_employees()
            if employees:
                print("\n---Employee lidt---")
                print("ID | Name      | Hire Date   | Salary   | Deapartment")   
                print ("_" *50)
                for emp in employees:
                    print(f"{emp[0]}     | {emp[1]:<12} | {emp[2]} | {emp[3]:<8} | {emp[4]}")
            else:
                print("\nNo employyes found")
        elif choice == "2":
            emp_name = input("Enter employee name: ")
            hire_date = input("Enter hire date (YYYY-MM-DD): ")
            salary = input("Enter Salary: ")
            dept_name = input("Enter department name: ")
            add_employee(emp_name, hire_date, salary, dept_name)
            print("Employee added successfully")
        elif choice == "3":
            emp_id = input("Enter employee ID to update ")
            emp_name = input("Enter employee name: ")
            hire_date = input("Enter hire date (YYYY-MM-DD): ")
            salary = input("Enter Salary: ")
            dept_name = input("Enter department name: ")
            update_employee(emp_id, emp_name, hire_date, salary, dept_name)
            print("Employee updated successfully")
        elif choice == "4":
            emp_id = input("Enter employee ID to delete: ")
            delete_employee(emp_id)
            print("Employee deleted successfully. ")
        elif choice =="5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice please try again.")

menu()