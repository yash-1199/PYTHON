import file_utility
#import math 
from math import *
fileName="data.txt"

content = file_utility.read_file(fileName)
#print(content)


#file_utility.write_file(fileName,'I learn python very well')

#file_utility.append_file(fileName,'Python is very simple')

number_lines=file_utility.count_lines(fileName)
#print(number_lines)

print(math.factorial(20))

math.acos(52)
math.tan(90)
