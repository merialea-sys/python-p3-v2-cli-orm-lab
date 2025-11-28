from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name = input("Enter the employee's name:")
    employee = Employee.find_by_name(name)
    if employee:
        print(employee)
    else:
        print(f'Employee {name} not found')


def find_employee_by_id():
    id = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id)
    if employee:
        print(employee)
    else:
        print(f'Employee {id} not found')


def create_employee():
    new_employee_name = input("Enter the employee's name: ")
    new_employee_job_title = input("Enter the employee's job title: ")
    new_employee_department_id = input("Enter the employee's department id: ")
    try:
        employee = Employee.create(
            new_employee_name,
            new_employee_job_title,
            new_employee_department_id
        )
        print(f'Success: {employee}')
    except Exception as exc:
        print("Error creating employee: ", exc)
    

def update_employee():
    update_employee_id = input("Enter the employee's id: ")
    update_employee_name = input("Enter the employee's new name: ")
    update_employee_job_title = input("Enter the employee's new job title: ")
    update_employee_department_id = input("Enter the employee's new department id: ")
    try:
        employee = Employee.update(
            update_employee_id,
            update_employee_name,
            update_employee_job_title,
            update_employee_department_id
        )
        print(f'Success: {employee}')
    except Exception as exc:
        print("Error updating employee: ", exc)


def delete_employee():
    delete_employee_id = input("Enter the employee's id: ")
    try:
        Employee.delete(delete_employee_id)
        print(f'Employee {delete_employee_id} deleted')
    except Exception as exc:
        print("Error deleting employee: ", exc)


def list_department_employees():
    department_id = input("Enter the department's id: ")
    employees = Department.employees(department_id)
    if employees:
        for employee in employees:
            print(employee)
    else:
        print(f'No employees found for department {department_id}')
    