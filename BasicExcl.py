# assigning the value 20 to first_number (short cut : ctrl+/)


import os
import sys


x = 10
y = 20


# result = x+y

'''
Arithmetic Operators

+, *, -, /, //, %, **


Order of Precedence

PEDMAS

PARANTHESIS
EXPONENT
DIVISION
MULTIPLICAITON
ADDITION
SUBSTRACTION

1. ()
2. **
3. *, /, //, % (Equal precedence - Evaluated from left to right)
4. +, - (Equal precedence - Evaluated from left to right)

Comparison Operators 

>, <, >=, <=, ==, != (Returns Boolean values - TRUE / FALSE)

Logical Operators / Boolean Operators 

AND, OR, NOT

Truth Table

AND (Returns TRUE when ALL the conditions are TRUE)
TRUE AND FALSE = FALSE
FALSE AND TRUE = FALSE
FALSE AND FALSE = FALSE
TRUE AND TRUE = TRUE

OR (Returns TRUE when ANY the conditions are/is TRUE)
TRUE OR FALSE = TRUE
FALSE OR TRUE = TRUE
FALSE OR FALSE = FALSE
TRUE OR TRUE = TRUE

NOT (Reverses the Boolean Value)
TRUE = FLASE
FALSE = TRUE

Datatypes
1. String --- str -- Characters
2. Integer -- int
3. float -- float
4. Boolean -- bool
5. Complex Number -- complex (scientific calculations)

'''

# print('Division: ', 10/3)
# print('Floor Division: ', 10//3)
# print('Remainder: ', 10%3)
# print('Power: ', 2**3)

# print(4-2+3+10*5/2)

# age = 18
# name = 'John'
# print( not (age == 18 and name == 'Oliver'))


# name = input("Please Enter you name: ")
# location = input("Enter you location: ")

# print(f"Good Morning! {name}, I see that you are from {location}")



from datetime import date


current_balance = 50000.00
account_holder_name = "Kshitij"
account_number = 2015640
transaction_type = "Debited" 
in_out_account = "Rahul"
transaction_amount = 10000.00
trasacation_date = date.today()
current_balance -= transaction_amount


message = f"""

Dear {account_holder_name}, your account with number {account_number} is {transaction_type} with {transaction_amount}
from {in_out_account} on {trasacation_date}. Current Balance: {current_balance}
If you have any queries please reach out to +91-04319654315 or help@yourbank.com.

"""

message_1 = """

Dear {}, your account with number {} is {} with {}
from {} on {}. Current Balance: {}
If you have any queries please reach out to +91-04319654315 or help@yourbank.com.

""".format(account_holder_name, account_number, transaction_type, transaction_amount, in_out_account, trasacation_date, current_balance)



message_2 = """

Dear {0}, your account with number {1} is {2} with {3}
from {4} on {5}. Current Balance: {6}
If you have any queries please reach out to +91-04319654315 or help@yourbank.com.

Thank you for banking with us {0}.

""".format(account_holder_name, account_number, transaction_type, transaction_amount, in_out_account, trasacation_date, current_balance)


print(message_2)






# print("Good Morning! {}, I see that you are from {}".format(name, location))