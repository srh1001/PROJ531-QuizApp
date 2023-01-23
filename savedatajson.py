import json
from profile import *
from quiz import *

# Obj python to Json :    
    
def append_to_json(_dict,path): 
    with open(path, 'ab+') as f:
        f.seek(0,2)                                #Go to the end of file    
        if f.tell() == 0 :                         #Check if file is empty
            f.write(json.dumps([_dict]).encode())  
        else :
            f.seek(-1,2)           
            f.truncate()                           
            f.write(' , '.encode())                #Write the separator
            f.write(json.dumps(_dict).encode())    
            f.write(']'.encode())                 
    
def profile_to_send_to_json(obj):
    #if isinstance(obj, Profile):
        profile = {"name": obj.name, "pw": obj.get_pw(), "status": obj.get_status(), "liste_score": obj.liste_score}
        append_to_json(profile, "C:/Users/srhmr/Downloads/data_json/dataAllProfiles.json")

def quiz_to_send_to_json(obj):

  #  elif isinstance(obj, Quiz):
        quiz = {"name": obj.name, "questions": obj.quest, "reponses": obj.rep, "reponses_c": obj.rep_c, "point": obj.point}
        append_to_json(quiz, "C:/Users/srhmr/Downloads/data_json/dataAllQuizzes.json")        
    

# Json to obj python :       
      
def extract_json_profile(path, all_profiles={}):
    with open(path, "r+") as f:
        l = json.loads(f.read())
        for i in range(0,len(l)):
            profile = Profile(*l[i].values())
            all_profiles[profile.name] = profile
    return all_profiles

def extract_json_quiz(path, all_quizzes={}):
    with open(path, "r+") as f:
        l = json.loads(f.read())
        for i in range(0,len(l)):
            quiz = Quiz(*l[i].values())
            all_quizzes[quiz.name] = quiz
    return all_quizzes

def overwrite_profile(_dict): 
    l = []
    for obj in _dict.values():
        p = {"name": obj.name, "pw": obj.get_pw(), "status": obj.get_status(), "liste_score": obj.liste_score}
        l.append(p)
    jsonString = json.dumps(l)
    jsonFile = open("C:/Users/srhmr/Downloads/data_json/dataAllProfiles.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()
