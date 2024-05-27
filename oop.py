class Account:
    def __init__ (self, pin, number, user_name, user_address, minimum_balance=0):
        self.__pin = pin
        self.number = number
        self.__balance = 0
        self.user_name = user_name
        self.user_address = user_address
        self.transactions = []
        self.__overdraft_limit = 0
        self.__interest_rate = 0
        self.__is_frozen = False
        self.__minimum_balance = minimum_balance

    def show_balance(self, pin):
        if pin == self.__pin:
            return self.__balance
        else:
            return "Wrong pin"
        Balance

    def show_balance(self, pin):
        if pin == self.__pin:
            if self.__is_frozen:
                return "Account is frozen"
            return self.__balance
        else:
            return "Wrong pin"

    def view_account_details(self, pin):
        if pin == self.__pin:
            return {
                "Account Number": self.number,
                "User Name": self.user_name,
                "User Address": self.user_address,
                "Balance": self.__balance,
                "Frozen": self.__is_frozen
            }
        else:
            return "Wrong pin"

    def change_user(self, pin, new_user_name, new_user_address):
        if pin == self.__pin:
            self.user_name = new_user_name
            self.user_address = new_user_address
            return "Owner details updated successfully"
        else:
            return "Wrong pin"

    def deposit(self, amount):
        if self.__is_frozen:
            return "Account is frozen"
        self.__balance += amount
        self.transactions.append({
            "type": "Deposit",
            "amount": amount,
            "date": datetime.datetime.now()
        })
        return "Deposit successful"

    def withdraw(self, amount, pin):
        if pin == self.__pin:
            if self.__is_frozen:
                return "Account is frozen"
            if self.__balance + self.__overdraft_limit - amount >= self.__minimum_balance:
                self.__balance -= amount
                self.transactions.append({
                    "type": "Withdrawal",
                    "amount": amount,
                    "date": datetime.datetime.now()
                })
                return "Withdrawal successful"
            else:
                return f"Withdrawal failed: Minimum balance requirement not met. Minimum balance: {self.__minimum_balance}"
        else:
            return "Wrong pin"

    def account_statement(self, pin):
        if pin == self.__pin:
            return {
                "Account Number": self.number,
                "Owner Name": self.user_name,
                "Balance": self.__balance,
                "Transactions": self.transactions,
                "Frozen": self.__is_frozen
            }
        else:
            return "Wrong pin"

    def set_overdraft_limit(self, pin, limit):
        if pin == self.__pin:
            self.__overdraft_limit = limit
            return "Overdraft limit set successfully"
        else:
            return "Wrong pin"

    def set_interest_rate(self, pin, rate):
        if pin == self.__pin:
            self.__interest_rate = rate
            return "Interest rate set successfully"
        else:
            return "Wrong pin"

    def calculate_interest(self, pin, months):
        if pin == self.__pin:
            interest = self.__balance * (self.__interest_rate / 100) * months
            return interest
        else:
            return "Wrong pin"

    def apply_interest(self, pin, months):
        if pin == self.__pin:
            interest = self.calculate_interest(pin, months)
            self.__balance += interest
            self.transactions.append({
                "type": "Interest",
                "amount": interest,
                "date": datetime.datetime.now()
            })
            return "Interest applied successfully"
        else:
            return "Wrong pin"

    def freeze_account(self, pin):
        if pin == self.__pin:
            self.__is_frozen = True
            return "Account frozen successfully"
        else:
            return "Wrong pin"

    def unfreeze_account(self, pin):
        if pin == self.__pin:
            self.__is_frozen = False
            return "Account unfrozen successfully"
        else:
            return "Wrong pin"

    def transaction_history(self, pin):
        if pin == self.__pin:
            return self.transactions
        else:
            return "Wrong pin"

    def set_minimum_balance(self, pin, minimum_balance):
        if pin == self.__pin:
            self.__minimum_balance = minimum_balance
            return f"Minimum balance set to {minimum_balance}"
        else:
            return "Wrong pin"

    def close_account(self, pin):
        if pin == self.__pin:
            self.__balance = 0
            self.__is_frozen = True
            return "Account closed successfully"
        else:
            return "Wrong pin"

account = Account(number="0712345678", pin="4568", owner_name="Alice John", owner_address="245-savannah")

result = account.close_account(pin="1234")

result = account.close_account(pin="0000")
print(result)