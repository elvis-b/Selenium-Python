
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