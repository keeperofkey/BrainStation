#!/usr/bin/env python3

import string


def set_len(key: str) -> str:
    if len(message) > len(key):
        key = key * (len(message) // len(key))
        if len(message) % len(key) != 0:
            add = len(message) % len(key)
            key += key[:add]
        return key
    elif len(message) < len(key):
        key = key[: len(message)]
        return key
    elif len(message) == len(key):
        return key
    else:
        return "error"


def calc_offset(message: str, key: str) -> dict:
    key = set_len(key)
    key_arr = []
    message_arr = []
    for i in range(len(key)):
        int_idx = string.ascii_lowercase.index(key[i])
        key_arr.append(int_idx)

    for i in range(len(message)):
        int_idx = string.ascii_lowercase.index(message[i])
        message_arr.append(int_idx)

    mydict = {
        "key": key_arr,
        "message": message_arr,
    }
    return mydict


def encrypt(message: str, key: str) -> str:
    # apply Vigenere cipher to message using Key
    off_dict = calc_offset(message, key)
    new_msg = ""
    for row in range(len(message)):
        new_msg += string.ascii_lowercase[
            (off_dict["key"][row] + off_dict["message"][row]) % 26
        ]
    return new_msg


def decrypt(message: str, key: str) -> str:
    # apply Vigenere cipher to message using Key
    off_dict = calc_offset(message, key)
    new_msg = ""
    for row in range(len(message)):
        new_msg += string.ascii_lowercase[
            (off_dict["message"][row] - off_dict["key"][row]) % 26
        ]
    return new_msg


if __name__ == "__main__":
    choice = input("Encrypt(1) or Decrypt(2): ")
    message = input("Enter message: ")
    key = input("Enter key: ")
    if choice == "1":
        print("Encrypting...")
        print(encrypt(message, key))
    elif choice == "2":
        print("Decrypting...")
        print(decrypt(message, key))
    encrypt_message = encrypt(message, key)
