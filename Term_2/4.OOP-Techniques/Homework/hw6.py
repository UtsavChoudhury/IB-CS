class Company():
    def __init__(self, name, projects):
        self.name = name
        self.projects = projects

    def __str__(self):
        projects_str = '\n'.join(str(x) for x in self.projects)
        return f'COMPANY NAME: {self.name}\nPROJECTS:\n{projects_str}'


class Project():
    def __init__(self, identifier, tasks):
        self.identifier = identifier
        self.tasks = tasks
    
    def __str__(self):
        tasks_str = '\n'.join(str(x) for x in self.tasks)
        return f'PROJECT IDENTIFIER: {self.identifier}\nTASKS:\n{tasks_str}'


class Task():
    def __init__(self, name, workers):
        self.name = name
        self.workers = workers
    
    def __str__(self):
        workers_str = '\n'.join(str(x) for x in self.workers) # Without str() it will print its location in memory without its actual string representation.
        return f'TASK: {self.name}\nWORKERS:\n{workers_str}'


class Worker():
    def __init__(self, name, employee):
        self.name = name
        self.employee_status = employee
    
    def __str__(self):
        if self.employee_status:
            status = 'Employee'
        else:
            status = 'Hired-Contractor'
        return f'WORKER NAME: {self.name}\n - STATUS: {status}'


Alice = Worker('Alice', True)
Bob = Worker('Bob', False)

Research = Task('Research', [Alice])
Training = Task('Training', [Bob])

GPT6 = Project(6, [Research, Training])

OpenAI = Company('OpenAI', [GPT6])

print(OpenAI)
