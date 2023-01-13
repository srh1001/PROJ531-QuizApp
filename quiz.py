import time

class Quiz():
    def __init__(self, name: str, questions: list, reponses: list[list], reponses_c: list[int], point: list[int]):
        self.name = name
        self.quest = questions
        self.rep = reponses
        self.rep_c = reponses_c
        self.point = point

    def __repr__(self):
        return self.name
    def calculate_time(self,t1,t2):
        s=int(t2-t1)
        h=0
        m=0
        if s//3600!=0:
            h=s//3600
            s=s%3600
        if s%60!=0:
            m=s//60
            s=s%60
        if h==0:
            if m==0:
                return f"{s} secondes"
            else:
                return f"{m} minutes {s} secondes"
        else:
            return f"{h} heures {m} minutes {s} secondes"

    def launch_quiz(self):
        t1=time.time()
        score = 0
        score_maximal = 0
        print(self.name)
        for i in range(len(self.quest)):
            print()
            print(f"Question {i+1} :", self.quest[i])
            for j in range(len(self.rep[i])):
                print(f"{j+1}) {self.rep[i][j]}", end=' ')
            print()
            while True:
                try:
                    reponse_u=int(input("choisir le numéro de votre réponse : "))
                except:
                    print("saisir un nombre valide")
                else:
                    if reponse_u>len(self.rep[i]) or reponse_u<=0:
                        print("saisir un nombre valide.")
                    else:
                        break
            if (reponse_u-1) == self.rep_c[i]:
                score += self.point[i]
                print(f"Bonne réponse, vous avez gagné {self.point[i]} points ")
            else:
                print(f"Mauvaise réponse , la réponse est {self.rep[i][int(self.rep_c[i])-1]}")
            score_maximal += self.point[i]
        t2=time.time()
        print(f"Quiz terminé , votre score est {score}/{score_maximal} en {self.calculate_time(t1,t2)}")
        return score

