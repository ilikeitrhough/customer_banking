# Import the Account class from the Account.py file.
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
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        float: The interest earned.
    """
    # Create an instance of the SavingsAccount class and pass in the balance and interest rate parameters.
    savings_account = SavingsAccount(balance, interest_rate)

    # Calculate interest earned
    interest_earned = balance * (interest_rate / 100) * (months / 12)

    # Update the savings account balance by adding the interest earned
    updated_balance = balance + interest_earned

    # Pass the updated_balance to the set_balance method using the instance of the SavingsAccount class.
    savings_account.set_balance(updated_balance)

    # Pass the interest_earned to the set_interest method using the instance of the SavingsAccount class.
    savings_account.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return updated_balance, interest_earned
