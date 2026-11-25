def extract_features(match: dict, timeline: dict) -> dict:
    team_of = {p["participantId"]: p["teamId"] for p in match["info"]["participants"]}
    frames = timeline["info"]["frames"]
    cutoff = 600_000  

    totals = {
        100: {"gold": 0, "xp": 0, "level": 0, "cs": 0},
        200: {"gold": 0, "xp": 0, "level": 0, "cs": 0},
    }
    for pid, pf in frames[10]["participantFrames"].items():
        team = team_of[int(pid)]
        totals[team]["gold"] += pf["totalGold"]
        totals[team]["xp"] += pf["xp"]
        totals[team]["level"] += pf["level"]
        totals[team]["cs"] += pf["minionsKilled"] + pf["jungleMinionsKilled"]

  
    kills = {100: 0, 200: 0}
    kill_log = []  
    for frame in frames[:11]:
        for e in frame["events"]:
            if e["type"] != "CHAMPION_KILL" or e["timestamp"] > cutoff:
                continue
            killer = e["killerId"]
            if killer == 0:  # zabójstwo bez gracza (np. wieża)
                continue
            team = team_of[killer]
            kills[team] += 1
            kill_log.append((e["timestamp"], team))

    
    first_blood = 0
    if kill_log:
        first_blood = 1 if min(kill_log)[1] == 100 else -1

 
    blue_win = 0
    for team in match["info"]["teams"]:
        if team["teamId"] == 100:
            blue_win = int(team["win"])

    return {
        "gold_diff": totals[100]["gold"] - totals[200]["gold"],
        "xp_diff": totals[100]["xp"] - totals[200]["xp"],
        "level_diff": totals[100]["level"] - totals[200]["level"],
        "cs_diff": totals[100]["cs"] - totals[200]["cs"],
        "kills_diff": kills[100] - kills[200],
        "first_blood": first_blood,
        "blue_win": blue_win,
    }