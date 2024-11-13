#Write a python function add_two_numbers(a,b) that takes two numbers as input and returns their sum.
# def add_two_numbers(a, b):
#     return a + b
# result = add_two_numbers(3, 5)
# print(result)  

#2- Define a function find_maximum(a,b) that accepts two numbers and returns the larger number.
# def find_maximum(a, b):
#     return a if a > b else b
# result = find_maximum(10, 20)
# print(result)  

#3- Create a  function is_positive(num) tht checks if a given number is positive. The function should return True 
#if the number is positive nd flse otherwise.
# def is_positive(num):
#     return num > 0
# print(is_positive(5))    
# print(is_positive(-3))   
# print(is_positive(0))    

#4- Write a function print_name(name) that takes string name and prints "My name is [name]"
# def print_name(name):
#     print(f"My name is {name}")
# print_name("Alice")  

#5- Write a function square(x) that returns the square of a number x.
# def square(x):
#     return x**2 
# result =square(10**2)    
# print (result)    

#6- write a python function find_greater_than(1st ,n) that accepts a list 1st of numbers and a number n.  The function 
# should return a new list containing only the numbers greater than n.
# def find_greater_than(numbers, n):
#     return [num for num in numbers if num > n]

# numbers = [1, 5, 10, 15, 20]
# n = 10
# result = find_greater_than(numbers, n)
# print(result)  


#7- Create a function count_vowels(s) that takes a string s an input and returns the number of vowels in the string.
# def count_vowels(s):
#     vowels = "aeiouAEIOU"  
#     count = sum(1 for char in s if char in vowels)
#     return count
# string = "Hello, World!"
# result = count_vowels(string)
# print(result)  

#8- Write a python function factorial(n) that  calculates and returns the factorial of a number n using recursion.
# def factorial(n):
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers.")
#     elif n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# number = 5
# result = factorial(number)
# print(result)  

#9- Write a python function circle_area(radius) that takes the radius of a circleand returns the area of the circle.
# import math

# def circle_area(radius):
#     if radius < 0:
#         raise ValueError("Radius cannot be negative.")
#     return math.pi * (radius ** 2)
# radius = 5
# result = circle_area(radius)
# print(result)  

#10- Write a python function monthly_payment(principal,rate , years) that calculates the monthly mortgage payment for
# a given principal loan amount, annual interest rate , and loan term in years .
def monthly_payment(principal, rate, years):
    monthly_rate = rate / 100 / 12
    total_payments = years * 12
    
    if monthly_rate == 0:  
        return principal / total_payments
    payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -total_payments)
    return payment
principal = 200000  
rate = 5 
years = 30  
result = monthly_payment(principal, rate, years)
print(f"Monthly Payment: ${result:.2f}")  
