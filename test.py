score = int(input("Student degree is : "))

if score >= 90 :
    print("This student score of " + str(score) + " is referring to grade A" )
else:
    if score >= 80 and score < 90:
        print("B")
    else :
        if score >= 70:
            print("C")
        else :
            if score >= 60:
                print("D")