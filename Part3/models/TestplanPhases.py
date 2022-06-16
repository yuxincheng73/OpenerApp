class TestplanPhases:
    def __init__(self, data):
        self.testplanIds = data['testplanId']
        self.phases = data['phase']
        self.risks = data['risk']
        self.employeeIds = data['employeeId']
        self.isApproved = data['isApproved']
        self.approvedBy = data['approvedBy']