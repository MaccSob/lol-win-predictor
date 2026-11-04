def extract_features(match: dict, timeline: dict) -> dict:
    team_of = {p["participantId"]: p["teamId"] for p in match["info"]["participants"]}
    frames = timeline["info"]["frames"]

    totals = {100: {"gold": 0, "xp": 0, "level": 0, "cs": 0},
              200: {"gold": 0, "xp": 0, "level": 0, "cs": 0}}
              

    
    for pid, pf in frames[10]["participantFrames"].items():
        team = team_of[int(pid)]
        totals[team]["gold"] += pf["totalGold"]
        totals[team]["xp"] += pf["xp"]
        totals[team]["level"] += pf["level"]
        totals[team]["cs"] += pf["minionsKilled"] + pf["jungleMinionsKilled"]

    gold_diff = totals[100]["gold"] - totals[200]["gold"]
    xp_diff = totals[100]["xp"] - totals[200]["xp"]
    level_diff = totals[100]["level"] - totals[200]["level"]
    cs_diff = totals[100]["cs"] - totals[200]["cs"]

    for team in match["info"]["teams"]:
        if team["teamId"] == 100:
            blue_win = int(team["win"])


    return { "gold_diff": gold_diff, 
            "xp_diff": xp_diff, 
            "level_diff": level_diff, 
            "cs_diff": cs_diff, 
            "blue_win": blue_win,
            } 