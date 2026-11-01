import json
from src.riot_client import get_timeline, get_match


match_id = "EUW1_8031235541"

with open("data/sample.match.json", "w") as f:
    json.dump(get_match(match_id), f)

with open("data/sample.timeline.json", "w") as f:
    json.dump(get_timeline(match_id), f)