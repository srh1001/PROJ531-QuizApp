file = open('test.txt', "r")
lines = file.read().splitlines()
titre = lines[0]
quest = lines[1].split(',')
quest.pop()
reponse = []
for k in range(2, len(lines) - 1):
    reponse.append(lines[k])
L = lines[-1]
point = L.split(';')
print(titre)
score = 0
score_maximal = 0
print(reponse)
for i in range(len(quest)):
    print(f"Question {i+1} :", quest[i])
    reponse_u = int(input("choisir le numéro de votre réponse"))
    point_i = list(map(int, point[i].split(",")))
    score_maximal += max(point_i)
    if point_i[reponse_u - 1] == 0:
        print("reponse fausse")
    else:
        score += point_i[reponse_u - 1]
        print(f"réponse correcte vous avez gagnez {point_i[reponse_u-1]} points")
print(f"votre score est {score} sur {score_maximal} ")
