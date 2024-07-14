class Person():
    def setname(self,name):
        self.name = name
        def getname(self):
            print(self.name)

class Student(Person):
    def setage(self,age):
        self.age=age
        def getage(self):
            print(self.age)

s = Student()
s_name = input("Name is: ")
s.setname(s_name)

s_age = int(input("age is: "))
s.setage(s_age)

print("The student name is:",s_name)
print("The student age is:",s_age)


class House:
    h = "10ft"
    w = "70ack"
    def display_h(self):
        print("The height of this house is: ",self.h)

    def display_w(self):
        print("The width of this house is: ",self.w)

h = House()
h.display_h()
h.display_w()

# create a class person with say_hello method in which a person introduce him self and create a constructor under it and init name and age.
# create another class student which is derived from person in which a student introduce him self and create a constructor under it and init name,grade and age.And display it

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say_hello(self):
        print(f"Radhe Radhe, My self {self.name} any age is {self.age}")

class Student(Person):
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade

    def say_hello(self):
        print(f"Radhe Radhe, My self {self.name} any age is {self.age} and i got {self.grade} grade in my  university")

p=Person("Karan",80)
p.say_hello()

s = Student("Arjun",19,90)
s.say_hello()
        

#  multiple inheritance

# create a class Parent1 with method intro and print intro sane as with Parent2 and Parent3 then create a child class which is inherite from all parent class and same make a method with intro ..then create an obj and display all parent class and child also

class Parent1:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def intro1(self):
        print(f"Hlo i am his father and my name is {self.name} my age is {self.age} i currently stay here {self.address}")

class Parent2:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def intro2(self):
        print(f"Hlo i am his mother and my name is {self.name} my age is {self.age} i currently stay here {self.address}")

class Parent3:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def intro3(self):
        print(f"Hlo i am his grandparent and my name is {self.name} my age is {self.age} i currently stay here {self.address}")

class Child(Parent1,Parent2,Parent3):
     def __init__(self,name,age,address,grade):
        self.name=name
        self.age=age
        self.address=address
        self.grade=grade
     def intro4(self):
        print(f"Hlo  my name is {self.name} my age is {self.age} i currently stay here {self.address} and my grade is {self.grade}")

p1=Parent1("karan",45,"patna bihar")
p1.intro1()
p2=Parent2("Arya",40,"Patna,bihar")
p2.intro2()
p3=Parent3("Arjun",70,"Barh")
p3.intro3()
c = Child("AK",19,"Patna bihar","O")
c.intro4()

        
# multilevel inheritance
# create a class grandparent with func1 method and print hello grandparentthen create another class parent inherta from grandparent with func2 and print hello parent create another class child enherit from parent and print hello child and display it.

class GrandParent:
    def func1(self):
        print("Hello grandparent")
class Parent(GrandParent):
    def func2(self):
        print("Hello parent")
class Child(Parent):
    def func3(self):
        print("Hello child")
c=Child()
c.func1()
c.func2()
c.func3()


# hierarchical inheritance example
 
class parent:                       
    def func1(self):                   
        print("Hello Parent")
 
class child1(parent):               
    def func2(self):                   
        print("Hello Child1")
 
 
class child2(parent):               
    def func3(self):                   
        print("Hello Child2")   
                               
 
# Driver Code
test1 = child1()                     
test2 = child2() 
 
test1.func1()                       
test1.func2()
 
test2.func1()                       
test2.func3()       



# hybrid inheritance example
 
class parent1:
    def func1(self):                   
        print(" Parent1")
 
 
class parent2:
    def func2(self):                   
        print("hi Parent2")
 
class child1(parent1):                    
    def func3(self):                   
        print(" Child1")
 
 
class child2(child1, parent2):            
    def func4(self):                   
        print("hi Child2")   
                               
 
# Driver Code
test1 = child1()                         
test2 = child2()
 
test1.func1()
test1.func3()                      
 
test2.func1()                      
test2.func2()                       
test2.func3()                       
test2.func4()                      
