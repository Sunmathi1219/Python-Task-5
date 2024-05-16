"""
Write a python function to validate the regular expression for the following
a) email address
"""

import re

email_addr="sunmathiuthra26@gmail.com"

def validate_email_address(address):
    pattern = r"^[a-zA-z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,6}$"

    if re.match(pattern,address):
        return True
    
    else:
        return False
    
print("Validate Email Address :", validate_email_address(email_addr))    