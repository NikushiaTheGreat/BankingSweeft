from datetime import datetime
import uuid

TRANSACTIONS = []


class Customer:
    def __init__(self, name: str, email: str):
        self.customer_id = uuid.uuid4()
        self.name = name
        self.email = email


class Account:
    def __init__(self, balance: float, customer: Customer):
        self.account_id = uuid.uuid4()
        self.__balance = balance
        self.customer = customer

    @property
    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if self.__balance < amount:
            return "fuli araa dzmao"
        self.__balance -= amount
        return self.__balance


class SavingsAccount(Account):
    def __init__(self, balance: float, customer: Customer, interest_rate: float):
        super().__init__(balance, customer)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.__balance += amount * self.interest_rate
        return self.__balance


class Transaction:
    def __init__(self, amount: float,
                 source_account: Account,
                 destination_account: Account):

        self.transaction_id = uuid.uuid4()
        self.amount = amount
        self.source_account = source_account
        self.destination_account = destination_account
        self.timestamp = datetime.now()


def process_transaction(transaction: Transaction):
    amount = transaction.amount
    source_account = transaction.source_account
    destination_account = transaction.destination_account

    source_account.withdraw(amount)
    destination_account.deposit(amount)

    TRANSACTIONS.append(transaction)



