class Employee():
  def __init__(self,empname,empid,job,salary,dept):
    self.empname=empname
    self.empid=empid
    self.job=job
    self.salary=salary
    self.dept=dept
  print('Employee object is created....!')
def details(self):
  print(f"empname is {self.empname}")
  print(f"empid is {self.empid}")
  print(f"job is {self.job}")
  print(f"salary is {self.salary}")
  print(f"dept is {self.dept}")
e1=Employee('prams',1,'manager',20000,'AI')
details(e1)