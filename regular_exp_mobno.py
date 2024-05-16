""""
b.) validate mobile number of bangladesh using regular expression in python
"""

import re

mobile_number = "+8801712345678"

def validate_mobile_no(number):
    pattern = r"^\+8801[3-9]\d{8}$"

    if re.match(pattern,number):
        return True
    
    else:
        return False
    
print("Validate Mobile  Number :",validate_mobile_no(mobile_number))    