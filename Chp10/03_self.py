class Employee:
    language = "Python" # This is a class attribute
    salary = "1200000"

    def getInfo(self):
        print(f"The language is {self.language}, The salary is {self.salary}")

    def greet(self):
        print("Good morning")

rituraj = Employee()
#rituraj.language = "JavaScript" # This is an instance attribute
rituraj.getInfo()
rituraj.greet()
#Employee.getInfo(rituraj)