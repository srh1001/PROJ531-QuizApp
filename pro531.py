class Quizz():
    def __init__(self, fich):
        self.fich = fich
        self.quest = []
        self.rep = []
        self.titre = ""
        self.point = []

    def lecture(self):
        file = open(self.fich, "r")
        lines = file.read().splitlines()
        self.titre = lines[0]
        self.quest = lines[1].split(',')
        self.quest.pop()
        for k in range(2, len(lines) - 1):
            self.rep.append(lines[k])
        L = lines[-1]
        self.point = L.split(';')

    def __repr__(self):
        self.lecture(self)
        print(self.titre)
        score = 0
        score_maximal = 0
        print(self.rep)
        for i in range(len(self.quest)):
            print(f"Question {i+1} :", self.quest[i])
            reponse_u = int(input("choisir le numéro de votre réponse"))
            point_i = list(map(int, self.point[i].split(",")))
            score_maximal += max(point_i)
            if point_i[reponse_u - 1] == 0:
                print("reponse fausse")
            else:
                score += point_i[reponse_u - 1]
                print(f"réponse correcte vous avez gagnez {point_i[reponse_u-1]} points")
        print(f"votre score est {score} sur {score_maximal} ")


q = Quizz('test.txt')
print(q)

