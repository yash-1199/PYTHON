# nested if 
#it is nothing but if statement inside if statement

# age above 18,he should contain an id card

age=20
has_id=False

if age>=18:
    if has_id==True:
        print('ypu can vote')


# I want to check a number whether it is evn or odd
# first I will check whether a number is greater than 0 or not
# if it is greater than 0 then only I will check whether it is even or odd

# num=100
# if num>0:
#     if num %2==0:
#         print('even number')
#     else:
#         print('odd number')
# else:
#     print('cant find even or odd as the number is negative')

bal=20000
withdraw=15000
if withdraw<bal:
    if withdraw<10000:
        print('transaction successful')
    else:
        print('your trancation amount cant be above 10000')
else:
    print('no sufficent balance')


