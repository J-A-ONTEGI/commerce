import string
import random

def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))