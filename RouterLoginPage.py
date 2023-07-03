import time
import sys
import os
from pwinput import pwinput
from os import system

system("title " + "Login Page 420.69.1.1")

logged_in = False

while logged_in == False:
    
    login = input("LOGIN: ")
    password = pwinput("PW: ", '*')

    if login == "Admin":

        if password == "admin":
            print("Login Completed!")
            time.sleep(2)
            logged_in == True
            break
            
        else:
            print("Wrong Password!")
            time.sleep(2)
            os.system("cls")
    else:
        print("Wrong Username and Password!")
        time.sleep(2)
        os.system("cls")

os.system("cls")
print(f"Welcome " + login)
time.sleep(5)


input()


