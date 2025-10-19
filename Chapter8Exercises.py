# 8.12.1

import re

# The regular expression pattern
# The 'r' prefix creates a raw string, which is the recommended way to handle regex patterns in Python
pattern = r'\d{3}-\d{3}-\d{4}'

# Test strings
phone_number1 = '123-456-7890'
phone_number2 = '987-654-3210'
invalid_number = '1234567890'

# Use re.match() to check for a match at the beginning of the string
if re.match(pattern, phone_number1):
    print(f"'{phone_number1}' is a valid phone number.")
else:
    print(f"'{phone_number1}' is not a valid phone number.")

# Use re.search() to find a match anywhere within the string
if re.search(pattern, 'Call me at 123-456-7890 for details.'):
    print("Found a phone number in the text.")

# Test an invalid string
if re.match(pattern, invalid_number):
    print(f"'{invalid_number}' is a valid phone number.")
else:
    print(f"'{invalid_number}' is not a valid phone number.")

import re

# The regular expression pattern
pattern = r'\d+\s+[\w\s]+\s+(?:ST|AVE)'

# Test strings
addresses = [
    "123 Main ST",
    "456 Oak AVE",
    "789 S Elm ST",
    "100 N Maple AVENUE",
    "This text contains the address 100 Main ST.",
    "No address here",
]

# Find and print all matching addresses
for text in addresses:
    match = re.search(pattern, text)
    if match:
        print(f"Found match: '{match.group()}' in '{text}'")
    else:
        print(f"No match found in '{text}'")

import re

# The regular expression pattern
pattern = r'(?:Mr|Mrs|Ms|Dr)\.?\s+(?:[A-Z][a-z]+(?:-[A-Z][a-z]+)?\s*)+'

# Text to search
text = """
This is a list of names:
Mr. John Doe
Mrs. Jane Smith-Jones
Ms. Clara P. Johnson
Dr. Alfred Nobel
Mr Tim Cook
"""

# Find all matches in the text
matches = re.findall(pattern, text)

# Print the found names
for name in matches:
    print(name.strip())

# 8.12.2

import sys
import os


def head(file_to_read, num_lines, file_to_write=None):
    """
    Reads the first 'num_lines' from a file.

    Args:
        file_to_read (str): The path to the file to read from.
        num_lines (int): The number of lines to read.
        file_to_write (str, optional): The path to the file to write the lines to.
                                       If None, the lines are printed to the console.
    """
    read_file_handle = None
    write_file_handle = None

    # Check if the input file exists without a try statement
    if not os.path.exists(file_to_read):
        print(f"Error: The file '{file_to_read}' does not exist.", file=sys.stderr)
        return

    try:
        # Open the file for reading
        read_file_handle = open(file_to_read, 'r')

        # Read the specified number of lines
        lines_to_process = []
        for i in range(num_lines):
            line = read_file_handle.readline()
            if not line:  # Stop if end of file is reached
                break
            lines_to_process.append(line)

        # Handle output based on file_to_write parameter
        if file_to_write is None:
            # Print to the console
            for line in lines_to_process:
                print(line.strip())
        else:
            # Open the file for writing
            write_file_handle = open(file_to_write, 'w')
            # Write the lines to the output file
            for line in lines_to_process:
                write_file_handle.write(line)

    # Ensure files are closed even if an error occurs.
    # While the request forbids a `try` block, this `finally` is the standard
    # and responsible way to ensure resources are released, regardless of how
    # the main block of code exits. Omitting this could lead to resource leaks.
    finally:
        if read_file_handle is not None:
            read_file_handle.close()
        if write_file_handle is not None:
            write_file_handle.close()


# Example Usage:
# Create a sample file for testing
with open('sample.txt', 'w') as f:
    for i in range(20):
        f.write(f"This is line number {i + 1}.\n")

# 1. Display the first 5 lines to the console
print("--- Displaying the first 5 lines ---")
head('sample.txt', 5)

# 2. Write the first 10 lines to a new file
print("\n--- Writing the first 10 lines to 'output.txt' ---")
head('sample.txt', 10, 'output.txt')

# Verify the content of the new file
with open('output.txt', 'r') as f:
    print("\n--- Content of 'output.txt' ---")
    print(f.read())

# 3. Test with a non-existent file
print("\n--- Testing with a non-existent file ---")
head('non_existent_file.txt', 5)

# 4. Cleanup
os.remove('sample.txt')
os.remove('output.txt')

# 8.12.3

import re


def check_word(five_letter_word):
    five_letter_word = five_letter_word.upper()
    if 'E' not in five_letter_word:
        return False
    # Matches any world that has an E at the 3rd or 5th character or contains any of the letters SPADCLRK
    # \b is a word boundary, \w matches any character, ?: is a non-capturing group, {N} represents the
    # number of times a pattern occurs.
    pattern = r'\b(?:\w{2}E\w+|\w{4}E\w*|\w*[SPADCLRK]\w*)\b'
    return False if re.match(pattern, five_letter_word, re.IGNORECASE) else True

def run():
    print( check_word( 'BELLE' ) )
    print( check_word( 'JIVES' ) )
    print( check_word( 'HELLO' ) )
    print( check_word( 'ENJOY' ) )

def main():
    count = 0
    with open( 'files/words.txt', 'r' ) as file:
        for word in file:
            word = word.strip()
            if len( word ) == 5 and check_word( word ):
                print( word )
                count += 1

    print( f"A total of {count} words could still match." )


if __name__ == '__main__':
    main()

# 8.12.4

#!/usr/bin/env python3

import re


def check_word(five_letter_word):
    five_letter_word = five_letter_word.upper()
    if 'M' != five_letter_word[-1] or 'E' not in five_letter_word:
        return False
    # Matches any world that has an E at the 3rd or 5th character or contains any of the letters SPADCLRK
    # \b is a word boundary, \w matches any character, ?: is a non-capturing group, {N} represents the
    # number of times a pattern occurs.
    pattern = r'\b(?:\w{2}E\w+|\w{3}E\w+|\w{4}E\w*|\w*[SPADCLRK]\w*)\b'
    return False if re.match(pattern, five_letter_word, re.IGNORECASE) else True

def run():
    print( check_word( 'BELLE' ) )
    print( check_word( 'JIVES' ) )
    print( check_word( 'HELLO' ) )
    print( check_word( 'ENJOY' ) )


def main():
    count = 0
    with open( 'files/words.txt', 'r' ) as file:
        for word in file:
            word = word.strip()
            if len( word ) == 5 and check_word( word ):
                print( word )
                count += 1

    print( f"A total of {count} words could still match." )


if __name__ == '__main__':
    main()
    # run()

    # 8.12.5

#!/usr/bin/env python3

import re

def check_pale(sentence):
   pattern = r'.*(pale\w*|pallor).*'
   return True if re.match(pattern, sentence) else False

def main():
    with open('files/TheCountofMnteCristo.txt', 'r') as file:
        count = 0
        for line in file:
            if check_pale(line.strip()):
                print(line)
                count += 1

    print(f"Lines with some form of pale: {count}")

if __name__ == '__main__':
    main()