'''
Challenge # 1:
Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.
ex:
sum_to(6)  # returns 21
sum_to(10) # returns 55
'''
def sum_to(n):
  return sum(range(1, n + 1))
# sum1 = sum_to(1)
# print(sum1)

'''
Challenge # 2:
Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.
ex:
largest([1, 2, 3, 4, 0])  # returns 4
largest([10, 4, 2, 231, 91, 54])  # returns 231
'''

def largest(nums):
  return max(nums)
# res1 = largest([1, 3, 5, 7, 9])
# print(res1)
# res2 = largest([7, 2, 193432, 0, -55])
# print(res2)

'''
Challenge # 3:
Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.
ex:
occurrences('fleep floop', 'e')   # returns 2
occurrences('fleep floop', 'p')   # returns 2
occurrences('fleep floop', 'ee')  # returns 1
occurrences('fleep floop', 'fe')  # returns 0
'''

def occurrences(string, comparison_string):
  count = 0
  start = 0
  comparison_len = len(comparison_string)
  while start < len(string):
    index = string.find(comparison_string, start)
    if index == -1:
      break
    count += 1
    start = index + comparison_len
  return count

# res1 = occurrences('dragon ball z', 'a')
# print(res1)

'''
Challenge # 4:
Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.
ex:
product(-1, 4) # returns -4
product(2, 5, 5) # returns 50
product(4, 0.5, 5) # returns 10.0
'''

def product(*args):
  sum = 1
  for num in args:
    sum *= num
  return sum
# res = product(2, 10)
# print(res)

'''
BONUS🚀:
Write a function named steps_to_zero that accepts a non-negative integer as an argument, and returns the number of steps it took to reduce the integer to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
steps_to_zero(14) # returns 6
'''

# Step 1) 14 is even; divide by 2 and obtain 7. 
# Step 2) 7 is odd; subtract 1 and obtain 6.
# Step 3) 6 is even; divide by 2 and obtain 3. 
# Step 4) 3 is odd; subtract 1 and obtain 2. 
# Step 5) 2 is even; divide by 2 and obtain 1. 
# Step 6) 1 is odd; subtract 1 and obtain 0.
