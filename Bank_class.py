class Bank_account():
    def __init__(self,account_holder_name,balance,account_number):
        self.account_holder_name = account_holder_name
        self.balance = balance
        self.account_number = account_number

    def display(self):
        print(self.account_holder_name,self.balance,self.account_number)
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print("insufficient balance.")
    def deposit(self,amount):
        self.balance = self.balance + amount
    def get_balance(self):
        print(self.balance)

account1 = Bank_account("Darren",7500,"41563572851")
print('''option1: Withdraw
option2: Deposit
option3: Get Balance
option4: Display account details
option5: exit''')

while True:
    option = input("which option do you want?" )
    if option == "1":
        withdrawal_amount = int(input("how much do you want to withdraw?" ))
        account1.withdraw(withdrawal_amount)
    elif option == "2":
        deposition_amount = int(input("how much do you want to deposit?" ))
        account1.deposit(deposition_amount)
    elif option == "3":
        account1.get_balance()
    elif option == "4":
        account1.display()
    else:
        break


