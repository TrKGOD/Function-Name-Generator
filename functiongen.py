import secrets
import string

def generate_random_key(size, num_digits):
    random_bytes = secrets.token_bytes(size)
    random_key = random_bytes.hex()
    
    random_digits = secrets.randbelow(10 ** num_digits)
    
    random_key = random_key[:num_digits] + str(random_digits) + random_key[num_digits+1:]
    return random_key

key_size = int(input("Amount of letters in your key: "))
num_digits = int(input("Amount of numbers in your key: "))

random_key = generate_random_key(key_size, num_digits)
print("Random Key:", random_key)
