import json


with open("data/sample.timeline.json") as f:
    timeline = json.load(f)

with open("data/sample.match.json") as f:
    match = json.load(f)    

frames = timeline["info"]["frames"]   


pf = frames[10]["participantFrames"]
print(list(pf.keys()))
print(pf["1"].keys())
print(pf["1"])

print(list(match.keys()))
print(list(match["info"].keys()))

print(match["info"]["teams"])

for p in match["info"]["participants"][:2]:
    print(p["participantId"],p["teamId"])


print(timeline["info"].keys())
print(len(frames))
print(frames[10].keys())
print(frames[10]["timestamp"])





types = {e["type"] for fr in frames for e in fr["events"]}
