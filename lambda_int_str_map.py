"""" Lambda function  to check every element of a list is an integer or string using map() function"""

data=['sunmathi',1912,'samuthra',26,'dhanu',884]

int_or_str=lambda x: isinstance(x,int) or isinstance(x,str)

result=list(map(int_or_str,data))

if result:
    print("Every elements of a list is integers or string")

else:
    print("Every elements of a list is not  integers or string")    



