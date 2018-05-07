# USAGE EXAMPLES


# team1, team2 = balance_teams(players)
# team1, team2 = stack_teams(players)
# team1, team2 = random_teams(players)
# await bot.send_message(message.channel, team_string(team1, team2))



# WHAT SHOULD YOUR PLAYERS LOOK LIKE?
# players = [[mmr, name], [mmr, name], [mmr, name], ...] len() = 10

from statistics import mean
from random import randint as r
from operator import itemgetter

# pass this function two teams, and it will return 5 values
def team_utils(team1, team2):   
    team1string, team2string = [], []
    
    place = 0
    for member in team1:
        place += 1
        team1string.append(f"{place}.{member[1]}({member[0]})")
    
    place = 0
    for member in team2:
        place += 1
        team2string.append(f"{place}.{member[1]}({member[0]})")
    
    team1string = "\n".join(team1string)
    team2string = "\n".join(team2string)
    
    team_asum = team_sum(team1)
    team_bsum = team_sum(team2)
    if team_asum > team_bsum:
        difference = team_asum - team_bsum
    else:
        difference = team_bsum - team_asum
        
    return team1string, team2string, team_asum, team_bsum, difference

    
# finds the sum of a team   
def team_sum(team):
    tota = 0
    for p in team:
         tota += int(p[0])
    return tota

def sort_players(members):
    return sorted(members, key=itemgetter(0))



# balances a team from a sorted list of 10 "Players" (player = [mmr, name])    
def balance_teams(players):
    team_a, team_b = [], []
    
    
    while players:
        team_asum = team_sum(team_a)
        team_bsum = team_sum(team_b)
        low = players.pop(0)
        high = players.pop(-1)
        if team_asum < team_bsum:
            team_a.append(high)
            team_b.append(low)
        else:
            team_b.append(high)
            team_a.append(low)
        

    return team_a, team_b
 

# stacks a team from a sorted list of 10 "Players" (player = [mmr, name])
def stack_teams(players):
    team_a = [member for member in players if players.index(member) <= 4]
    team_b = [member for member in players if players.index(member) >= 5]
    
    
    return team_a, team_b
    
    

# randomises a team from a list of 10 "Players" (player = [mmr, name])    
def random_teams(players):
    team_a, team_b = [], []
    
    
    while players:
        if len(team_a) < 5:
            team_a.append(players.pop(r(0, len(players) - 1)))
        else:
            team_b.append(players.pop())
            
    team_astring, team_bstring, team_asum, team_bsum, difference = team_utils(team_a, team_b)
    
    return team_a, team_b
    
    
    
# finds the average of a team   
def team_mean(team):
    teammmrs = []
    for player in team:
        mmr = player[0]
        teammmrs.append(mmr)
    return mean(teammmrs)

# creates the final display of the teams for discord output only    
def team_string(team1, team2):
    team_astring, team_bstring, team_asum, team_bsum, difference = team_utils(team1, team2)
    string = f"""```
MMR Difference: {difference}\n
Team A:
{team_astring}
Total: ({team_asum})
Average: ({team_mean(team1)})

Team B:
{team_bstring}
Total: ({team_bsum})
Average: ({round(team_mean(team2), 1)})
```"""
    return string
        