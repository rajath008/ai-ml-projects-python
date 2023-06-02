import re

email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
while 1:
    user_email=str(input("Enter your email : "));
    
    if re.search(email_condition,user_email):
        print("Valid Email")
    
    else:
        print("Wrong email")