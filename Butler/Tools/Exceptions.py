class OpenException(Exception):
    problem = ""
    
    def __init__(self, problem: str):
        self.problem = problem
        
class OpenCancellation(Exception):
    statement = ""
    
    def __init__(self, statement: str):
        self.statement = statement
        
