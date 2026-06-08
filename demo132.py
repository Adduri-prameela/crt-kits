class Student():
    def __init__(self,name,age):
        print("Student Object ic created...!")
        self.name=name
        self.age=age
def details(self):
    print("----------------")
    print("name is {self.name}")
    print(f"name is {self.age}")
s1=Student('prameela',21)
details(s1)
s2=Student('harsha',21)
details(s2)
s3=Student('keerthi',21)
details(s3)