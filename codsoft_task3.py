import random
import array

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']

# combines all the character arrays above to form one array
COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

# take user input for the desired password length
while True:
    try:
        password_length = int(input("Enter the length of the password: "))
        if password_length <= 0:
            print("Please enter a positive integer.")
        else:
            break
    except ValueError:
        print("Please enter a valid integer.")

rand_digit = random.choice(DIGITS)
rand_upper = random.choice(UPCASE_CHARACTERS)
rand_lower = random.choice(LOCASE_CHARACTERS)
rand_symbol = random.choice(SYMBOLS)

temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

for _ in range(password_length - 4):
    temp_pass += random.choice(COMBINED_LIST)

temp_pass_list = array.array('u', temp_pass)
random.shuffle(temp_pass_list)

password = ""
for char in temp_pass_list:
    password += char

# print out password
print("Generated Password:", password)
