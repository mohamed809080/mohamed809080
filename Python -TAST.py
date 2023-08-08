#####################################################
## Create a class that represents a bank account. ##
#####################################################
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append({'type': 'deposit', 'amount': amount})

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return
        self.balance -= amount
        self.transactions.append({'type': 'withdrawal', 'amount': amount})

    def get_balance(self):
        return self.balance

    

#####################################################
## Create a class that represents a shopping cart. ##
#####################################################

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item['name'] != item_name]

    def get_total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.items)


bc=BankAccount(500)
print(f"my balance is{bc.balance}")
bc.withdraw(600)
print(f"my balance is{bc.balance}")

