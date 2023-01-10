import getpass
from profile import * 
from signup import *

def page_connection():
    return input("Se connecter -a | Créer un compte -b : ")


def sign_in():
    pseudo = input("Pseudo : ")
    if pseudo in (all_profiles):
        while True:
            pw = getpass.getpass("Password : ")
            current_user = all_profiles[pseudo]
            if pw == current_user.get_pw():
                return current_user
            else:
                print("Incorrect password.")
    else:
        print("No account was found.")
        page_connection()

def choose_or_create_quiz():


def choose_quiz():
    print(all_quizzes.keys())
    return input("What quiz do you want to do ? : ")


while True:
    p = page_connection()
    if p == "a":
        current_user = sign_in()
        # current_user.get_stats()
        if current_user.get_status() == "admin":
            # create_quiz()
            
        else:
        # q = choose_quiz()
        # all_quizzes[q].launch_quiz()
        break

    elif p == "b": 
        f"Create your account : "
        create_account()
    else: 
        break