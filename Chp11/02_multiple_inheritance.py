class Employee:
    company = "ITC"
    name = "Defualt name"
    def show(self):
        print(f"The name of the employee is {self.name} and the compony is {self.salary}")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the language here is your language: {self.language}")

class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")

a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()