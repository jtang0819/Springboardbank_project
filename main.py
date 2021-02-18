import pandas as pd
import csv


class Customer:
    def __init__(self, firstname, lastname, address):
        """Takes firstname, lastname, address from initialization to create line in customer_information.csv
        also checks for user_id existence, default is 1000, iterate + 1"""
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        data = pd.read_csv('customer_information.csv')
        if len(data) > 0:
            user_id = max(data['user_id']) + 1
        else:
            user_id = 1000
        self.userid = user_id
        append_this = [self.firstname, self.lastname, self.address, self.userid]
        with open('customer_information.csv', 'a', newline='') as f:
            wr = csv.writer(f, dialect='excel')
            wr.writerow(append_this)
        print(self.userid)

    def user_number(self):
        return self.userid


class BankAccount:
    def __init__(self, account_type, user_id):
        """ BankAccount creates bank account in account_information.csv with:
        accountnumber default at 1000000, iterate +1"""
        self.balance_amt = 0
        self.account_type = account_type
        data = pd.read_csv('account_information.csv')
        currentmax = len(data['accountnumber'])
        if currentmax > 0:
            accountnumber = max(data['accountnumber']) + 1
        else:
            accountnumber = 1000000
        self.account_number = accountnumber
        self.userid = user_id
        append_this = [self.account_number, self.account_type, self.balance_amt, self.userid]
        with open('account_information.csv', 'a', newline='') as f:
            wr = csv.writer(f, dialect='excel')
            wr.writerow(append_this)

    def withdraw(self, amount):
        if amount > self.balance_amt:
            print("Not enough remaining in balance")
        else:
            self.balance_amt -= amount

    def deposit(self, amount):
        self.balance_amt += amount

    def balance(self):
        return f"${self.balance_amt}"

    def account_config(self):
        return self.account_type


class Employee:
    def __init__(self, firstname, lastname, position, base_salary=60000):
        """Create employee object that can create customers and create bank accounts"""
        self.firstname = firstname
        self.lastname = lastname
        self.salary = base_salary
        self.position = position
        f = open('employee_information.csv', 'w+')
        try:
            data = pd.read_csv(f)
            data.empty
            f.close()
        except pd.errors.EmptyDataError:
            f.write('employee_id, firstname, lastname, salary, position\n')
            f.close()
        data = pd.read_csv('employee_information.csv')

        print(data.empty)
        if data.empty:
            employee_id = 1000000000
        else:
            employee_id = max(data['employee_id']) + 1
        print(employee_id)
        self.employee_id = employee_id
        append_this = [self.employee_id, self.firstname, self.lastname, self.salary, self.position]
        with open('employee_information.csv', 'a+') as f:
            wr = csv.writer(f, dialect='excel')
            wr.writerow(append_this)

    def create_customer(self, firstname, lastname, address):
        customer = Customer(firstname, lastname, address)
        return customer, f"User ID: {customer.user_number()}"

    def create_bank_account(self, accounttype="", userid=""):
        if accounttype != 'checking' or accounttype != 'savings':
            account_type = input('Please enter account type: checking or savings: ')
        else:
            pass
        user_id = userid
        while type(user_id) != int:
            try:
                user_id = int(input('Please enter valid user id: '))
            except ValueError:
                user_id = int(input('Please enter valid user id(integer only): '))
            bank_account = BankAccount(account_type, user_id)
        return bank_account


# x = Employee('jordan', 'tang', 'analydddst')
# x.create_customer('jordan', 'tang', 'address')
# x = Customer('Jordan', 'Tang', 'my address')
#print(x.firstname)
# a = BankAccount('checking')
# a.deposit(1000)
# a.withdraw(5000)
# print(a.account_config())
# print(a.account_number)
# print(a.balance())
