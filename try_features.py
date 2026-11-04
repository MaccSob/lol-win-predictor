import json
from src.features import extract_features

with open("data/sample.timeline.json") as f:
    timeline = json.load(f)

with open("data/sample.timeline.json") as f:
    match = json.load(f)    


print(extract_features(match, timeline))