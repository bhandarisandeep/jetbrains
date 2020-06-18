# Write your code here
import random


def get_score(list):
    # print(list)
    # creating a dic based on the
    score_dic = {}
    for line in list:
        line = line.replace("\n", "")
        line = line.split(" ")
        # print(line[0])
        # print(line[1])
        score_dic[line[0]] = line[1]
    return score_dic


def update_score(score_dic):
    score = open('rating.txt', 'w+', encoding='utf-8')
    for name,points in score_dic.items():
        print(name,str(points), sep=" ",file=score)
    score.close()


rps_win = {"rock": "paper",
           "paper": "scissors",
           "scissors": "rock"}

rps_lose = {"rock": "scissors",
            "paper": "rock",
            "scissors": "paper"}

var = ["win", "loose", "draw"]
user_name = input("Enter your name: ")
print("""Hi you know the rules of rock,paper and scissors !!! \n pretty simple huh ! \n
 So there are a few simple things to follow in command line:
 1. !rating : To check your score.
 2. !exit : To leave the game in between.
 3. Rest type the options from the rock,,paper and scissors and play the infinite game.
 4. Your score is saved in the file and every time you play the game it will be resumed from the last saved. 
 """)
score = open('rating.txt', 'a+', encoding='utf-8')
score.close()
score = open('rating.txt', 'r+', encoding='utf-8')
score_list = score.readlines()
score_dic = get_score(score_list)
score.close()
# print(score_dic)
if user_name in score_dic.keys():
    print('Hello {} your last saved score is : {}'.format(user_name, score_dic[user_name]))
else:
    print('Hello', user_name)
    score_dic[user_name] = 0
print("\nSo let's start ;-) \n")
# print(score_dic) # checking all the people score
user_chose = input()
while user_chose != "!exit":
    win_or_loose = random.choice(var)
    # print(win_or_loose)
    if user_chose not in ('rock', 'paper', 'scissors', '!rating'):
        print('Invalid input')
    elif user_chose == "!rating":
        print('Your rating: ',score_dic[user_name])
    elif win_or_loose == "win":
        print(f'Well done. Computer chose {rps_lose[user_chose]} and failed ')
        score_dic[user_name] = int(score_dic[user_name]) + 100
    elif win_or_loose == "loose":
        print(f'Sorry, but computer chose {rps_win[user_chose]}')
    else:
        print(f'There is a draw ({user_chose})')
        score_dic[user_name] = int(score_dic[user_name]) + 50
    user_chose = input()

print("Bye!")

update_score(score_dic)
