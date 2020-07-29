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
