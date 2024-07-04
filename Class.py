class Greeding:
    def sayhello(self, name=None,  wish=None):
        if name is not None and wish is not None:
                print("Hello",name+" "+wish)
        elif name is not None and wish is None:
                print("hello")
        else:
              print("hi")

g = Greeding()
g.sayhello()



class Student:
      name="Aarti"

s1=Student()
print(s1.name)



class Car:
      color = "blue"
      brand= "XYZ"
c=Car()
print(c.color)
print(c.brand)


class Student:
      name="Miss kashyap"
      def __init__(self):
            print("adding new student in database")
s1=Student()
print(s1.name)

class Student:

      def __init__(self,fullname):
            self.name=fullname
            print("adding new student in database")
s1=Student("Muskan")
print(s1.name)
s2=Student("Arjun")
print(s2.name)