import getpass
from profile import *

all_profiles = {}

def create_account():
    global all_profiles
    pseudo = input("Choose your pseudo : ")

    if pseudo not in all_profiles.keys():
        pw = getpass.getpass("Choose your password : ")
        all_profiles[pseudo] = Profile(name = pseudo, pw = pw)
    else:
        print("Username already taken.")

