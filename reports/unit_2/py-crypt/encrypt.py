#!/usr/bin/env python3

import string


# part 1
def sec_key():
    words = [
        "hello",
        "world",
        "encryption",
        "someonecracedmypassword",
        "poorsecurityhurtseveryone",
    ]
    result = []
    for word in words:
        result.append(encrypt(word, "secretkey"))

    return result


def bs():
    words = [
        "srnabepakm",
        "ciubrxhrvm",
        "cvsbcjtcmqqrt",
        "qfozfwvukqhlilrbfwoekgcaf",
        "uyeyhavkuzcjowofwmfplwjrskhmyssywwu",
    ]
    result = []
    for word in words:
        result.append(decrypt(word, "brainstation"))

    return result


# clean input
def strip_ws(message: str, key: str) -> tuple:
    message = message.replace(" ", "")
    key = key.replace(" ", "")
    return message, key


# match length of key and message
def set_len(message: str, key: str) -> str:
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


# find alphabetical index
def calc_offset(message: str, key: str) -> dict:
    key = set_len(message, key)
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


# use alphabetical index to encrypt
def encrypt(message: str, key: str) -> str:
    off_dict = calc_offset(message, key)
    new_msg = ""
    for row in range(len(message)):
        new_msg += string.ascii_lowercase[
            (off_dict["key"][row] + off_dict["message"][row]) % 26
        ]
    return new_msg


# use alphabetical index to decrypt
def decrypt(message: str, key: str) -> str:
    off_dict = calc_offset(message, key)
    new_msg = ""
    for row in range(len(message)):
        new_msg += string.ascii_lowercase[
            # order is important
            (off_dict["message"][row] - off_dict["key"][row])
            % 26
        ]
    return new_msg


# capture user input
if __name__ == "__main__":
    part = input("Part 1 or 2: ")
    if part == "1":
        print(sec_key(), bs())
    elif part == "2":
        choice = input("Encrypt(1) or Decrypt(2): ")
        message = input("Enter message: ")
        key = input("Enter key: ")
        message, key = strip_ws(message, key)
        if choice == "1":
            print("Encrypting...")
            print(encrypt(message, key))
        elif choice == "2":
            print("Decrypting...")
            print(decrypt(message, key))
        encrypt_message = encrypt(message, key)
    else:
        print("error")
