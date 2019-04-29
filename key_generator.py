__author__ = 'jayaimzzz'

import argparse
import hashlib, binascii
import random

password = b'letmein'
random_num_min= 0
random_num_max= 1000

def generate_random_key():
    salt = bytes(random.randint(random_num_min,random_num_max))
    dk = generate_key(salt)
    return dk

def generate_key(salt):
    key = hashlib.pbkdf2_hmac('sha256',password,salt, 1000)
    return key.hex()

def validate_key(key):
    isValid = False
    for i in range(random_num_min,random_num_max):
        salt = bytes(i)
        dk = generate_key(salt)
        if dk == key:
            isValid = True
            break
    return isValid
        


def create_parser():
    parser = argparse.ArgumentParser(description="Generate a unique key or validate a key")
    parser.add_argument('-g','--generatekey', help='generates one key', action='store_true')
    parser.add_argument('-v','--validatekey', help='validates key provided', action='store_true')
    parser.add_argument('-key', help='The key needing validation', type=str, required=False)
    return parser

if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    if args.validatekey and not args.key:
        print("Key must be provided when validating. Example: -v -key keyToValidate")
        exit()
    if args.generatekey:
        print(generate_random_key())
        exit()
    if args.validatekey and args.key:
        isValid = validate_key(args.key)
        if isValid:
            print("Key is Valid")
        else:
            print("Key is NOT Valid")
    
    