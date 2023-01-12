all_quizzes = {}

class Quiz():
    def __init__(self, name: str, questions: list, reponses: list[list], reponses_c: list[int], point: list[int]):
        self.name = name
        self.quest = questions
        self.rep = reponses
        self.rep_c = reponses_c
        self.point = point

    def __repr__(self):
        return self.name

    def launch_quiz(self):
        score = 0
        score_maximal = 0
        print(self.name)
        for i in range(len(self.quest)):
            print(f"Question {i+1} :", self.quest[i])
            for j in range(len(self.rep[i])):
                print(f"{j+1}) {self.rep[i][j]}", end=' ')
            print()
            reponse_u = int(input("choisir le numéro de votre réponse "))
            if (reponse_u -1) == self.rep_c[i]:
                score += self.point[i]
                print(f"Bonne réponse, vous avez gagné {self.point[i]} points ")
            else:
                print(f"Mauvaise réponse , la réponse est {self.rep[int(self.rep_c[i])-1][j]}")
            score_maximal += self.point[i]
        print(f"Quiz terminé , votre score est {score}/{score_maximal}")
        return score


def create_quiz_file(fichier: str):
    '''
    creation d une quiz a partir d un fichier
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
    
    all_quizzes[titre] = Quiz(titre, question, rep, rep_c, p)
    return all_quizzes


def create_quiz():
    '''
     creation d une quizz par l administrateur
    '''
    global all_quizzes
    titre = input("Proposez un titre du quiz : ")
    n = int(input("Proposez le nombre de questions pour le quizz "))
    questions = []
    reponses = []
    rep_c = []
    point = []
    for i in range(n):
        questions.append(input(f"Saisissez la question n°{i+1} "))
        reponses.append(input("saisissez les réponses séparés par ; ").split(";"))
        rep_c.append(int(input("saisir le numéro de la réponse correcte "))-1)
        point.append(int(input("saisir le score ")))
        print()
    
    all_quizzes[titre] = Quiz(titre, questions, reponses, rep_c, point)
    for j in range (n):
        time.sleep
    return all_quizzes

create_quiz()
