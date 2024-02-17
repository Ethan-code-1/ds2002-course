#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

import os 

os.environ["BEST_SPORT"] = input('What sport is the best? ')
os.environ["BEST_LANG"] = input('What coding language is the best? ')
os.environ["FIRST_DORM"] = input('What was your first year dorm? ')

SPORT_ENV = os.getenv("BEST_SPORT")
LANG_ENV = os.getenv("BEST_LANG")
DORM_ENV = os.getenv("FIRST_DORM")

print("")

print("Sport was:", SPORT_ENV)
print("Language was:", LANG_ENV)
print("Dorm was:", DORM_ENV)