# warpping data and function into a single unit

class Account:
    def __init__(self, bal,aNo):
        self.bal=bal
        self.aNo=aNo

    def debit(self,amount):
        self.bal -= amount
        print("Rs", amount,"was debited")

    def cradit(self,amount):
        self.bal += amount
        print("Rs", amount,"was cradit")

    def get_balance(self):
        return self.bal


aNo=Account(10000,12345)
aNo.debit(10000)
aNo.cradit(200)
print(aNo.bal)
print(aNo.aNo)

        