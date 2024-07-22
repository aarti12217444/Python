#5.Write a Python function student_data () that will print the ID of a student (student_id). 
# If the user passes an argument student_name or student_class the function will print the student name and class.


class Student:
    def __init__(self,id,name=None,class1=None):
        self.id = id
        self.name = name
        self.class1=class1
    def student_data(self):
        print("id: ",self.id)
        if self.name:
            print("name:",self.name)
        if self.class1:
            print("class:",self.class1)


s3=Student(12217444,"Aarti","Btech")
s3.student_data()