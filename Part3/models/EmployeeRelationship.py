class EmployeeRelationship:
    def __init__(self, data):
        self.employeeIds = data['employeeId']
        self.managerIds = data['managerId']