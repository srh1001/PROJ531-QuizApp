class Profile():
    
    def __init__(self, name, pw=None, status = "user", liste_score = {"test":0}) :
        self.name = name
        self.pw = pw
        self.status = status
        self.liste_score = liste_score

    def get_pw(self):
        return self.pw
    
    def get_status(self):
        return self.status
        
    def set_score(self, quiz, score):
         self.liste_score[quiz] = score

    def show_stats(self):
        print("|  Quiz  |   Score  |")
        for k, v in self.liste_score.items():
            f"|  {k}  |   {v}  |"

        




