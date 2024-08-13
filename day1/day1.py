# trebuchet

import re

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9',
          'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
number_words = {
    '1':1, 'one': 1, '2': 2, 'two': 2, '3': 3,'three': 3, '4': 4,'four': 4,
    '5': 5, 'five': 5, '6': 6,'six': 6, '7': 7,'seven': 7, '8': 8,'eight': 8, '9': 9, 'nine': 9,
}

def get_digits(line):
    digits = re.findall(r'\d', line)
    if digits:
        return digits[0], digits[-1]
    return None, None

def get_string_digits(line, words):
    matches = []
    positions = []

    for word in words:
        start = 0
        while True:
            start = line.find(word, start)
            if start == -1:
                break
            positions.append((start, word))
            start += len(word) 
    positions.sort()
    matches = [word for _, word in positions]
    print(matches)
    return matches

def trebuchet(option, file):
    file = open(file, "r").readlines()
    sum = 0

    for line in file:
        digit1 = 0
        digit2 = 0

        if option == "int":
            digit1, digit2 = get_digits(line)  
            combined_digit = int(digit1 + digit2)
            sum += combined_digit
        elif option == "string": 
            matches = get_string_digits(line, digits)  
            combined_digit = int(str(number_words[matches[0]]) + str(number_words[matches[-1]]))
            sum += combined_digit
    print("Sum: ", sum)

trebuchet("int", "day1/puzzle-1.txt")
trebuchet("string", "day1/puzzle-1.txt")