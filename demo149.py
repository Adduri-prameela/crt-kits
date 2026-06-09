'''
Encapsulation : It wraps up states & behaviours of entity in a single container & accessing using public data  handler methods

'''
class BankAccount:
    def __init__(self,name,acc_no,pin):
        self.__name=name
        self.__acc_no=acc_no
        self.__pin=pin
        print('Bank Account is created')
    def get_name(self):
        print(self.__name)
    def get_accno(self):
        print(self.__acc_no)
    def get_pin(self):
        print(self.__pin)
b1=BankAccount('Scott',1234567890,1234)
b1.get_name()
b1.get_accno()
b1.get_pin()