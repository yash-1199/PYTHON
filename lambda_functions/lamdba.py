from functools import reduce

# lambda functions in python are small,anonymous(nameless) functions.

# def add(a,b):
#     return a+b

#sum=lambda a,b : a+b

#lambda arguments :expresssion 

#print(sum(4,5))


#map,filter,reduce
 

# nums=[2,3,4,5]

# result=list(map(lambda x:x*x,nums))
# print(result)


#map==>transformtion
# map is used when you want to apply a function to every value in list
#map(function,iterable)


#filter ==>kepp only some elements based on condition 
nums=[1,2,3,4,5,6]
#fiter only even number
evn=[]
# for num in nums:
#     if num%2==0:
#         evn.append(num)
# print(evn)

#filter(function ,iteratable)

# res=list(filter(lambda x: x%2==0,nums))
# print(res)


#reduce is used combine all elements into a single values
# take all values combine and return one resuslt

nums1=[1,2,3,4,5,6]
#reduce(function,iterable object)
res2=reduce(lambda a,b:a+b,nums)
print(res2)

   