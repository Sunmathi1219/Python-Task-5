""""
d.) validate regular expression of 16 character alpha-numeric password composed of alphabets of uppercase,lowercase,special characters numbers.
"""

import re
Password="UthraSunDhanu$45"

def validate_password(pwd):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$"

    if re.match(pattern,pwd):
        return True
    else:
        return False
    
print("validate Password :",validate_password(Password))    