name = input("Name: ")


age = int(input("Age: "))


height = int(input("Height(cm): "))


weight = int(input("Weight(kg): "))


eyeCol = input("Eye Colour: ")


hairCol = input("Hair Colour: ")


if(age < 10):
    print ("Go get your parent please and ask them to not let you on the computer, silly x")
elif(age > 10 or age < 18):
    print ("Go back to school silly, you shouldn't be playing with this app!")
elif(age > 18 or age < 60):
    print ("You're probably assessing this code, and I thank you for correctly inputting stuff!")


if(height < 130):
    print ("AWWWWWWWWWWWWWWW SMOL CUTE BEAN!")
elif(height > 130 or height < 160):
    print ("Average height boundaries, I pat you nicely")
elif(height > 160 or height < 180):
    print ("waw so tall")
else:
    print ("HEIGHT ERROR WAW")

if(weight < 20):
    print("uhm...you should try and get some help sweetie, you're really light")
elif (weight > 20 or weight < 40):
    print ("Do me a favour and go eat a banana! bananas are great! yay for potassium! x")
elif (weight > 40 or weight < 90):
    print ("yay for average weight!!!!")
else:
    print ("You're doing okay!")
