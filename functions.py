import main as m
import utils as u
import loggin






def add_team():

    team = {
        "id": 0,
        "name": None,
        "played": 0,
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_againts": 0,
        "ponits": 0}
    
    

    try:
        add_1=input("Enter the name of the group")
        if u.a_test_that_is_filled(add_1):
            add_1 = add_1.lower()
            for i in m.itams:
                if i["name"]==add_1:
                    print ("The name exists in the system")
                    return

            team["name"] = add_1
            name_id=int(input("Enter the name id"))
            if u.a_test_that_is_filled(name_id):
                for i in m.itams:
                    if i["id"] == name_id:
                        print("The name id exists in the system")
                team["id"]=name_id
            m.itams.append(team)
        print("Successfully inserted")
           
    except:
        print("Data entry error")
        add_team()



def show_all_teams():
        if not m.itams:
              print("empty list")
              return
        else:
           for i in m.itams:
           
                print(f"The group name is {i["name"]}")
                print(f"id = {i["id"]}")
                print(f"Number of games= {i["played"]}")
                print(f"Number of points for the team:{i[ "ponits"]}")
                


def add_match_result():
    try:
        match_1=int(input("Enter game result"))
        examination_1=u.id_testing(match_1)

        exiles_1=int(input("How many goals did the team score?"))
        examination_2=u.positive_integers(exiles_1)
        match_2=int(input("Enter game result"))

        examination_3=u.id_testing(match_2)
        exiles_2=int(input("How many goals did the team score?"))
        examination_4=u.positive_integers(exiles_2)
        examination_5=u.Check_if_you_played(exiles_1,match_2)
        if examination_1 and examination_2 and examination_3 and examination_4==True and match_1 != match_2 and examination_5==True:

                  m.matches["home_team_id"]= match_1
                  m.matches["away_team_id"]= match_2
                  m.matches["home_goal"]= exiles_1
                  m.matches["away_goals"]= exiles_2
                  m.itam_matches.append(m.matches)
                  u.loading_data(m.matches)

        else:
             print("There is an error in the input.")
    except:
        add_match_result()

def Show_standings():
    sorting_goals_against = sorted(m.itams, key=lambda t:( t["ponits"],t["goals_for"]-t["goals_againts"],t["goals_for"],t["name"]) ,reverse=True)



    print(sorting_goals_against)



              
def Show_leading_team():
    sorting_goals_against = sorted(m.itams, key=lambda t: t["ponits"], reverse=True)
    print(f"The leading team is  {sorting_goals_against[0]}")
    if sorting_goals_against==0:
        print ("There are no games in the system")
         
#     
def Show_best_attacking_team():
    sorting_goals_against = sorted(m.itams, key=lambda t: t["goals_for"], reverse=True)
    print(f"The leading team is  {sorting_goals_against[0]}")
    if sorting_goals_against == 0:
        print("There are no games in the system")
# def Show_team_success_rate():


def Show_teams_without_wins():
    for i in m.itams:
        if i["wins"]==0:
           print(i["name"])


def  Show_tournament_summary():
    print(m.matches)



