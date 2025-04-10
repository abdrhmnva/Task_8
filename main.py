from employee import Employee
from employee_dao import EmployeeDAO

def main():
    dao = EmployeeDAO()

    # Insert multiple employees
    employees = [
        Employee(name="Alice Smith", position="Software Engineer", salary=80000.0, hire_date="2023-06-15"),
        Employee(name="Bob Johnson", position="Data Analyst", salary=70000.0, hire_date="2022-09-01"),
        Employee(name="Carol White", position="Project Manager", salary=90000.0, hire_date="2021-04-10"),
        Employee(name="David Lee", position="DevOps Engineer", salary=85000.0, hire_date="2020-12-20"),
        Employee(name="Eve Brown", position="UI/UX Designer", salary=75000.0, hire_date="2023-01-05"),
        Employee(name="Frank Green", position="Product Owner", salary=95000.0, hire_date="2019-07-17"),
    ]

    for emp in employees:
        dao.insert(emp)

    # View all employees
    print("\n📋 All Employees:")
    for e in dao.get_all():
        print(e)

if __name__ == "__main__":
    main()
