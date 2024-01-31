#Shiven, Jay Lebo, Alec, Andrew, Jay Patel
class BankAccount:
    def __init__(user,account_name, starting_balance):
        user.account_name = account_name
        user.balance = starting_balance

    def deposit(user, amount):
        user.balance += amount

    def withdraw(user,amount):
        user.balance -= amount

    def get_balance(user):
        return f"{user.account_name} has a balnce of {user.balance}"
    

    
            

        