import sys

def load_numbers(file_path):
    numbers = []
    with open(file_path, 'r') as f:
        for line in f:
            # Iterate through each line in the file
            for word in line.split():
                # Iterate through each word in the line
                try:
                    # Try to convert the word to a int
                    numbers.append(int(word))
                except ValueError:
                    # If the conversion fails, the word is not a number
                    pass
    return numbers
