"""class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            raise ValueError("Division by zero")
        return self.num1 / self.num2
calc = Calculator(10, 5)
print("Addition:", calc.add())
print("Subtraction:", calc.subtract())
print("Multiplication:", calc.multiply())
print("Division:", calc.divide())"""
"""import datetime

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def calculate_age(self):
        today = datetime.date.today()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return age
name = input("Enter your name: ")
country = input("Enter your country: ")
dob_str = input("Enter your date of birth (YYYY-MM-DD): ")
dob = datetime.datetime.strptime(dob_str, "%Y-%m-%d").date()
person = Person(name, country, dob) 
print(person.name, "is from", person.country)
print("Age:", person.calculate_age())"""
"""class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def create_account(self):
        name = input("Enter customer name: ")
        initial_balance = float(input("Enter initial balance: "))
        account_number = len(self.customers) + 1
        account = {"account_number": account_number, "name": name, "balance": initial_balance}
        self.customers.append(account)
        print(f"Account created successfully. Account number: {account_number}")

    def deposit(self):
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter amount to deposit: "))
        for customer in self.customers:
            if customer["account_number"] == account_number:
                customer["balance"] += amount
                print(f"Deposited {amount} to account {account_number}")
                return
        print("Account not found")

    def withdraw(self):
        account_number = int(input("Enter account number: "))
        amount = float(input("Enter amount to withdraw: "))
        for customer in self.customers:
            if customer["account_number"] == account_number:
                if customer["balance"] >= amount:
                    customer["balance"] -= amount
                    print(f"Withdrew {amount} from account {account_number}")
                else:
                    print("Insufficient balance")
                return
        print("Account not found")

    def check_balance(self):
        account_number = int(input("Enter account number: "))
        for customer in self.customers:
            if customer["account_number"] == account_number:
                print(f"Account {account_number} balance: {customer['balance']}")
                return
        print("Account not found")
bank = Bank("My Bank")

while True:
    print("\nBank Operations:")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        bank.create_account()
    elif choice == 2:
        bank.deposit()
    elif choice == 3:
        bank.withdraw()
    elif choice == 4:
        bank.check_balance()
    elif choice == 5:
        break
    else:
        print("Invalid choice")"""
"""import math

class Shape:
    def getPerimeter(self):
        pass

    def getArea(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def getPerimeter(self):
        return 2 * math.pi * self.radius

    def getArea(self):
        return math.pi * self.radius**2
circle = Circle(5)
print("Perimeter of the circle:", circle.getPerimeter())
print("Area of the circle:", circle.getArea())"""
"""import math

def area(shape):
  if shape == "circle":
    radius = float(input("Enter the radius of the circle: "))
    return math.pi * radius * radius
  elif shape == "square":
    side = float(input("Enter the side of the square: "))
    return side * side
  elif shape == "rectangle":
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    return length * breadth
  else:
    return "Invalid shape"

shape = input("Enter the shape (circle, square, rectangle): ")
result = area(shape)
print("The area of the", shape, "is:", result)"""
"""class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)
num1 = ComplexNumber(2, 3)
num2 = ComplexNumber(4, 5)
sum_result = num1 + num2
print("Sum:", sum_result.real, "+", sum_result.imag, "i")
product_result = num1 * num2
print("Product:", product_result.real, "+", product_result.imag, "i")"""
"""class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def __add__(self, other):
        seconds = self.seconds + other.seconds
        minutes = self.minutes + other.minutes + seconds // 60
        hours = self.hours + other.hours + minutes // 60
        seconds %= 60
        minutes %= 60
        return Time(hours, minutes, seconds)

    def __sub__(self, other):
        seconds = self.seconds - other.seconds
        minutes = self.minutes - other.minutes
        hours = self.hours - other.hours
        if seconds < 0:
            seconds += 60
            minutes -= 1
        if minutes < 0:
            minutes += 60
            hours -= 1
        return Time(hours, minutes, seconds)
time1 = Time(10, 30, 20)
time2 = Time(5, 45, 30)
added_time = time1 + time2
print("Added time:", added_time)
subtracted_time = time1 - time2
print("Subtracted time:", subtracted_time)"""
"""from typing import Dict, List
from datetime import datetime, date
import uuid

class InsufficientFundsError(Exception):
    pass

class Account:
    
    def __init__(self, account_holder: str, initial_balance: float = 0.0, account_type: str = 'Savings'):
        self.account_number = str(uuid.uuid4())[:8]
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_type = account_type
        self.transactions: List[Dict] = []
        if initial_balance > 0:
            self.record_transaction('Initial Deposit', initial_balance)
    
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self.balance += amount
        self.record_transaction('Deposit', amount)
    
    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds")
        
        self.balance -= amount
        self.record_transaction('Withdrawal', -amount)
    
    def record_transaction(self, transaction_type: str, amount: float) -> None:
        transaction = {
            'date': datetime.now(),
            'type': transaction_type,
            'amount': amount,
            'balance': self.balance
        }
        self.transactions.append(transaction)
    
    def get_transaction_history(self) -> List[Dict]:
        return self.transactions
    
    def __str__(self) -> str:
        return (f"Account Number: {self.account_number}\n"
                f"Holder: {self.account_holder}\n"
                f"Type: {self.account_type}\n"
                f"Balance: ${self.balance:.2f}")

class Bank:
    
    def __init__(self, name: str):
        self.name = name
        self.accounts: Dict[str, Account] = {}
    
    def create_account(self, account_holder: str, initial_balance: float = 0.0, 
                       account_type: str = 'Savings') -> Account:
        account = Account(account_holder, initial_balance, account_type)
        self.accounts[account.account_number] = account
        return account
    
    def get_account(self, account_number: str) -> Account:
        if account_number not in self.accounts:
            raise ValueError("Account not found")
        return self.accounts[account_number]
    
    def transfer_funds(self, from_account: str, to_account: str, amount: float) -> None:
        if from_account == to_account:
            raise ValueError("Cannot transfer to the same account")
        
        source_account = self.get_account(from_account)
        destination_account = self.get_account(to_account)
        source_account.withdraw(amount)
        destination_account.deposit(amount)
    
    def list_accounts(self) -> List[Account]:
        return list(self.accounts.values())

def main():
    my_bank = Bank("Python National Bank")
    
    while True:
        try:
            print("\n--- Bank Management System ---")
            print("1. Create New Account")
            print("2. View Account Details")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Transfer Funds")
            print("6. View Transaction History")
            print("7. List All Accounts")
            print("8. Exit")
            choice = input("Enter your choice (1-8): ").strip()
            
            if choice == '1':
                name = input("Enter account holder name: ").strip()
                balance = float(input("Enter initial balance: "))
                account_type = input("Enter account type (Savings/Checking): ").strip()
                account = my_bank.create_account(name, balance, account_type)
                print(f"Account created successfully. Account Number: {account.account_number}")
            
            elif choice == '2':
                account_number = input("Enter account number: ").strip()
                account = my_bank.get_account(account_number)
                print("\nAccount Details:")
                print(account)
            
            elif choice == '3':
                account_number = input("Enter account number: ").strip()
                amount = float(input("Enter deposit amount: "))
                account = my_bank.get_account(account_number)
                account.deposit(amount)
                print("Deposit successful!")
            
            elif choice == '4':
                account_number = input("Enter account number: ").strip()
                amount = float(input("Enter withdrawal amount: "))
                account = my_bank.get_account(account_number)
                account.withdraw(amount)
                print("Withdrawal successful!")
            
            elif choice == '5':
                from_account = input("Enter source account number: ").strip()
                to_account = input("Enter destination account number: ").strip()
                amount = float(input("Enter transfer amount: "))
                my_bank.transfer_funds(from_account, to_account, amount)
                print("Transfer successful!")
            
            elif choice == '6':
                account_number = input("Enter account number: ").strip()
                account = my_bank.get_account(account_number)
                print("\n--- Transaction History ---")
                for transaction in account.get_transaction_history():
                    print(f"{transaction['date']} | {transaction['type']} | "
                          f"${abs(transaction['amount']):.2f} | "
                          f"Balance: ${transaction['balance']:.2f}")
            
            elif choice == '7':
                print("\n--- All Accounts ---")
                for account in my_bank.list_accounts():
                    print(account)
                    print("-" * 30)
            
            elif choice == '8':
                print("Thank you for using the Bank Management System!")
                break
            
            else:
                print("Invalid choice. Please try again.")
        
        except ValueError as ve:
            print(f"Error: {ve}")
        except InsufficientFundsError as ife:
            print(f"Transaction Error: {ife}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    main()"""
"""class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def __add__(self, other):
        seconds = self.seconds + other.seconds
        minutes = self.minutes + other.minutes + seconds // 60
        hours = self.hours + other.hours + minutes // 60
        seconds %= 60
        minutes %= 60
        return Time(hours, minutes, seconds)

    def __sub__(self, other):
        seconds = self.seconds - other.seconds
        minutes = self.minutes - other.minutes
        hours = self.hours - other.hours
        if seconds < 0:
            seconds += 60
            minutes -= 1
        if minutes < 0:
            minutes += 60
            hours -= 1
        return Time(hours, minutes, seconds)

def get_time_input():
    hours = int(input("Enter hours: "))
    minutes = int(input("Enter minutes: "))
    seconds = int(input("Enter seconds: "))
    return Time(hours, minutes, seconds)
time1 = get_time_input()
time2 = get_time_input()
added_time = time1 + time2
print("Added time:", added_time)
subtracted_time = time1 - time2
print("Subtracted time:", subtracted_time)"""
"""class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self):
        item_name = input("Enter item name: ")
        item_price = float(input("Enter item price: "))
        self.items.append((item_name, item_price))

    def remove_item(self):
        item_name = input("Enter item name to remove: ")
        for i in range(len(self.items)):
            if self.items[i][0] == item_name:
                del self.items[i]
                print(f"{item_name} removed from cart.")
                break
        else:
            print(f"{item_name} not found in cart.")

    def calculate_total(self):
        total_price = 0
        for item, price in self.items:
            total_price += price
        return total_price

def main():
    cart = ShoppingCart()

    while True:
        print("\n1. Add Item")
        print("2. Remove Item")
        print("3. Calculate Total")
        print("4. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            cart.add_item()
        elif choice == 2:
            cart.remove_item()
        elif choice == 3:
            total_price = cart.calculate_total()
            print("Total Price:", total_price)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()"""

"""class Employee:
    def work(self):
        print("Employee is working.")

    def getSalary(self):
        salary = float(input("Enter employee's salary: "))
        print(f"Employee's salary is: {salary}")


class HRManager(Employee):
    def work(self):
        print("HR Manager is managing employees.")

    def addEmployee(self):
        new_employee_name = input("Enter new employee's name: ")
        print(f"HR Manager is adding a new employee: {new_employee_name}")
employee1 = Employee()
employee1.work()
employee1.getSalary()

hr_manager = HRManager()
hr_manager.work()
hr_manager.getSalary()
hr_manager.addEmployee()"""

"""import math

class Shape:
    def getPerimeter(self):
        pass

    def getArea(self):
        pass

class Circle(Shape):
    def __init__(self):
        self.radius = float(input("Enter the radius of the circle: "))

    def getPerimeter(self):
        return 2 * math.pi * self.radius

    def getArea(self):
        return math.pi * self.radius**2
circle = Circle()
print("Perimeter of the circle:", circle.getPerimeter())
print("Area of the circle:", circle.getArea())"""

"""def divide_numbers(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
divide_numbers(10, 2)
divide_numbers(10, 0)"""
"""def get_integer_input():
    while True:
        try:
            num = int(input("Enter an integer: "))
            return num
        except ValueError:
            print("Invalid input. Please enter an integer.")
integer_value = get_integer_input()
print("You entered:", integer_value)"""
"""def divide_numbers(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ArithmeticError as e:
        print("An arithmetic error occurred:", e)
divide_numbers(10, 2)
divide_numbers(10, 0)"""
"""import math

def find_square_root(number):
    if number < 0:
        raise ValueError("Square root of negative number is not defined.")
    else:
        return math.sqrt(number)
num = float(input("Enter a number: "))
result = find_square_root(num)
print("The square root of", num, "is", result) """
"""import math
number = float(input("Enter a number: "))
log_value = math.log(number)
print("Natural logarithm of", number, "is", log_value)
print("The value of pi is:", math.pi)"""
"""import sys
print("Command-line arguments:", sys.argv)
print("Python version:", sys.version)
print("Platform:", sys.platform)
print("Exiting the program...")
sys.exit()"""
"""import math
print("Value of pi:", math.pi)
print("Value of e:", math.e)
angle_in_degrees = float(input("Enter an angle in degrees: "))
angle_in_radians = math.radians(angle_in_degrees)
print("Sine of the angle:", math.sin(angle_in_radians))
print("Cosine of the angle:", math.cos(angle_in_radians))
print("Tangent of the angle:", math.tan(angle_in_radians))
number = float(input("Enter a number: "))
print("Natural logarithm of the number:", math.log(number))
print("Base-10 logarithm of the number:", math.log10(number))
base = float(input("Enter the base: "))
exponent = float(input("Enter the exponent: "))
result = math.pow(base, exponent)
print(base, "raised to the power of", exponent, "is:", result)
n = int(input("Enter a non-negative integer: "))
factorial = math.factorial(n)
print("Factorial of", n, "is:", factorial)
num = float(input("Enter a non-negative number: "))
sqrt_value = math.sqrt(num)
print("Square root of", num, "is:", sqrt_value)"""
"""import time
current_time = time.time()
print("Current time in seconds since the Epoch:", current_time)
readable_time = time.ctime(current_time)
print("Readable time:", readable_time)
local_time = time.localtime()
print("Local time:", local_time)
formatted_time = time.strftime("%d/%m/%Y %H:%M:%S", local_time)
print("Formatted time:", formatted_time)
time.sleep(5)
print("5 seconds have passed.")"""
"""import os

# Get current working directory
print(os.getcwd())

# Create a new directory
os.mkdir("new_folder")

# List files and directories
print(os.listdir())

# Get file information
print(os.stat("file.txt"))  # Replace "file.txt" with an actual file name

# Rename a file
os.rename("old_file.txt", "new_file.txt")  # Replace with actual file names

# Remove a file
os.remove("file_to_remove.txt")  # Replace with an actual file name"""
"""import random
random_integer = random.randint(1, 10)
print("Random integer:", random_integer)
random_float = random.random()
print("Random float:", random_float)
fruits = ["apple", "banana", "cherry", "date"]
random_fruit = random.choice(fruits)
print("Random fruit:", random_fruit)
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled numbers:", numbers)
sample_numbers = random.sample(range(1, 21), 5)
print("Sample numbers:", sample_numbers)"""
# my_module.py
def greet(name):
    print("Hello, " + name + "!")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# main.py
import my_module

my_module.greet("Alice")
result = my_module.factorial(5)
print("Factorial of 5:", result)