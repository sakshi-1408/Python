# # 1-Print no form 1 to 10 using a for loop  
# #for i in range(1,11):
#   #  print (i)

# #2-Calculate the sum of numbers from 1 to 10 using a for loop 
# #total_sum = 0
# #for i in range (1,11):
#  #   total_sum += i
# #print ("sum of number:", total_sum) 

# #3-print reverse numbers from 1 to 10 
# #for i in range (10,0,-1):
#  #   print (i) 

# #4-print even no from 1 to 10
# #for i in range (1,11):
#   # if i % 2 == 0:
#    #   print (i)

# #5-Print characters of a string using for loop
# #string = "HELLO"
# #for char in string:
#  #   print(char)

# # 6-Find the largest no in a list using a for loop
# #numbers = [3,4,5,6,7]
# #largest = numbers[0]
# #for num in numbers:
#  ##   if num>largest:
#   #      largest = num 
# #print ("largest number:",largest)

# # 7- Find the average of numbers in a list 
# #numbers = [4,6,8,3,9,15]
# #total_sum = 0
# #for num in numbers :
#   total_sum += num 
# #average = total_sum / len(numbers)
# #print("average:",average) 

# #8- Count the number of vowels in a string 
# string = "HELLO WORLD"
# vowels = "aeiouAEIOU"
# count = 0
# for char in string :
#    if char in vowels:
#       count += 1
# print ("number of vowels :",count)       

#9- print a pattern of stars using nested for loop.
# for i in range (1,6):
#     for j in range(i):
#         print ("*",end='')
#     print()    

#10- Calculte factorial of a number using a while loop
# number = 10
# factorial = 1
# while number > 0:
#     factorial *= number
#     number -= 1
# print ("Factorial:", factorial)     

#11- calcuate the sum of numbers between 1 to 100 using a while loop
# total_sum = 0
# number = 1
# while number <= 100:
#     total_sum +=number
#     number += 1
# print ("sum from 1 to 100:",total_sum)    

#12- Find all the prime numbers between 1 and 50 using nested loop
# primes = []
# for num in range(2,51):
#     is_prime = True
#     for i in range (2,int(num**0.5)+1):
#         if num % i == 0 :
#             is_prime = False 
#             break
#     if is_prime:
#             primes.append(num)
# print("Prime numbers between 1 and 50 are:",primes)  

# 13- Print numbers from 1 to 10 .If a number is even ,skip it using a for loop 
# for i in range(1,11):
#    if i % 2 == 0:
#       continue
#    print(i)           

#14- Print numbers from 1 to 10 . If a no is divisible by 4 , stop the loop.
# for i in range (1,11) :
#     if i % 4 == 0:
#         break 
#     print (i)
#15 - Print Fibonacci sequence up to the 10th term.
# fibonacci = [0,1]
# for i in range (2,10):
#     next_term = fibonacci[i-1] + fibonacci[i-2]
#     fibonacci.append(next_term)
# print("Fibonacci sequence up to 10th term:",fibonacci)    

#16- python program to convert the month name to a number of days 
# month = "August"
# days_in_month ={
#     "January":31,
#     "February":28,
#     "March":31,
#     "April":30,
#     "May":31,
#     "June":30,
#     "July":31,
#     "August":31,
#     "September":30,
#     "October":31,
#     "November":30,
#     "December":31,
# }
# print(f"Days in {month}:",days_in_month.get(month,"Invalid month"))

#17- Python program to check if a given number is an armstrong number.
# number = 120 
# sum_of_cubes = sum(int(digit)**3 for digit in str(number))
# if sum_of_cubes == number:
#     print(number,"is an armstrong number")
# else:
#     print(number,"is not an armstrong number")    

#18- find the first occurence of a number in a list using a while loop.
# numbers = [1,2,3,4,5,6]
# target = 3 
# index = 0
# found = -1
# while index <len(numbers):
#     if numbers[index]== target:
#         found = index 
#         break
#     index += 1
# print("First occurence of",target,"is at index:",found) 

# 19- print numbers in a list until a negative number is encountered using a while loop.
# numbers = [1,2,3,-4,5,-6,7]
# index = 0
# while index <len(numbers):
#     if numbers[index]<0:
#         break
#     print(numbers[index])
#     index += 1
