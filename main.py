import os

FILE = "employees.txt"

class Employee:
    def __init__(self):
        self.employees = []
        self.load_employees()

    def load_employees(self):
        if os.path.exists(FILE):
            with open(FILE, "r") as file:
                for line in file:
                    emp_data = line.strip().split(",")
                    if len(emp_data) == 5: 
                        self.employees.append({
                            "id": emp_data[0],
                            "name": emp_data[1],
                            "designation": emp_data[2],
                            "salary": emp_data[3],
                            "address": emp_data[4],
                        })

    def save_employees(self):
        with open(FILE, "w") as file:
            for emp in self.employees:
                file.write(f"{emp['id']},{emp['name']},{emp['designation']},{emp['salary']},{emp['address']}\n")

    def add_employee(self): 
        while True: 
            emp_id = input("Enter Employee ID: ").strip() 
            if not emp_id: 
                print("Employee ID cannot be empty.")
                emp_id = input("Enter Employee ID: ").strip()
            
            if any(emp["id"] == emp_id for emp in self.employees):
                print("Error: Employee ID already exists. Please use a unique ID.")
                emp_id = input("Enter Employee ID: ").strip()
                
            name = input("Enter Employee Name: ").strip()
            if not name:
                print("Employee Name cannot be empty.")
                name = input("Enter Employee Name: ").strip()
                
            designation = input("Enter Employee Designation: ").strip()
            if not designation:
                print("Employee Designation cannot be empty.")
                designation = input("Enter Employee Designation: ").strip()
                
            salary = input("Enter Employee Salary: ").strip()
            if not salary:
                print("Employee Salary cannot be empty.")
                salary = input("Enter Employee Salary: ").strip()
                
            address = input("Enter Employee Address: ").strip()
            if not address:
                print("Employee Address cannot be empty.")
                address = input("Enter Employee Address: ").strip() 
            
            break
        
        self.employees.append({
            "id": emp_id,
            "name": name,
            "designation": designation,
            "salary": salary,
            "address": address
            })
        self.save_employees()
        print("Employee added successfully!")

    def update_employee(self):
        emp_id = input("Enter Employee ID to update: ")
        for emp in self.employees:
            if emp["id"] == emp_id:
                emp["name"] = input(f"Enter new name (current: {emp['name']}): ") or emp["name"]
                emp["designation"] = input(f"Enter new designation (current: {emp['designation']}): ") or emp["designation"]
                emp["salary"] = input(f"Enter new salary (current: {emp['salary']}): ") or emp["salary"]
                emp["address"] = input(f"Enter new address (current: {emp['address']}): ") or emp["address"]
                self.save_employees()
                print("Employee updated successfully!")
                return
        print("Employee not found.")

    def delete_employee(self):
        emp_id = input("Enter Employee ID to delete: ")
        for emp in self.employees:
            if emp["id"] == emp_id:
                self.employees.remove(emp)
                self.save_employees()
                print("Employee deleted successfully!")
                return
        print("Employee not found.")

    def view_employees(self):
        if not self.employees:
            print("No employees found.")
            return
        print(f"{'ID':<10}{'Name':<20}{'Designation':<20}{'Salary':<10}{'Address':<30}")
        print("-" * 90)
        for emp in self.employees:
            print(f"{emp['id']:<10}{emp['name']:<20}{emp['designation']:<20}{emp['salary']:<10}{emp['address']:<30}")

    def search_employee(self):
        keyword = input("Enter name or designation to search: ").lower()
        results = [
            emp for emp in self.employees if
            keyword in emp["name"].lower() or
            keyword in emp["designation"].lower()
        ]
        if not results:
            print("No employees found.")
            return
        print(f"{'ID':<10}{'Name':<20}{'Designation':<20}{'Salary':<10}{'Address':<30}")
        print("-" * 90)
        for emp in results:
            print(f"{emp['id']:<10}{emp['name']:<20}{emp['designation']:<20}{emp['salary']:<10}{emp['address']:<30}")


class EmployeeApp:
    def __init__(self):
        self.employee = Employee()

    def show_menu(self):
        while True:
            print("\n***Employee Management System***\n")
            print("1. Add Employee")
            print("2. Update Employee")
            print("3. Delete Employee")
            print("4. View All Employees")
            print("5. Search Employee")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.employee.add_employee()
            elif choice == "2":
                self.employee.update_employee()
            elif choice == "3":
                self.employee.delete_employee()
            elif choice == "4":
                self.employee.view_employees()
            elif choice == "5":
                self.employee.search_employee()
            elif choice == "6":
                print("Exiting the system...")
                break
            else:
                print("Invalid choice. Please try again...")

if __name__ == "__main__":
    app = EmployeeApp()
    app.show_menu()
