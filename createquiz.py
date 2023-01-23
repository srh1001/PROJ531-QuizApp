import os
from quiz import *
from savedatajson import *

if os.path.exists("C:/Users/srhmr/Downloads/data_json/dataAllQuizzes.json"):
    all_quizzes = extract_json_quiz("C:/Users/srhmr/Downloads/data_json/dataAllQuizzes.json")
else:
    all_quizzes = {}

def create_quiz_file(fichier: str):
    '''
    creation d un quiz a partir d un fichier txt
    '''
    global all_quizzes
    file = open(fichier, "r")
    lines = file.read().splitlines()
    titre = lines[0]
    question = lines[1].split(';')
    rep = []
    for k in range(2, len(lines) - 1):
        rep.append(lines[k].split(';'))
    point = lines[-1].split(';')
    rep_c = []
    p = []
    for tu in point:
        t = list(map(int, tu.split(',')))
        rep_c.append(t[0])
        p.append(t[1])

    quiz = Quiz(titre, question, rep, rep_c, p)
    all_quizzes[titre] = quiz
    quiz_to_send_to_json(quiz)

    return quiz


def create_quiz():
    '''
     creation d une quizz par l administrateur
    '''
    global all_quizzes
    titre = input("Proposez un titre du quiz : ")
    while True:
        try:
            n = int(input("Proposez le nombre de questions pour le quiz : "))
        except:
            print("Veuillez saisir un nombre.")
        else:
            break
    questions = []
    reponses = []
    rep_c = []
    point = []
    for i in range(n):
        questions.append(input(f"Saisissez la question n°{i+1} "))
        reponses.append(input("saisissez les réponses séparés par un ; : ").split(";"))
        while True:
            try:
                rep_c.append(int(input("saisir le numéro de la réponse correcte : "))-1)
            except:
                print("veuillez saisir un nombre")
            else:
                break
        while True:
            try:
                point.append(int(input("Saisir le score : ")))
            except:
                print("Veuillez saisir un nombre.")
            else:
                break
        print()
    
    quiz = Quiz(titre, questions, reponses, rep_c, point)
    all_quizzes[titre] = quiz
    quiz_to_send_to_json(quiz)

    return quiz



