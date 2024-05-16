


'''

Control Structures: Use to control the flow of the Program

If - Else

'''

'''

>=21 - The Person is allowed
18 - 20 - Persion should check with the staff
<18 - Strictly Not Allowed


'''


# age = int(input("Please enter the Age: "))

# if age >= 21:
#     print("You are allowed!")

# else:
#     print("You are not allowed. Check with  Staff")



age = float(input("Please enter the Age: "))
if age >= 21:
    print("Check Passed.")

elif age > 18 and age <=20:
    print("Kindly reach out to the Staff")

else:
    print("You are not allowed!")


