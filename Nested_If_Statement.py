#What is the Score?

Score = int(input("Give me the score of your grade. "))

if Score >= 90:
    print("Your grade is an A")
else:
    if Score >= 80:
        print("Your grade is a B")
    else:
        if Score >= 70:
            print("Your grade is a C.")
        else:
            if Score >= 60:
                print("Your grade is a D")
            else:
                if Score <= 60:
                    print("Your grade is an F and you are a retard.")


# Rewrite the code using ELIF statements

Score = int(input("Give me the score of your grade. "))

if Score >= 90:
    print("You got an A!")
elif Score >= 80:
    print("You got a B.")
elif Score >= 70:
    print("You got a C")
elif Score >= 60:
    print("You got a D")
else:
    print("YOu got an F and you a retard.")