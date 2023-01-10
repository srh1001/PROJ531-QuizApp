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
        return None

def sign_out():
    print("Deconnexion réussie")

def home_page(profile):

    current_user.get_stats()

    if profile.get_status() == "admin":
        choose_or_create_quiz()
        
    else:
        q = choose_quiz()
        all_quizzes[q].launch_quiz()
    
    home_page(profile)



def choose_or_create_quiz():
    p = input("Create a quiz -a  |  Choose an existant quiz -b")
    if p == "b":
        choose_quiz()
    elif p == "a":
        path = input("File directory : ")
        quiz_name = input("Quiz name : ")
        create_quiz_file(path)
        print("Quiz", all_quizzes[quiz_name], "created")
        choose_or_create_quiz()
    else:
        print("Incorrect input")
        choose_or_create_quiz()


def choose_quiz():
    print(all_quizzes.keys())
    return input("What quiz do you want to do ? : ")


while True:
    p = page_connection()
    if p == "a":
        current_user = sign_in()
        if current_user == None :
            f"No account was found."
        else:
            current_user.show_stats()

            if current_user.get_status() == "admin":
                choose_or_create_quiz()
                
            else:
                q = choose_quiz()
                all_quizzes[q].launch_quiz()


    elif p == "b": 
        f"Create your account : "
        create_account()
    else: 
         break