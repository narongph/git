# Function input
name = int(input("Please input number"))            # Teat input function

print("Your input data = ", name)
if name>0 and name<=5:
    print("name value is 0-5")
else:
    if name>6 and name<=10:
        print("name value is 6-10")
    else:
        print("name value is >=11")
