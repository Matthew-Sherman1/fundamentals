class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def make_withdrawl(self,amount):
        self.balance -= amount
        return self
    def display_user_balance(self):
        print('User:'+self.name+',Balance:',self.balance)
        return self
    def transfer_money(self,other_user,amount):
        self.make_withdrawl(amount)
        # subtracts amount from the person transferrings account
        other_user.balance += amount
        # adds this amount to the account of the person recieving the money 
        return self
    
# user 1
p1 = User('Matt', 5000)
# user 2
p2 = User('Mike', 2000)
# user 3
p3 = User('Sherm',10000)
p1.make_withdrawl(500).transfer_money(p3,1000).display_user_balance()
# user 1 withdrawls 500 and transfers 1000 to user 3 then the balance is displayed
p2.make_withdrawl(500).transfer_money(p3,1000).display_user_balance()
# user 2 withdrawls 500 and transfers 1000 to user 3 then the balance is displayed
p3.make_withdrawl(500).display_user_balance()





# p1.make_withdrawl(500).transfer_money(p2,700).display_user_balance()
# p3.make_withdrawl(0).transfer_money(p2,5000).display_user_balance()

