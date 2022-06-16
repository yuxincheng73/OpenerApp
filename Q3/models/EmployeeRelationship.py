class EmployeeRelationship:
    def __init__(self, data):
        self.employeeIds = data['employeeId']
        self.managerIds = data['managerId']

    def add_employee_manager_relationship(self, employeeId, managerId):
        self.employeeIds.append(employeeId)
        self.managerIds.append(managerId)