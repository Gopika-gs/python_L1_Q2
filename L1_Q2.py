num = int(input("Enter a number "))
if num < 0 or num == 0:
    print("invalid input")
elif num % 2 == 0:
    print(num," is even number.")
else:
    print (num, " is odd number.")