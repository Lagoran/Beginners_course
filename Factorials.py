i = int(input("Please type you number : "))
factorial = 1

for num in range(1,i + 1):
    factorial *= num

print("Factorial of your number " + str(i) + " is " + str(factorial))