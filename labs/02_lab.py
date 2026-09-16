# Artificial Intelligence
# Lab 2

# 1. Simple Reflex Agent
threshold = 30.0

def perceiveTemperature():
    t= input('Enter the temperature:')
    t = float(t)  

    return t

def perceiveLight():
    l = input('Enter the level of light:')

    return l.lower()

def model():
    t = perceiveTemperature()

    if(t > threshold):
        print('Fan ON')
    else:
        print('Fan OFF')

    l = perceiveLight()

    if(l == 'low'):
        print('Light ON')
    else:
        print('Light OFF')

model()

# Struct variables are always public while Class variables are always private

# 2. Create an instance of class and display the namespace
class Student:

    def __init__(self, name= None, regno= None, age=None, gender=None):
        self.name = name
        self.regno = regno
        self.age = age
        self.gender = gender

    def showNamespace(self):
        print(Student.__dict__)

# 3. Write __student__data() - prints student_id, and name/class if given
    def student__data(self):
        print('Name:', self.name)
        print('Reg#:', self.regno)

# 4. Show a Student class's type, __dict__keys, and __module__
s1 = Student('Ali', 16, 43, 'Male')

print(s1.__class__)
print(Student.__module__)
print(Student.__dict__)
print(s1.__dict__)

# 5. Create empty students and mark classes: test instanceof/subclass
s2 = Student()
s3 = Student()

class Marks(Student):
    pass

m1 = Marks(s2)
m2 = Marks(s3)

# 6. Modify attribute values and print before and after
print('Before(name):', s1.name)
s1.name = 'Usman'
print('After(name):', s1.name)

# 7. Add a student_class attribute, then remove stduent_name
s1.student_class = "BSCS"
del s1.name
print(s1.student_class)

# 8. Write a function that displays all the attributes of a student
def printData(s):
    print(s.__dict__)

printData(s1)

# 9. Create student4 and student5 instances and print in the given format
s4 = Student('Akif', 16, 43, 'Male')
s5 = Student('Ram', 11, 32, 'Male')

s4.student__data()
s5.student__data()
