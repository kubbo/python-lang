"""this is person class"""
class Person:
    name = ""

    def __init__(self, name):
        self.name = name


    def __del__(self):

        print("del")


    def hi(self):
        print("hi %s" % self.name)

class Student(Person):
    grade=0
    def __init__(self,name,grade):
        Person.__init__(self,name)
        self.grade = grade


    def hi(self):
        print("I'm %s,in grade %s" %(self.name,self.grade))

person = Person("netty")
person.hi()
print(person.__doc__)

student = Student("zhuwei",10)
student.hi()
