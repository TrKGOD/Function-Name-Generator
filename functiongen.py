import secrets
import string

def generate_random_key(size, num_digits, num_special_chars):
    random_bytes = secrets.token_bytes(size)
    random_key = random_bytes.hex()
    
    random_special_chars = ''.join(secrets.choice(string.punctuation) for _ in range(num_special_chars))
    random_digits = secrets.randbelow(10 ** num_digits)
    
    random_key = random_special_chars + random_key[:num_digits] + str(random_digits) + random_key[num_digits+1:]
    return random_key

key_size = int(input("Amount of letters in your key: "))
num_digits = int(input("Amount of numbers in your key: "))
num_special_chars = int(input("Amount of special characters in your key: "))

random_key = generate_random_key(key_size, num_digits, num_special_chars)
print("Random Key:", random_key)
