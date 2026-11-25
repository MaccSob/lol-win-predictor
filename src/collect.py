from collections import deque
import time
import json, os
from riot_client import get_match_ids, get_match, get_timeline

MAX_MATCHES = 200

seen_matches = set(f[:-5] for f in os.listdir("data/raw"))
seen_puuids = set()
queue = deque([MY_PUUID])

while queue and len(seen_matches) < MAX_MATCHES:
    puuid = queue.popleft()
    if puuid in seen_puuids:
        continue
    seen_puuids.add(puuid)

    for match_id in get_match_ids(puuid, 20):
        if match_id in seen_matches:
            continue
        match = get_match(match_id)
        timeline = get_timeline(match_id)
        if match["info"]["gameDuration"] > 900:
            continue
        with open(f"data/raw/{match_id}.json", "w") as f:
            json.dump({"match": match, "timeline": timeline}, f)
        seen_matches.add(match_id)
        queue.extend(match["info"]["participants"])
        time.sleep(1.3)
