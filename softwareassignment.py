class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []
        
    def add_employee(self, emp):
        self.employees.append(emp)
        
    def sort_table(self, key):
        if key == 1:
            self.employees.sort(key=lambda emp: emp.age)
        elif key == 2:
            self.employees.sort(key=lambda emp: emp.name)
        elif key == 3:
            self.employees.sort(key=lambda emp: emp.salary)
        else:
            print("Invalid sorting key")
        
    def print_table(self):
        for emp in self.employees:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")

def main():
    emp_table = EmployeeTable()
    
    emp_table.add_employee(Employee("161E90", "Raman", 41, 56000))
    emp_table.add_employee(Employee("161F91", "Himadri", 38, 67500))
    emp_table.add_employee(Employee("161F99", "Jaya", 51, 82100))
    emp_table.add_employee(Employee("171E20", "Tejas", 30, 55000))
    emp_table.add_employee(Employee("171G30", "Ajay", 45, 44000))
    
    print("Choose sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    
    sorting_key = int(input())
    emp_table.sort_table(sorting_key)
    
    print("\nSorted Employee Table:")
    emp_table.print_table()

if __name__ == "__main__":
    main()
