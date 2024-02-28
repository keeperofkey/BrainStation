#!/usr/bin/env python3


import hashlib

tup_list = [
    (
        "DARYL HOWLAND",
        "husky",
        "09e28e9c5875ef3b2b7463e1c9adc3cefbd35af73283f9f9281dc9b8c48f9524",
    ),
    (
        "MARISSA FERREIRA",
        "labrador",
        "0782cb514029008de13d7e71aa1662c310b08d0d0abb29b3220466c0f3b08c1f",
    ),
    (
        "TIM SUNG",
        "beagle",
        "6573818d2ffc8a09380b22a5aa517a33cca87f54e51897ee8e64b45166a76e51",
    ),
    (
        "SIMONE OSTERMANN",
        "dachshund",
        "e05151fd4885688b44dece508de93cfcbe7cacb262d1d3999f9287014ab5bfb7",
    ),
]


def sha256(passwd):
    h = hashlib.new("sha256")
    h.update(passwd.encode("UTF-8"))
    return h.hexdigest()


def verify(hash, passwd):
    if hash == sha256(passwd):
        return True
    else:
        return False


if __name__ == "__main__":
    for tup in tup_list:
        print(verify(tup[2], tup[1]))
