print('hi')

# try:
#     a=10
#     b=0
#     print(a/b)
# except:
#     print('dont gve zero for b')
#     b=10

# print('python')
# print('pyspark')

#zeroDivion errors
#value error
#type eror
#indexerror
#key errors
#fileNot found error

# try:
#     file=open('test1.txt')
# except:
#     print('file is not there')
#     file=open('test.txt')
#     print('file is not there opening other file')

try:
    a=int(input('Enter value a '))
    b=int(input('enter value b '))
    print(a/b)
except:
    print('Cannot divide by zero')
