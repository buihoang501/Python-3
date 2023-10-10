work_hours = [('John', 300), ('Neka', 500), ('Jire', 700)]


def employee_check(work_hours):
    max_hours = 0
    employee_of_month = ''
    for name, hours in work_hours:
        if hours > max_hours:
            max_hours = hours
            employee_of_month = name
        else:
            pass
    return {employee_of_month, max_hours}


name, hours = employee_check(work_hours)
print(name, hours)
