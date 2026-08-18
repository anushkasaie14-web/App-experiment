# Experiment No. 4
# Title: Fibonacci using Recursion, Memoization and Tabulation


# -----------------------------------------
# METHOD 1: RECURSION
# -----------------------------------------

# Function to calculate Fibonacci using recursion
def fibonacci_recursion(n):

    # Base case: Fibonacci of 0 is 0
    if n == 0:
        return 0

    # Base case: Fibonacci of 1 is 1
    if n == 1:
        return 1

    # Recursive case
    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


# -----------------------------------------
# METHOD 2: MEMOIZATION (Top-Down Approach)
# -----------------------------------------

# Function to calculate Fibonacci using recursion and memoization
def fibonacci_memoization(n, memo={}):

    # Base case: Fibonacci of 0 is 0
    if n == 0:
        return 0

    # Base case: Fibonacci of 1 is 1
    if n == 1:
        return 1

    # Check if the result is already stored
    if n in memo:
        return memo[n]

    # Calculate and store the result
    memo[n] = (fibonacci_memoization(n - 1, memo) +
               fibonacci_memoization(n - 2, memo))

    return memo[n]


# -----------------------------------------
# METHOD 3: TABULATION (Bottom-Up Approach)
# -----------------------------------------

# Function to calculate Fibonacci using tabulation
def fibonacci_tabulation(n):

    # Base cases
    if n == 0:
        return 0

    if n == 1:
        return 1

    # Create a table
    dp = [0] * (n + 1)

    # Initialize first two values
    dp[0] = 0
    dp[1] = 1

    # Fill the table
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# -----------------------------------------
# MAIN PROGRAM
# -----------------------------------------

n = int(input("Enter the value of n: "))

print("Fibonacci using Recursion:",
      fibonacci_recursion(n))

print("Fibonacci using Memoization:",
      fibonacci_memoization(n))

print("Fibonacci using Tabulation:",
      fibonacci_tabulation(n))