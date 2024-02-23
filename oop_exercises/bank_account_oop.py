

class BankAccount:
    admin_password = '1234'
    accounts = {}
    commision_rate = 0.05
    
    def __init__(self, id, owner_name, initial_balance=0):
        self.id = id
        self.owner_name = owner_name
        self.balance = initial_balance
        self.transactions = []
        self.accounts[id] = self
        
    @classmethod
    def create_account(cls, id, owner_name, initial_balance=0):
        return cls(id, owner_name, initial_balance)
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f'Deposit: +{amount}')
    
        
    def widthdraw(self, amount):
        commision = amount * BankAccount.commision_rate
        total_widthdrawal = amount + commision
        if total_widthdrawal <= self.balance:
            self.balance -= total_widthdrawal
            self.transactions.append(f'Widthdrawal: -{total_widthdrawal} includes {commision} commision')
        else:
            print(f'Insufficient funds for the operation, your balance is {self.balance}, when you need {amount}')
            self.transactions.append(f'Widthdrawal attempt: -{total_widthdrawal} includes {commision} commision')
    
    def dump(self):
        print("/-\\"* 20)
        print(f'Your identification number is: {self.id}')
        print(f'Your name is: {self.owner_name}')
        print(f'Your balance is: {self.balance}')
        print("Transaction history:")
        for transaction in self.transactions:
            print(transaction)
            
    def __str__(self):
        return f'{self.owner_name}, balance is {self.balance}, identification number is {self.id}'
    


def main():
    print('Welcome to the Leumi bank!')
    while True:
        print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Display Account Info\n5. Forgot Account ID\n6. Exit.\n7. All accounts data(only for admins)")
        choice = input("Enter your choice: ")
        if choice == "1":
            id = input("What's your id number?(teudat zeut) ")
            owner_name = input("What's your name? ")
            initial_balance = float(input("What's your balance? "))
            account = BankAccount.create_account(id, owner_name, initial_balance)
            print("Account created successfully.")
            
        elif choice == "2":
            id = input("Enter your id number: ")
            amount = float(input("Enter deposit amount: "))
            account = BankAccount.accounts.get(id)
            if account:
                account.deposit(amount)
                print("Deposit successful!")
            else:
                print("Account not found.")            
            
        elif choice == "3":
            id = input("Enter your id number: ")
            amount = float(input("Enter widthdraw amount: "))
            account = BankAccount.accounts.get(id)
            if account:
                account.widthdraw(amount)
                print("Withdrawal successful!")
            else:
                print("Account not found")
                
        elif choice == "4":
            id = input('Enter your account number: ')
            account = BankAccount.accounts.get(id)
            if account:
                account.dump()
            else:
                print("Account not found.")
                
        elif choice == "5":
            owner_name = input("Enter your name to retrieve account ID: ")
            found = False
            for id, account in BankAccount.accounts.items():
                if account.owner_name == owner_name:
                    print(f"Account ID: {id}")  
                    found = True
                    break
            if not found:
                print("Account not found for the provided name")
        
        elif choice == "6":
            print('Thank you for using Leumi bank, your payment for exiting the bank is 5000 shekel hadash.')
            break
            
        elif choice == "7":
            attempt = input('Write down admin password: ')
            if attempt == BankAccount.admin_password:
                print('All created accounts:')
                for account in BankAccount.accounts.values():
                    print(account)
            else:
                print("Access denied. Look for password.")
            
        else:
            print('Invalid choice. Your account was debited for additional 50 shekel hadash for excessive use. Try again.')


if __name__ == "__main__":
    main()