class Profile():
    
    def __init__(self, name, pw=None, status = "user", liste_score = {}) :
        self.name = name
        self.pw = pw
        self.liste_score = liste_score

    def get_pw(self):
        return self.pw
        
    def set_score(self, quiz, score):
         self.liste_score[quiz] = score
        




