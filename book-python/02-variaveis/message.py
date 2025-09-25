message = 'Hello World!'
print(message)
print(message.upper())
print(message.lower())
print(message.title())
print(message.replace('World', 'Python'))
print(message.split())
print(message[0:5])  # Slicing to get 'Hello'
print(message[-6:])  # Slicing to get 'World!'
print(message.find('World'))  # Find the index of 'World'
print(message.count('o'))  # Count occurrences of 'o'
print(len(message))  # Length of the message
print(message.startswith('Hello'))  # Check if it starts with 'Hello'
print(message.endswith('!'))  # Check if it ends with '!'
print(message.isalpha())  # Check if all characters are alphabetic
print(message.isalnum())  # Check if all characters are alphanumeric
print(message.isdigit())  # Check if all characters are digits
print(message.strip())  # Remove any leading/trailing whitespace
print(message.capitalize())  # Capitalize the first letter
print(message.swapcase())  # Swap case of all letters
print(message.center(50, '-'))  # Center the message with padding
print(message.ljust(50, '-'))  # Left justify the message with padding
print(message.rjust(50, '-'))  # Right justify the message with padding
print(message.split(' '))  # Split the message by spaces
print(' '.join(['Hello', 'Python', message]))  # Join a list into a string with spaces
print(message.partition('World'))  # Partition the string around 'World'
#print(message.rpartition('World'))  # Right partition the string around 'World'
#print(message.zfill(20))  # Zero-fill the message to a width of 20
#print(message.format())  # Format the message (no placeholders to fill)
#print(message.format_map({'name': 'Python'}))  # Format with a mapping
#print(message.casefold())  # Casefold the message for case-insensitive comparisons
#print(message.removeprefix('Hello '))  # Remove prefix 'Hello '
#print(message.removesuffix('!'))  # Remove suffix '!'
#print(message.translate(str.maketrans('', '', 'aeiou')))  # Remove vowels
#print(message.encode('utf-8'))  # Encode the message to bytes using UTF-8
#print(message.decode('utf-8'))  # Decode the bytes back to string (if it were bytes)
#print(message.isprintable())  # Check if all characters are printable
#print(message.expandtabs(4))  # Expand tabs in the message (if any)
#print(message.rfind('o'))  # Find the last occurrence of 'o'
#print(message.index('World'))  # Get index of 'World', raises error if not found
#print(message.rindex('o'))  # Get last index of 'o', raises error if not found
#print(message.splitlines())  # Split the message into lines (if it had newlines)
#print(message.isascii())  # Check if all characters are ASCII
#print(message.casefold())  # Casefold for case-insensitive comparison
#print(message.format_map({'greeting': 'Hello', 'object': 'World'}))  # Format with a mapping
#print(message.removeprefix('Hello '))  # Remove prefix 'Hello '
#print(message.removesuffix('!'))  # Remove suffix '!'
#print(message.translate(str.maketrans('', '', 'aeiou')))  # Remove vowels
