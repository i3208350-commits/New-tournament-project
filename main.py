from email.charset import add_alias
from shlex import split
import functions as f
import utils as u

teams = []
matches = [{
            "home_team_id":0,
            "away_team_id":0,
            "home_goals:":0,
            "away_goals:":0

           }]

# team = {
#     "id": 1,
#     "name":0,
#     "played":0,
#     "wins":0,
#     "draws":0,
#     "losses":0,
#     "goals_for":0,
#     "goals_againts":0,
#     "ponits":0}
itams=[]

matches={
    "home_team_id":0,
    "away_team_id":0,
    "home_goals":0,
    "away_goals":0}
def menu():


    print("1. Add team")
    print("2. Show all teams")
    print("3. Add match result")
    print("4. Show standings")
    print("5. Show leading team")
    print("6. Show best attacking team")
    print("7. Show team success rate")
    print("8. Show teams without wins")
    print("9. Show tournament summary")
    print("10.Check championship potential")
    print("0. Exit Choose an option:     ")

    choice=int(input("Tap your choice"))
    # while True:
    #     if choice==0:
    #           break

    if choice==1:
            f.add_team()

    if choice==2:
            f.show_all_teams()
    if choice==3:
        f.add_match_result()
    if choice==4:
        f.Show standings()













# f.add_team(itams)
# f.add_team(itams)
# print(itams)
# f.add_team(itams)

# f.show_all_teams(itams)






if __name__=="__main__":
       menu()
