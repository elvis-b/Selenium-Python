
#Exercise 1
'''
Exercise 1:
Check if a given string is a palindrome or not.
'''

# First we define the method and then we utilize it in a while loop.
def isPalindrome(string):
    reversedString = string[::-1] #We reverse the String using [::-1], which takes the last character at the end and goes backwards
    if string == reversedString:  #We check if the original string equals to the reversed one
        print(string, "is a palindrome")
    else:
        print(string, "is not a palindrome")

while True: # I chose a while true loop so the user won't need to rerun the app every time they want to check a new string
    string = input("Add the string to check: ")
    isPalindrome(string)



'''
Exercise 5:

Given a String find whether it is a valid 10-digit phone number.
Number should be in format xxx-xxx-xxxx
E.g 234-456-9999
'''

'''
Exercise 6:

Find whether a number is a Perfect number
E.g A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.
For instance, 6 has divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6, so 6 is a perfect number.
'''

