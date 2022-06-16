class Employee:
    def __init__(self, data):
        self.employeeIds = data['employeeId']
        self.names = data['name']

    def add_employee(self, employee):
        self.employeeIds.append(employee.employeeId)
        self.names.append(employee.name)