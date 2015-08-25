currentProblems = []

def reset():
    currentProblems.clear()

def report(message = "", forbidUnitCreation = False, forbidExecution = False):
    problem = Problem(message, forbidUnitCreation, forbidExecution)
    currentProblems.append(problem)

def canCreateExecutionUnits():
    for problem in currentProblems:
        if problem.forbidUnitCreation: return False
    return True

def canExecute():
    for problem in currentProblems:
        if problem.forbidExecution: return False
    return True

def getProblems():
    return currentProblems


class Problem:
    def __init__(self, message = "", forbidUnitCreation = False, forbidExecution = False):
        self.message = message
        self.forbidUnitCreation = forbidUnitCreation
        self.forbidExecution = forbidExecution



# Exceptions
########################################        

class ExecutionUnitNotSetup(Exception):
    pass

class NodeRecursionDetected(Exception):
    pass
