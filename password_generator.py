import string
import random

def password_generator(length=12, use_digits=True, use_special_chars=True):
    chars = string.ascii_letters # Upper and lower case letters

    if use_digits:
        chars += string.digits

    if use_special_chars:
        chars += string.punctuation
    
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == '__main__':
    length = int(input('Enter the length of the password: '))
    use_digits = input('Do you want to use digits? (y/n): ').strip().lower() == 'y'
    use_special_chars = input('Do you want to use special characters? (y/n): ').strip().lower() == 'y'

    password = password_generator(length, use_digits, use_special_chars)
    print(f"Generated password: {password}")