class Project:
    def __init__(self, title, price):
        self.title = title
        self.price = price
        self.completed = False

    def complete(self):
        self.completed = True


class Client:
    def __init__(self, name):
        self.name = name
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)