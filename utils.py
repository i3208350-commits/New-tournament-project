import main as m
import loggin
def a_test_that_is_filled(x):
    if x=="":
        return False
    else:
        return True


def positive_integers(x):
    if not isinstance(x,int):
        print("You did not submit a whole number.")
        m.menu()
    if x<0:
        print("You did not submit a positive number_1.")
        m.menu()
    else:
        return True

def Group_testing(x):
    for i in m.itams:
        if i["name"]==x:
            return True
        else:
            return False
def id_testing(x):
    for i in m.itams:
        if i["id"]==x:
            return True
        else:
            return False
def loading_data(x):

    for i in m.itams:
        wins=0
        if m.matches["home_goal"]>m.matches["away_goals"]:
            wins=1
        if m.matches["home_goal"]<m.matches["away_goals"]:
            wins=2
       
        if i[id]==m.matches["home_team_id"]:
            i["played"]+=1
            i["goals_againts"]+=m.matches["home_goal"]
            i["goals_for"]+=m.matches[ "away_goals"]
            if wins==1:
                i["wins"]+=1
                i["ponits"]+=3
            if wins==0:
                i["draws"]+=1
                i["ponits"]+=1
                  
        
        if i[id]==m.matches["away_team_id"]:
            i["played"]+=1
            i["goals_againts"]+=m.matches["away_goals"]
            i["goals_for"]+=m.matches["goals_for"]
            if wins==2:
                i["wins"]+=1
                i["ponits"]+=3
            if wins==0:
                i["draws"]+=1
                i["ponits"]+=1

def Check_if_you_played(x,v):
    for i in m.itam_matches:
        if i["home_team_id"]==x["home_team_id"] and i["away_team_id"]== v["away_team_id"] or i["away_team_id"]==x["home_team_id"] and i["home_team_id"]== v["away_team_id"]:
            return False

        else:
            return True

def Show_team_success_rate():
    for i in m.itams:
               if i["ponits"]==0:
                   print("No games")
               else:
                   print( sorted(i["ponits"] / (["played"] * 3) * 100))

# def Show_teams_without_wins():







