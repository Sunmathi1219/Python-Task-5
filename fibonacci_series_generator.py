""""
python lambda function create a fibonacci series from 1 to 50 elements
"""

from functools import reduce

fibonacci_series=lambda y: reduce(lambda x,_: x+[x[-1]+x[-2]],range(y-2),[0,1])

print("Fibonacci series from 1 to 50 elements is :" ,fibonacci_series(50))