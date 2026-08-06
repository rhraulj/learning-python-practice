class Employee:
    laguage = "Py" # This is class attribute
    salary = 1200000

rituraj = Employee()
rituraj.name = "Rituraj" # This ia an instant attribute
print(rituraj.name,rituraj.laguage , rituraj.salary) 

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name,rohan.salary, rohan.laguage)

#Here name is instant attribute and salary and laguage are class attribute as they directly as they 
# directly belong to the class 