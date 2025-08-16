# Example: Bank Account Operations
# Let's track a bank account balance with various transactions

# Initial balance
balance = 1000.00    # Starting balance in dollars
print(f"Initial balance: ${balance:.2f}")

# Simple deposit using =
deposit = 500.00
balance = balance + deposit    # Could also write: balance += deposit
print(f"After deposit of ${deposit:.2f}: the balance is ${balance:.2f}")

# Compound assignment for withdrawal - shorter way
withdrawal = 200.00
balance -= withdrawal         # Same as: balance = balance - withdrawal
print(f"After withdrawal of ${withdrawal:.2f}: ${balance:.2f}")

# Monthly interest using *=
monthly_interest_rate = 0.01  # 1% monthly interest
balance *= (1 + monthly_interest_rate)
print(f"After interest: ${balance:.2f}")

# Quarterly bonus using +=
quarterly_bonus = 50.00
balance += quarterly_bonus
print(f"After quarterly bonus: ${balance:.2f}")

# Splitting account between two people using /=
balance /= 2
print(f"After splitting account: ${balance:.2f}")

# Power-of operator for long-term projection
years = 5
annual_interest = 0.05
balance **= (1 + annual_interest)  # Same as: balance = balance ** (1 + annual_interest)
print(f"Projected balance after {years} years: ${balance:.2f}")

# Modulus assignment for odd/even transaction count
transaction_count = 17
transaction_count %= 2  # Will be 1 if odd, 0 if even
print(f"Is the number of transactions odd? {bool(transaction_count)}")