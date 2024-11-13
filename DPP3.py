# # # #1- Create a list of 5 integres and print the sum of all the elements.
# # # # numbers = [1,2,3,4,5]
# # # # total_sum = sum(numbers)
# # # # print ("The sum of the numbers :",total_sum)

# # #  #2- given the list no =[3,8,2,10,6], print the first ,last and middle elements of the list.
# # # # number =[3,8,2,10,6]
# # # # first_no = number[0]
# # # # last_no = number[-1]
# # # # middle_no = number[len(number) // 2]

# # # # print("First element:",first_no)
# # # # print("Last element:",last_no)
# # # # print("Middle element:",middle_no)

# # # #3- Slice the list to print the first thre elements
# # # # fruits = ['apple','banana','cherry','date']
# # # # first_three_fruits = fruits[:3]
# # # # print("First three fruits :",first_three_fruits )

# # # #4- Add 'Yellow' at the end of the list and then remove  'green'.
# # # # Colors = ['red','green','blue']
# # # # Colors.append("yellow")
# # # # Colors.remove ("green")
# # # # print("updated list",Colors)

# # # #5- Generate a list of squares of numbers from 1 to 10 using list comprehension
# # # # squares = [x**2 for x in range(1,11)]
# # # # print ("The square of numbers are:", squares )

# # # #6-Create a 2D list representing a 3x3 matrix and access the element in the second row and third column
# # # # matrix = [
# # # #     [1 , 2 , 3],
# # # #     [1 , 2 , 3],
# # # #     [1 , 2 , 3]
# # # # ]
# # # # element=  matrix[1],[2]
# # # # print ("Elements in  the third row and second column :", element)


# # #                                    #TUPLE
# # # # 1- Create a tuple of 4 strings and print its fourth element.
# # # # my_tuple = ('pple','banana','cherry','mango')
# # # # fourth_element = my_tuple[3]
# # # # print(fourth_element)


# # # #2- why cant we modify the elements of a tuple? 
# # # # give an example of an arror that occurs when trying to modify a tuple.

# # # # my_tuple = (1,2,3)
# # # # print ("tuples cnnot be modified after creation)


# # # #3-  Creating a tuple with three integers.
# # # coords =  (3,4,5)
# # # x,y,z = coords
# # # print(x,y,z)


# # #4- creating two tuples
# # tuple1 = (1,2,3)
# # tuple2 = (4,5,6)
# # concatenated = tuple1 + tuple2
# # print(concatenated)

# #5- creating a list with three integers
# my_list = [10,20,30]
# my_tuple = tuple(my_list)
# print(my_tuple)

# Finding elements
# creating a tuple with letters
# letters  = ('a','b','c','d')
# if 'e' in letters:
#     print("e is in the tuple")
# else:
#     print("e is not in tuple")    


#7- Creating a dictionary with fruits as keys and their prices as values.
# fruit_prices = {'apple': 50,'banana':70}
# print(fruit_prices['apple'])

#8- Creating a dictionary with fruit prices.
# fruit_prices = {'apple': 50,'banana':70}
# fruit_prices['orange']=30
# fruit_prices['banana']=40
# print(fruit_prices)

#9- Creating a dictionary with student info.
# student = {'name':'Sakshi','age':22,'course':'MCA'}
# for key,value in student.items():
#     print(key,value)

#10- creating a dictionary of fruit  prices
# fruit_prices = {'apple': 50,'banana':70,'orange':30}
# price = fruit_prices.get('grape','not available')
# print(price)

#11- Creating dictionary with letter grades
# grades = {'A':90,'B':20,'C':40}
# for key,value in grades.items():
#     print(key,value)

#12- creating a dictionary with numbers as a keys and their squares as values.
# squares_dict = {x:x**2 for x in range(1,6)}
# print (squares_dict)

#13- Creating a list of items for shopping.
# shopping_list = ['apple','banana','vegetables','bread','curd']
# shopping_list.append('milk')
# shopping_list.remove('banana')
# print (shopping_list)

#14- Creating a list of tuples contining student_name and scores.
# students = {('Babli',90),('Ritika',90),('Aarti',85)}
# student_dict = {name:score for name , score in students}
# for name , score in student_dict.items():
#     if score > 70:
#         print(name)
