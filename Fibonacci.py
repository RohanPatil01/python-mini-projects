def fibonacci(num):
    if num <= 0:
        print("Please enter a positive integer!")
    else:
        a, b = 0, 1
        print(f"The Fibonacci Sequence of {num} terms:", end=" ")
        for _ in range(num):
            print(a, end=" ")
            a, b = b, a + b

num = int(input("Enter the number of terms: "))
fibonacci(num)
