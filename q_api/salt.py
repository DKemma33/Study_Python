import random
import string

salt_length = 14

def generate_salt(length):
    characters = string.ascii_letters + string.digits
    salt = ''.join(random.choice(characters) for _ in range(length))
    return salt

salt = generate_salt(salt_length)
print(salt)

