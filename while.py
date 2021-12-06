i = int(input("Please enter the digit of your desires : "))
pos_i = i
sum = 0

while i > 0:
    sum += i
    i -=1

print("You have entered the following digit " + str(pos_i) + " and the sum of the respective digits is " + str(sum))