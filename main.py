def authenticate():
    while True:
        password = input("Enter the password: ")
        if password == "Cherie94":
            print("Authentication successful!")
            return True
        elif not password:
            print("Password cannot be empty. Please try again.")
        else:
            print("Authentication failed. Please try again.")


if authenticate():
    # Your protected code here
    print("Welcome to the protected area!")
else:
    print("Access denied.")

# go on

import locale

# Set the locale to Arabic (assuming the system supports it)
locale.setlocale(locale.LC_ALL, 'arabic')

def arabic_letter_value(letter):
    letter = letter.lower()
    arabic_letters = {
        'ا': 1, 'ب': 2, 'ت': 400, 'ث': 500, 'ج': 3, 'ح': 8, 'خ': 600, 'د': 4,
        'ذ': 700, 'ر': 200, 'ز': 7, 'س': 60, 'ش': 300, 'ص': 90, 'ض': 800,
        'ط': 9, 'ظ': 900, 'ع': 70, 'غ': 1000, 'ف': 80, 'ق': 100, 'ك': 20,
        'ل': 30, 'م': 40, 'ن': 50, 'ه': 5, 'و': 6, 'ي': 10
    }
    return arabic_letters.get(letter, 0)

def calculate_arabic_word_value(word):
    total_value = 0
    for letter in word:
        total_value += arabic_letter_value(letter)
    return total_value

def derive_number(value):
    while value >= 10:
        value = sum(int(digit) for digit in str(value))
    return value

if __name__ == "__main__":
    # Set UTF-8 encoding for input/output
    import sys
    if sys.stdout.encoding != 'utf-8':
        sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

    while True:
        # Example usage:
        word = input("Enter an Arabic word: ")
        value = calculate_arabic_word_value(word)
        powerful_number = value ** 2
        magical_number = powerful_number * 7
        derived_number = derive_number(value)

        print("The numerical value of the word '{}' is: {}".format(word, value))
        print("The derived number of the numerical value is: {}".format(derived_number))
        print("The powerful number of the numerical value is: {}".format(powerful_number))
        print("The magical number is: {}".format(magical_number))

        input("Press Enter to continue...")
