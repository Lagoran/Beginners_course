def C_F_converter(Celsius_degrees):
    return round(1.8*Celsius_degrees + 32,1)


Celsius = float(input("Please type the degrees in Celsius : "))

Farenheit = C_F_converter(Celsius)

print("\nDegrees converted in Farenheit degrees is : " + str(Farenheit))