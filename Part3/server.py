from models.Employee import Employee
from models.EmployeeRelationship import EmployeeRelationship
from models.Testplan import Testplan
from models.TestplanPhases import TestplanPhases
import json

"""
Seed data
"""
testplan_data = {"testplanId": [1, 2, 3, 4], "testplanName": ["first test name", "second test name", "third test name", "fourth test name"]}
testplan_phase_data = {
    "testplanId": [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4], 
    "phase": ["A", "B", "C", "A", "B", "C", "A", "B", "C", "D", "E", "A"], 
    "risk": ["L", "M", "H", "M", "H", "M", "M", "L", "M", "H", "H", "M"], 
    "employeeId": [1, 1, 2, 1, 1, 2, 2, 3, 3, 1, 4, 6], 
    "isApproved": [True, True, False, True, True, False, True, True, True, False, False, True], 
    "approvedBy": [1, 2, None, 3, 5, None, 3, 3, 4, None, None, 7]
}
employee_data = {"employeeId": [1, 2, 3, 4, 5, 6, 7], "name": ["john", "kyle", "bob", "jane", "margot", "jake", "luna"]}
employee_relationship_data = {"employeeId": [1, 1, 2, 2, 3, 4, 5, 6], "managerId": [2, 3, 3, 4, 4, 5, 7, 7]}

"""
------------------------------------------------------------------------------------------------------------------------
Question 3 part c)
------------------------------------------------------------------------------------------------------------------------
"""
# Iterative Approach chosen over recursive to find upper-managers of a manager
def find_all_eligible_managers(employee_relationship_table, employeeId, risk):
    eligible_managers = []
    if risk == 'L':
        #return just the author/employee
        eligible_managers.append(employeeId)
    elif risk == 'M':
        #return direct managers
        direct_managers = [employee_relationship_table.managerIds[idx] for idx, elem in enumerate(employee_relationship_table.employeeIds) if elem == employeeId]
        eligible_managers = direct_managers
    else: 
        #return direct and indirect managers of author's direct managers
        direct_managers = [employee_relationship_table.managerIds[idx] for idx, elem in enumerate(employee_relationship_table.employeeIds) if elem == employeeId]
        set_direct_managers = set(direct_managers)
        managers = direct_managers
        #while there is a direct or indirect manager, check if there are more managers above to add
        while managers:
            manager = managers.pop(0)
            upper_direct_managers = [employee_relationship_table.managerIds[idx] for idx, elem in enumerate(employee_relationship_table.employeeIds) if elem == manager]
            upper_direct_managers = set(upper_direct_managers) - set_direct_managers
            for upper_direct_manager in upper_direct_managers:
                managers.append(upper_direct_manager)

            eligible_managers = eligible_managers + list(upper_direct_managers)
        #remove duplicates
        eligible_managers = list(set(eligible_managers))
    return eligible_managers

def prettyprint_testplan_phases(testplan_phase_table, employee_relationship_table, testplanId):
    #find the index where table.testplanId == testplanId
    indicies = [idx for idx, elem in enumerate(testplan_phase_table.testplanIds) if elem == testplanId]
    if indicies is None:
        return "Testplan does not exist"

    phases = {}
    eligible_managers = []
    for idx in indicies:
        #if unapproved, return all eligible managers
        if not testplan_phase_table.isApproved[idx]:
            eligible_managers = find_all_eligible_managers(employee_relationship_table, testplan_phase_table.employeeIds[idx], testplan_phase_table.risks[idx])
        #else if approved, return the approval manager
        else:
            eligible_managers = [testplan_phase_table.approvedBy[idx]]

        phases[testplan_phase_table.phases[idx]] = eligible_managers

    dic = {"Testplan": {"testplanId": testplanId, "phases": phases}}
    print(json.dumps(dic, indent=4))

"""
------------------------------------------------------------------------------------------------------------------------
Question 3 part d)
------------------------------------------------------------------------------------------------------------------------
"""
def approve_phase_testplan(testplan_phase_table, employee_relationship_table, testplanId, phase, approverId):
    #check whether this phase of this testplanId is unapproved first
    valid = False
    idx, employeeId, risk = None, None, None
    for index, (tpId, p, a) in enumerate(zip(testplan_phase_table.testplanIds, testplan_phase_table.phases, testplan_phase_table.isApproved)):
        if tpId == testplanId and p == phase and a == False:
            idx = index
            employeeId = testplan_phase_table.employeeIds[index]
            risk = testplan_phase_table.risks[index]
            valid = True
    if not valid:
        print("Either this testplan and phase don't exist or already approved.")

    # print(f"index: {idx}, employeeId: {employeeId}, risk: {risk}")
    #check if approverId is a valid approver, if so, approve
    eligible_approvers = find_all_eligible_managers(employee_relationship_table, employeeId, risk)
    if approverId in eligible_approvers:
        testplan_phase_table.isApproved[idx] = True
        testplan_phase_table.approvedBy[idx] = approverId
    else:
        print("ApproverId is not valid to approve this phase and testplan.")

"""
------------------------------------------------------------------------------------------------------------------------
Question 3 part e)
------------------------------------------------------------------------------------------------------------------------
"""
#Function to get the CEO node
def get_CEO(employee_relationship_table, employee_table):
    #CEO should be the only node in the graph that doesn't have any outgoing edges
    edges = []
    for e, m in zip(employee_relationship_table.employeeIds, employee_relationship_table.managerIds):
        edges.append((e,m))
    #get number of total employees
    num_employees = len(employee_table.employeeIds)
    #list to mark which nodes DO have outgoing edges, and thus, not the CEO
    mark = [0] * (num_employees+1)

    #begin marking the nodes for whether they have outgoing edges
    for i in range(len(edges)):
        mark[edges[i][0]] = 1

    #find the CEO
    for i in range(1, num_employees+1):
        if not mark[i]:
            #the only unmarked node must be the CEO
            return i

#BFS returns optimal solution for shortest path, unlike DFS
def shortest_path_to_CEO(employee_relationship_table, employee_table, employeeId):
    #get CEO node
    ceo = get_CEO(employee_relationship_table, employee_table)
    print(f"CEO is employee: {ceo}")
    #keep track of visited employees
    visited = {}
    queue = [[employeeId]]

    #start node is the CEO, return CEO
    if employeeId == ceo:
        print(f"Shortest path to CEO: {employeeId}")
        return employeeId

    while queue:
        path = queue.pop(0)
        #get last employee from path
        employee = path[-1]
        #found path to CEO
        if employee == ceo:
            print(f"Shortest path to CEO: {path}")
            return path

        #otherwise, check all other paths
        if employee not in visited:
            #add to visited employees
            visited[employee] = True
            #add direct managers to queue
            direct_managers = [employee_relationship_table.managerIds[idx] for idx, elem in enumerate(employee_relationship_table.employeeIds) if elem == employee]
            for direct_manager in direct_managers:
                newpath = list(path)
                newpath.append(direct_manager)
                queue.append(newpath)

    #no path was found to CEO
    return "No path was found to the CEO."

if __name__ == "__main__":
    #initialize tables
    employee_table = Employee(employee_data)
    employee_relationship_table = EmployeeRelationship(employee_relationship_data)
    testplan_table = Testplan(testplan_data)
    testplan_phase_table = TestplanPhases(testplan_phase_data)

    print("--------------------------------------------------------------------------------------------------")
    print("Question 3 part c")
    print("--------------------------------------------------------------------------------------------------")
    #pretty print a testplan and its phases
    testplanIdToTest = 1
    prettyprint_testplan_phases(testplan_phase_table, employee_relationship_table, testplanIdToTest)

    print("--------------------------------------------------------------------------------------------------")
    print("Question 3 part d")
    print("--------------------------------------------------------------------------------------------------")
    testplanIdToTest, phase, approverId = 3, 'D', 4
    print(f"TestplanPhase Table Before: {testplan_phase_table.approvedBy}")
    approve_phase_testplan(testplan_phase_table, employee_relationship_table, testplanIdToTest, phase, approverId)
    print(f"TestplanPhase Table After: {testplan_phase_table.approvedBy}")

    print("--------------------------------------------------------------------------------------------------")
    print("Question 3 part e")
    print("--------------------------------------------------------------------------------------------------")
    employeeId = 4
    shortest_path_to_CEO(employee_relationship_table, employee_table, employeeId)