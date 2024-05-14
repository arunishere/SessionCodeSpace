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
