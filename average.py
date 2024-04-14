class Student: #making the class
    def __init__(self,name,physics,chemistry,math):  #defining the constructor
        self.name = name 
        self.physics = physics
        self.chemistry = chemistry
        self.math = math


    def result(self):  #defining the function average 
        avg = (self.physics+self.chemistry+self.math)/3
        return self .name+ "| " + str(self.physics) +"   |   "+ str(self.chemistry) +"   |   " + str(self.math) + "   |   " +str(avg)

number_of_students =int(input("Enter the number of students: "))
for i in range(number_of_students):
    name = input("Enter the name of student: ")
    physics = int(input("Enter the physics marks: "))
    chemistry  = int(input("Enter the chemistry marks: "))
    math = int(input("Enter the math marks: "))
    s_1 = Student(name,physics,chemistry,math)
    if i ==0:
        print("Name | Pysics | Chemistry | Math | Average ")
    print(s_1.result())
                   