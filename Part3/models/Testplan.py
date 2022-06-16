class Testplan:
    def __init__(self, data) -> None:
        self.testplanIds = data['testplanId']
        self.testplanNames = data['testplanName']

    def get_testplans(self):
        pass