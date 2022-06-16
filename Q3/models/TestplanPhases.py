class TestplanPhases:
    def __init__(self, data):
        self.testplanIds = data['testplanId']
        self.phases = data['phase']
        self.risks = data['risk']
        self.employeeIds = data['employeeId']
        self.isApproved = data['isApproved']
        self.approvedBy = data['approvedBy']

    def add_testplan_phase(self, testplan):
        self.testplanIds.append(testplan.testplanId)
        self.phases.append(testplan.phase)
        self.risks.append(testplan.risk)
        self.employeeIds.append(testplan.employeeId)
        self.isApproved.append(testplan.isApproved)
        self.approvedBy.append(testplan.approvedBy)