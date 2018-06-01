# generates random key
# https://stackoverflow.com/a/2257449

import string
import random

def generate_key(size=8, chars=string.ascii_uppercase +    string.ascii_lowercase + string.digits):

    return ''.join(random.choice(chars) for _ in range(size))
