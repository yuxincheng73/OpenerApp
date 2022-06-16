class Testplan:
    def __init__(self, data) -> None:
        self.testplanIds = data['testplanId']
        self.testplanNames = data['testplanName']

    def add_testplan(self, testplan):
        self.testplanIds.append(testplan.testplanId)
        self.testplanNames.append(testplan.testplanName)