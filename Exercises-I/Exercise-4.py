'''
Exercise 4:

Remove the duplicate characters from the String and print it
Sample Output:
The given string is: resources
After removing duplicates characters the new string is: resouc
'''



def remove_duplicate_characters(string):
    formatted = ""

    for char in string:
        if char not in formatted: # We check if the character is not already in the result string (formatted)
            formatted += char
    print(formatted)

while True:
    string = input("Remove duplicate characters from: ")
    remove_duplicate_characters(string)

