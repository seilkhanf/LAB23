class account:
    def __init__(self,owner, balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,add):
        self.add=self.balance+add 
        print("Balance" ,self.owner,": ", self.add)
    def withdraw(self,minimum):
        self.minimum=minimum
        if minimum>self.balance:
            print("not money")
        else:
            self.balance=self.add-minimum
            print("Balance",self.owner," :", self.balance)


x=account('Turkey',4200)
x.deposit(2000)
x.withdraw(5700)

y=account('Almas',8500)
y.deposit(950)
y.withdraw(1200)
y.withdraw(3000)