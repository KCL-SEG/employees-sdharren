"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, pay, commission = 0, commission_type = None, hours = 1, num_of_contracts = 1):
        self.name = name

        self.contract = contract
        self.pay = pay
        self.hours = hours

        self.commission_type = commission_type
        self.commission = commission
        self.num_of_contracts = num_of_contracts

    def get_pay(self):
        return self.hours * self.pay + (self.commission * self.num_of_contracts)

    def __str__(self):
        if self.contract == "salary":
            pay_desc = f'{self.name} works on a monthly salary of {self.pay}'
        elif self.contract == "hourly":
            pay_desc = f'{self.name} works on a contract of {self.hours} hours at {self.pay}/hour'

        if self.commission_type == "bonus":
            comm_desc = f' and receives a bonus commission of {self.commission}.'
        elif self.commission_type == "rate":
            comm_desc = f' and receives a commission of {self.num_of_contracts} contract(s) at {self.commission}/contract.'
        else:
            comm_desc = "."

        return pay_desc + comm_desc + f' Their total pay is {self.get_pay()}.'


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', contract="salary", pay=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', contract="hourly", pay=25, hours=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', contract="salary", pay=3000, commission_type="rate", commission=200, num_of_contracts=4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', contract="hourly", pay=25, hours=150, commission_type="rate", commission=220, num_of_contracts=3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', contract="salary", pay=2000, commission_type="bonus", commission=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', contract="hourly", pay=30, hours=120, commission_type="bonus", commission=600)
