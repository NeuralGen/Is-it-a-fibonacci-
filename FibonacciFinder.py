random_number = int(input("Enter a number to check whether it's a fibonacci number : "))  # Take a random number to check


def Fibonacci(n):  # Returns n'th fibonacci number
    if n<= 0:
        print("Incorrect input")
        
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    
    # Second Fibonacci number is 1
    elif n == 2:
        return 1

    # Else apply the formula
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


counter, fibo_found = 1, False  # Initializing variables

while Fibonacci(counter) <= random_number:
    if Fibonacci(counter) == random_number:
        print("The number you enetered is a fibonacci")
        fibo_found = True
    counter += 1
else:
    if not fibo_found:
        print("The number you enetered is not a fibonacci")
