from random import *

tank = randint(10,26)
full_run_miles = randint(200,401)

print("The car has " + str(tank) + " gallons and that will be enoght to travel " + str(full_run_miles) + " miles")
print("That makes a consumption of " + str(full_run_miles / tank) + " MPG")

def MPG(tank,run):
    print("Realistic consumption is : " + str(run // tank) + " MPG")


MPG(tank,full_run_miles)
