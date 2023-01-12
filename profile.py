class Profile():
    
    def __init__(self, name, pw=None, status = "user", liste_score = {}) :
        self.name = name
        self.pw = pw
        self.status = status
        self.liste_score = liste_score

    def get_pw(self):
        return self.pw
    
    def get_status(self):
        return self.status
        
    def set_score(self, quiz_name, score):
         self.liste_score[quiz_name] = score

    def show_stats(self):
        print("Your results so far : ")
        print("|  Quiz  |   Score  |")
        for k, v in self.liste_score.items():
            print(f"|  {k}  |   {v}  |")
        print()

        




