class InsufficientFundsError(Exception):
    """Custom exception for insufficient balance"""
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(" Not enough balance to withdraw!")
    else:
        balance -= amount
        print(f"Withdrawal successful! Remaining balance: Rs.{balance}")
    return balance



try:
    withdraw(5000, 6000)
except InsufficientFundsError as e:
    print(e)
