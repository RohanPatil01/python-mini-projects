def factorial(num):
    if num == 0:
        return 1
    elif num < 0:
        return "Please enter a positive integer!"
    else:
        facto = num*factorial(num-1)
        return facto

num = int(input("Enter an integer: "))
print(factorial(num))