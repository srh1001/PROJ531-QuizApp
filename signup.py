import os
import getpass
from savedatajson import *
from profile import *

all_profiles = extract_json_profile("C:/Users/srhmr/Downloads/all_test_json/data_all_profiles.json")


if os.path.exists("C:/Users/srhmr/Downloads/all_test_json/data_all_quizzes.json"):
    all_profiles = extract_json_profile("C:/Users/srhmr/Downloads/all_test_json/data_all_profiles.json")
else:
    all_profiles = {}

def create_account():
    global all_profiles
    pseudo = input("Choose your pseudo : ")

    if pseudo not in all_profiles.keys():
        pw = getpass.getpass("Choose your password : ")
        profile = Profile(name = pseudo, pw = pw)
        all_profiles[pseudo] = profile
        profile_to_send_to_json(profile)

    else:
        print("Username unavailable.")
