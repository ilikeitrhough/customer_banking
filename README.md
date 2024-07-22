# Account Interest Calculator
This project calculates interest earned and updates balances for savings and CD (Certificate of Deposit) accounts. 
Users input the initial balance, interest rate, and duration in months for both account types. 
The program computes the interest and updates the balances accordingly.

## Table of Contents
Installation
Usage
Project Structure
Functions
Example
Contributing
License

## Installation
Clone the Repository:**
bash
Copy code
git clone https://github.com/ilikeitrhough/customer_banking

### Navigate to the Project Directory:
bash
Copy code
cd account-interest-calculator

### Ensure Python is installed:
Download from python.org.

### Usage Run the program with:
bash
Copy code
python main.py
Follow the prompts to enter account details. The program will display the interest earned and updated balances.

# Customer Banking System

This project is a simple banking system that allows users to create savings and CD (Certificate of Deposit) accounts, calculate interest earned, and update the account balances accordingly. The system is composed of several Python files, each with a specific responsibility in the system.

## Table of Contents
1. [Files Description](#files-description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [License](#license)

## Files Description

### 1. Account.py
Contains the `Account` class which includes methods to set the balance and interest of an account.

```python
class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    def set_balance(self, balance):
        self.balance = balance

    def set_interest(self, interest):
        self.interest = interest

from Account import Account

class SavingsAccount(Account):
    def __init__(self, balance, interest_rate):
        super().__init__(balance, interest_rate)
        self.balance = balance
        self.interest_rate = interest_rate
        self.interest = 0

    def set_balance(self, updated_balance):
        self.balance = updated_balance

    def set_interest(self, interest_earned):
        self.interest = interest_earned

def create_savings_account(balance, interest_rate, months):
    savings_account = SavingsAccount(balance, interest_rate)
    interest_earned = balance * (interest_rate / 100) * (months / 12)
    updated_balance = balance + interest_earned
    savings_account.set_balance(updated_balance)
    savings_account.set_interest(interest_earned)
    return updated_balance, interest_earned

from Account import Account

class CDAccount(Account):
    def __init__(self, balance, interest_rate):
        super().__init__(balance, interest_rate)
        self.balance = balance
        self.interest_rate = interest_rate
        self.interest = 0

    def set_balance(self, updated_balance):
        self.balance = updated_balance

    def set_interest(self, interest_earned):
        self.interest = interest_earned

def create_cd_account(balance, interest_rate, months):
    cd_account = CDAccount(balance, interest_rate)
    interest_earned = balance * (interest_rate / 100) * (months / 12)
    updated_balance = balance + interest_earned
    cd_account.set_balance(updated_balance)
    cd_account.set_interest(interest_earned)
    return updated_balance, interest_earned

from cd_account import create_cd_account
from savings_account import create_savings_account

def main():
    savings_balance = float(input("Enter the savings account balance: "))
    savings_interest = float(input("Enter the annual savings interest rate (APR in %): "))
    savings_maturity = int(input("Enter the number of months for the savings account: "))
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)
    print(f"Interest earned on the savings account: ${interest_earned:.2f}")
    print(f"Updated savings account balance: ${updated_savings_balance:.2f}")

    cd_balance = float(input("Enter the CD account balance: "))
    cd_interest = float(input("Enter the annual CD interest rate (APR in %): "))
    cd_maturity = int(input("Enter the number of months for the CD account: "))
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
    print(f"Interest earned on the CD account: ${interest_earned:.2f}")
    print(f"Updated CD account balance: ${updated_cd_balance:.2f}")

if __name__ == "__main__":
    main()
