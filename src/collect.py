import json
import os
import time
from collections import deque

from src.riot_client import get_puuid, get_match_ids, get_match, get_timeline

MAX_MATCHES = 50
MIN_DURATION = 900  

os.makedirs("data/raw", exist_ok=True)

seen_matches = {f[:-5] for f in os.listdir("data/raw")} 
skipped = set()                                          
seen_puuids = set()

queue = deque([get_puuid("dingdong", "ysl")])

while queue and len(seen_matches) < MAX_MATCHES:
    puuid = queue.popleft()
    if puuid in seen_puuids:
        continue
    seen_puuids.add(puuid)

    for match_id in get_match_ids(puuid, 20):
        if len(seen_matches) >= MAX_MATCHES:
            break
        if match_id in seen_matches or match_id in skipped:
            continue

        match = get_match(match_id)
        timeline = get_timeline(match_id)

        too_short = match["info"]["gameDuration"] < MIN_DURATION
        too_few_frames = len(timeline["info"]["frames"]) < 11
        if too_short or too_few_frames:
            skipped.add(match_id)
            continue

        with open(f"data/raw/{match_id}.json", "w") as f:
            json.dump({"match": match, "timeline": timeline}, f)
        seen_matches.add(match_id)

        queue.extend(p["puuid"] for p in match["info"]["participants"])
        time.sleep(1.3)

print(f"Zebrano {len(seen_matches)} meczów")