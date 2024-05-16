""""
c.) validate Telephone numbers of USA using regular expression in python

"""
import re 
Telephone_number="+1 123-456-7890"

def validate_phone_no(number):
    pattern = r"^\+1\s\d{3}[-]\d{3}[-]\d{4}$"
    if re.match(pattern,number):
        return True
    else:
        return False
    
print("Validate Phone Number :",validate_phone_no(Telephone_number))    