#1- Check whether a string is a palindrome
# def is_palindrome(s):

#     s=s.lower()
#     if s == s[::-1]:
#         return True
#     else :
#         return False
# print (is_palindrome("Madam"))   

#2- Count the number of vowels in a given string.
# def count_vowels(s):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in s:
#         if char in vowels:
#             count += 1
#     return count
# print(count_vowels("HELLO WORLD"))  

#3- Find the length of a string without using len()
# def string_length(s):
#     count = 0
#     for char in s:
#         count += 1 
#     return count
# print (string_length("sakshi"))    

#4- Covert a string to uppercase and lowercase
# def convert_string(s):
#     upper_case = s.upper()
#     lower_case = s.lower()
#     return upper_case , lower_case
# print(convert_string("Sakshi Gusain"))

#5- Find the first occurence of a substring in a string
# def find_substring(s,substring):
#     index = s.find(substring)
#     return index
# print(find_substring("Sakshi Gusain","Gusain"))

#6- Replace all occurences of a word in a string.
# def replace_word(s,old_word,new_word):
#   return s.replace(old_word,new_word)
# print(replace_word("Hello world","world","everyone"))    

#7- Reverse a string
# def reverse_string(s):
#     return s[::-1]
# print(reverse_string("Hello"))

#8- Count the numbers of words in a sentence
# def count_word(sentence):
#     word = sentence.split()
#     return len(word)
# print(count_word("This is a simple sentence."))

#9- Capitilize the first letter of each word(title case)
# def title_case(sentence):
#     words = sentence.split()
#     capitalized_words = [word.capitalize() for word in words]
#     return ' '.join(capitalized_words)
# print(title_case("hello world"))

     