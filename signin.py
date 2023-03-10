import getpass
from profile import * 
from signup import *
from createquiz import *


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
        print("No account was found")
        return None


def home_page(profile):

    profile.get_stats()

    if profile.get_status() == "admin":
        choose_or_create_quiz()
        
    else:
        q = choose_quiz()
        all_quizzes[q].launch_quiz()
    
    home_page(profile)



def choose_or_create_quiz(profile):
    p = input("Create a quiz -a  |  Choose an existant quiz -b  |  Sign out -/d : ")
    if p == "b":
        q = choose_quiz()
        if q in all_quizzes:
            score = all_quizzes[q].launch_quiz()
            profile.set_score(q, score)
            overwrite_profile(all_profiles)

            print()
        else:
            print("Incorrect input")
            
    elif p == "a":
        p = input("Import a file -a  |  Create with python -b  :  ")
        if p == "a":
            path = input("File directory : ")
            quiz_name = input("Quiz name : ")
            create_quiz_file(path)
            print("Quiz", all_quizzes[quiz_name], "created")
        elif p == "b":
            create_quiz()
        elif p=="/d":
            game()

    elif p == "/d":
        game()          
    else:
        print("Incorrect input")
        choose_or_create_quiz()


def choose_quiz():
    print("Quizzes currently available : ")
    for e in all_quizzes:
        print(e)
    print()
    return input("What quiz do you want to do ? : ")


def game():
    while True:
        p = page_connection()
        if p == "a":
            current_user = sign_in()
            if current_user == None :
                f"No account was found."
            else:
                while True :
                    current_user.show_stats()

                    if current_user.get_status() == "admin":
                        choose_or_create_quiz(current_user)
                        
                    else:
                        q = choose_quiz()
                        if q == "/d":
                            game()
                        elif q in all_quizzes:
                            score = all_quizzes[q].launch_quiz()
                            current_user.set_score(q, score)
                            overwrite_profile(all_profiles)
                            print()
                        else:
                            print("Incorrect input")


        elif p == "b": 
            f"Create your account : "
            create_account()
        else: 
            f"error"
            break

game()