import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
1.For the first result, it comes out 6.
  I have seen 5 as smallest number and 20 as largest number.

2.For first result, I see 5.
  The smallest number that I have seen is 3 and largest number is 9.
  It never produced 4 because step is 2
  
3.I see 5.363105515780637 as result 
 The biggest number could be 5.5, while the smallest is 2.5.
"""


print(random.randint(1, 100))