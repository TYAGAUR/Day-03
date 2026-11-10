try:
    tokens = int(input("Enter token count: "))
    print("Token count:", tokens)
except ValueError:
    print("Please enter a whole number.")