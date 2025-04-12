'''
Exercise 2:

Find the first most frequent character in a given string (edited)

Sample output:
The given string is : successes
The first most frequent char in the string is: s
'''

def find_most_frequent_char(string):
    most_frequent_char = max(string, key=string.count) # Apparently we can use the key=string.count in order to find the ocurrences of a character. Added in max function, we can extract the most_frequent character
    ocurrences = string.count(most_frequent_char)
    print("The most frequent char is: " + most_frequent_char + " with " + str(ocurrences) + " ocurrences" )

while True: # I chose a while true loop so the user won't need to rerun the app every time they want to check a new string
    string = input("String to identify the most frequent char: ")
    find_most_frequent_char(string)

