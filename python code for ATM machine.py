import time as t
class ATM:
    def __init__(self,pin,user_balance,saving_balance):
        self.pin=pin
        self.user_balance=user_balance
        self.saving_balance=saving_balance

    def display_balance(self):
        print("Your current account balance is", self.user_balance)

    def authenticate_login(self,pin_entered):
        if(self.pin==pin_entered):
            return True
        return False
    
    def withdraw_amount(self,amount):
        if(amount>self.user_balance):
            print("Insufficient account Balance!!")
            return
        self.user_balance-=amount
        print("Your account is debited with Rs.",amount)
        t.sleep(2)
        print("Remaining Balance: ",self.user_balance)

    def deposit_funds(self,amount):
        self.user_balance+=amount
        print("Your account is credited with Rs.",amount)
        print("Account balance:", self.user_balance)

    def transfer_funds(self,amount):
        if(amount>self.user_balance):
            print("Insufficient account Balance!!")
            return
        print("Transferring amount.....")
        t.sleep(2)
        self.user_balance-=amount
        self.saving_balance+=amount
        print("Amount transferred..")
        t.sleep(2)
        print("Your saving account balance is credited with Rs.",saving_balance)
        print("Your current account balance is debited with Rs.",user_balance)

pin=1234
user_balance=50000
saving_balance=70000
print("Welcome back to your account")
print("****************************")
t.sleep(2)
choice=0
use=ATM(pin,user_balance,saving_balance)
n = int(input("Enter your 4-digit pin:"))
n1= int(input("Enter your 4-digit pin again:"))
if(n==n1):
    if(use.authenticate_login(n)):
        print("Verifying your account...")
        t.sleep(1)
        print("*************************")
        print("Account verified...")
        t.sleep(0.5)
        while(True):
            print("Enter your choice below:(1-4)")
            print("1. Check account balance")
            print("2. Deposit amount")
            print("3. Withdraw amount")
            print("4. Transfer funds to savings balance")
            choice=int(input("Enter your choice:"))
            if choice in(1,2,3,4):
                    if(choice==1):
                        use.display_balance()
                        break
                    if(choice==2):
                        a=int(input("Enter amount you want to deposit: "))
                        use.deposit_funds(a)
                        break
                    if(choice==3):
                        a=int(input("Enter amount you want to withdraw: "))
                        use.withdraw_amount(a)
                        break
                    if(choice==4):
                        a=int(input("enter amount you transfer to savings balance: "))
                        use.transfer_funds(a)
                        break
                    else:
                        print("Invalid choice!!")
                        break
                        
            else:
                print("Invalid choice... Try again")
            
else:
    print("Your pin doesn't match... Try again!!")
    
    
