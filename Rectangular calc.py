def prism_vol(l, w, h):
    return l * w * h


lenght = int(input("Please type the lenght of the object : "))
width = int(input("Please type the width of the object : "))
height = int(input("Please type the height of the object : "))

The_volume = prism_vol(lenght, width, height)

print("\nThe volume of the rectangulat prism is : " + str(The_volume))