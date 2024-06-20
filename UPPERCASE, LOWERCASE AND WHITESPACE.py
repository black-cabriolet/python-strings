#Upper Case
a = "Hello, World!"
print(a.upper())

#LOWERCASE
a = "Hello, World!"
print(a.lower())

#REMOVING WHITESPACE
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Replace String
a = "Hello, World!"
"""
H is replaced with J
"""
print(a.replace("H", "J"))

#Split String
"""The split() method returns a list where the text between the specified separator becomes the list items."""
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
