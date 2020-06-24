# @author shazychinnu
import collections
num = [2,2,4,6,6,8,6,10,4,20,30]
print(sum(collections.Counter(num).values())) # This line find the number of characters in the list
print(sum(num))

sum = 0
for i in num:
    sum+=1
print(sum)

sum=0
for i in num:
    sum+=i
print(sum)
