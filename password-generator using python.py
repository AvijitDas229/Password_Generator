import random

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"

while 1:
    pass_len=int(input("Length of password you want? : "))
    pass_count=int(input("How many passwords do you want? : "))
    for x in range(0,pass_count):
        password = ""
        for x in range(0,pass_len):
            pass_char = random.choice(chars)
            password  = password + pass_char
        print("Here is your password : ")
        print(password)

