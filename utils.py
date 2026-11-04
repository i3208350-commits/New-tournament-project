import main as m
def a_test_that_is_filled(x):
    if x=="":
        return False
    else:
        return True


def positive_integers(x):
    if x!=int:
        print("You did not submit a whole number.")
        m.menu()
    if x<0:
        print("You did not submit a positive number.")
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

def Check_if_you_played(x):
    for i in m.itams:
        if i["id"]==x:
            if i["played"]==0:
               return True
        else:
            return False