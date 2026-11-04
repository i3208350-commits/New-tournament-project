from email.charset import add_alias
from shlex import split
import functions as f
import utils as u
import loggin

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
itam_matches=[]

matches={
    "home_team_id":0,
    "away_team_id":0,
    "home_goals":0,
    "away_goals":0}
def menu():
    while True:


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
        try:

            choice=int(input("Tap your choice"))


            if choice==1:
                f.add_team()
                continue
            if choice==2:
                f.show_all_teams()
                continue
            if choice==3:
                f.add_match_result()
                continue
            if choice==4:
                f.Show_standings()
                continue
            if choice==5:
                f.Show_leading_team()
                continue
            if choice==6:
                f.Show_best_attacking_team()
                continue
            if choice==7:
                f.Show_team_success_rate()
            if choice==8:
                f.Show_teams_without_wins()
            if choice==9:
                f.Show_tournament_summary()
            if choice == 10:
                f.Check_championship_potential()

            if choice==0:
                  break
        except:
               menu()














# f.add_team(itams)
# f.add_team(itams)
# print(itams)
# f.add_team(itams)

# f.show_all_teams(itams)






if __name__=="__main__":
       menu()
