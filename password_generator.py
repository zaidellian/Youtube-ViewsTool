import random
import string


lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation

# function to generate the password
def generate_password(length):
    # combine all character sets
    all_characters = lowercase + uppercase + digits + special_characters
    
    # ensure the password has at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_characters)
    ]
    
    # fill the remaining length of the password
    password += random.choices(all_characters, k=length - 4)
    
    # shuffle the password list to ensure randomness
    random.shuffle(password)
    
    # convert the list to a string
    return ''.join(password)

# the main statments
if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))
        if length < 4:
            print("Password length should be at least 4 characters.")
        else:
            password = generate_password(length)
            print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")
