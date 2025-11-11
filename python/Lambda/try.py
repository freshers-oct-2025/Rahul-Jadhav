'''
from functools import reduce


f=lambda a,b:a+b
print(f(5,10))  



nums=[3,2,6,7,4,2,9]
evens=list(filter(lambda x:x%2==0,nums))
print(evens)

squares=list(map(lambda x:x**2,nums))
print(squares)

doubles=list(map(lambda x:x*2,nums))
print(doubles)

sum_all = reduce(lambda a,b:a+b,nums)
print(sum_all)

avg=sum_all/len(nums)
print(avg)

'''

str="rahul "*3
print(str)

