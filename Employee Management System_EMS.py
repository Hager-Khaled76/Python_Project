# Enhanced Employee Management System (EMS)


# 1. Employee Class
class Employee:

    def __init__(
        self, emp_id, name, age, salary, department, job_title, email, phone
    ):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary
        self.department = department
        self.job_title = job_title
        self.email = email
        self.phone = phone

    def __str__(self):
        return (
            f"ID: {self.emp_id} | Name: '{self.name}' | Age: {self.age} | "
            f"Salary: {self.salary} | Dept: '{self.department}' | Title: '{self.job_title}'"
        )


# 2. EmployeeManager Class: Holds the list and business logic
class EmployeeManager:

    def __init__(self):
        self.employees = []

    # Check if ID exists (Prevent duplicates)
    def is_id_exists(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                return True
        return False

    # Add Employee
    def add_employee(self, emp):
        if self.is_id_exists(emp.emp_id):
            print("Error: Employee ID already exists!")
            return False
        self.employees.append(emp)
        print("Employee added successfully!")
        return True

    # Generator: List all employees using yield
    def get_all_employees_generator(self):
        for emp in self.employees:
            yield emp

    # Delete Employees by Age Range
    def delete_employee_with_age(self, age_from, age_to):
        cnt = 0
        for idx in range(len(self.employees) - 1, -1, -1):
            emp = self.employees[idx]
            if age_from <= emp.age <= age_to:
                print("Deleting:", emp.name)
                self.employees.pop(idx)
                cnt += 1
        if cnt == 0:
            print("No employees found in this age range.")

    # Search Options
    def search_by_id(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                return emp
        return None

    def search_by_name(self, name):
        results = []
        for emp in self.employees:
            if name.lower() in emp.name.lower():
                results.append(emp)
        return results

    def search_by_department(self, dept):
        results = []
        for emp in self.employees:
            if dept.lower() in emp.department.lower():
                results.append(emp)
        return results

    def search_by_salary_range(self, min_sal, max_sal):
        results = []
        for emp in self.employees:
            if min_sal <= emp.salary <= max_sal:
                results.append(emp)
        return results

    # Generator: Yield employees with salary >= min_salary
    def get_high_salary_employees(self, min_salary):
        for emp in self.employees:
            if emp.salary >= min_salary:
                yield emp

    # Sorting using sorted() and lambda
    def get_sorted_employees(self, option, reverse=False):
        if option == 1:  # Name
            return sorted(
                self.employees, key=lambda emp: emp.name.lower(), reverse=reverse
            )
        elif option == 2:  # Age
            return sorted(
                self.employees, key=lambda emp: emp.age, reverse=reverse
            )
        elif option == 3:  # Salary
            return sorted(
                self.employees, key=lambda emp: emp.salary, reverse=reverse
            )
        return self.employees

    # Statistics using Generator Expression
    def print_statistics(self):
        if len(self.employees) == 0:
            print("No employees to show statistics.")
            return

        total_emp = len(self.employees)

        # Generator Expression for total salary
        total_salary = sum(emp.salary for emp in self.employees)
        avg_salary = total_salary / total_emp

        # Generator Expression for average age
        avg_age = sum(emp.age for emp in self.employees) / total_emp

        highest_emp = max(self.employees, key=lambda emp: emp.salary)
        lowest_emp = min(self.employees, key=lambda emp: emp.salary)

        print("\n--- Employee Statistics ---")
        print("Total Employees:", total_emp)
        print("Average Salary :", avg_salary)
        print("Highest Salary :", highest_emp.salary, f"({highest_emp.name})")
        print("Lowest Salary  :", lowest_emp.salary, f"({lowest_emp.name})")
        print("Average Age    :", avg_age)


# 3. FrontEndManager Class
class FrontEndManager:

    def __init__(self):
        self.employee_manager = EmployeeManager()

    def print_options(self):
        print("\nProgram Options.")
        print("-----------------")
        messages = [
            "1) Add new Employee.",
            "2) List of All Employees.",
            "3) Delete Employee by age range.",
            "4) Search Employee.",
            "5) Update Employee.",
            "6) Sort Employees.",
            "7) Employee Statistics.",
            "8) Employees by Minimum Salary.",
            "9) End The Program.",
        ]
        print("\n".join(messages))

        try:
            inp = int(input("Enter Your Choice (1-9): "))
            return inp
        except ValueError:
            return -1

    def run(self):
        while True:
            choice = self.print_options()

            if choice == 1:
                self.add_employee_ui()

            elif choice == 2:
                print("\n--- List of All Employees ---")
                gen = self.employee_manager.get_all_employees_generator()
                count = 0
                for emp in gen:
                    print(emp)
                    count += 1
                if count == 0:
                    print("No employees found.")

            elif choice == 3:
                try:
                    age_from = int(input("Enter Age from: "))
                    age_to = int(input("Enter Age to: "))
                    self.employee_manager.delete_employee_with_age(
                        age_from, age_to
                    )
                except ValueError:
                    print("Invalid input! Please enter numbers for age.")

            elif choice == 4:
                self.search_employee_ui()

            elif choice == 5:
                self.update_employee_ui()

            elif choice == 6:
                self.sort_employees_ui()

            elif choice == 7:
                self.employee_manager.print_statistics()

            elif choice == 8:
                try:
                    min_sal = float(input("Enter Minimum Salary: "))
                    gen = self.employee_manager.get_high_salary_employees(
                        min_sal
                    )
                    for emp in gen:
                        print(emp)
                except ValueError:
                    print("Invalid salary input!")

            elif choice == 9:
                print("See you later.")
                break

            else:
                print("Wrong Choice! Please enter a number from 1 to 9.")

    # UI Helper Methods
    def add_employee_ui(self):
        print("\nEnter Employee Data.")
        try:
            emp_id = int(input("Enter Employee ID: "))
            if self.employee_manager.is_id_exists(emp_id):
                print("Error: ID already exists!")
                return

            name = input("Enter Name: ").strip()
            if name == "":
                print("Name cannot be empty!")
                return

            age = int(input("Enter Age (must be >= 18): "))
            if age < 18:
                print("Age must be at least 18!")
                return

            salary = float(input("Enter Salary: "))
            if salary < 0:
                print("Salary must be positive!")
                return

            department = input("Enter Department: ").strip()
            job_title = input("Enter Job Title: ").strip()
            email = input("Enter Email: ").strip()
            phone = input("Enter Phone: ").strip()

            emp = Employee(
                emp_id,
                name,
                age,
                salary,
                department,
                job_title,
                email,
                phone,
            )
            self.employee_manager.add_employee(emp)

        except ValueError:
            print("Invalid input! Age, ID, and Salary must be numbers.")

    def search_employee_ui(self):
        print("\n--- Search Options ---")
        print("1) Search by ID")
        print("2) Search by Name")
        print("3) Search by Department")
        print("4) Search by Salary Range")

        try:
            opt = int(input("Choose option: "))
            if opt == 1:
                emp_id = int(input("Enter ID: "))
                emp = self.employee_manager.search_by_id(emp_id)
                print(emp if emp else "Employee not found.")
            elif opt == 2:
                name = input("Enter Name: ")
                results = self.employee_manager.search_by_name(name)
                for emp in results:
                    print(emp)
            elif opt == 3:
                dept = input("Enter Department: ")
                results = self.employee_manager.search_by_department(dept)
                for emp in results:
                    print(emp)
            elif opt == 4:
                min_s = float(input("Enter Min Salary: "))
                max_s = float(input("Enter Max Salary: "))
                results = self.employee_manager.search_by_salary_range(
                    min_s, max_s
                )
                for emp in results:
                    print(emp)
        except ValueError:
            print("Invalid input!")

    def update_employee_ui(self):
        try:
            emp_id = int(input("Enter Employee ID to update: "))
            emp = self.employee_manager.search_by_id(emp_id)
            if emp is None:
                print("Employee ID not found!")
                return

            print("Enter new data (Leave blank to keep old value):")
            new_name = input(f"New Name [{emp.name}]: ").strip()
            if new_name != "":
                emp.name = new_name

            new_sal = input(f"New Salary [{emp.salary}]: ").strip()
            if new_sal != "":
                emp.salary = float(new_sal)

            new_dept = input(f"New Department [{emp.department}]: ").strip()
            if new_dept != "":
                emp.department = new_dept

            print("Employee updated successfully!")
        except ValueError:
            print("Invalid number input!")

    def sort_employees_ui(self):
        print("\n--- Sort Options ---")
        print("1) Sort by Name")
        print("2) Sort by Age")
        print("3) Sort by Salary")
        try:
            opt = int(input("Choose field (1-3): "))
            order = int(input("1) Ascending  2) Descending: "))
            is_reverse = order == 2

            sorted_list = self.employee_manager.get_sorted_employees(
                opt, is_reverse
            )
            for emp in sorted_list:
                print(emp)
        except ValueError:
            print("Invalid input!")


if __name__ == "__main__":
    app = FrontEndManager()
    app.run()