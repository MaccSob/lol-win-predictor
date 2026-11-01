import json


with open("data/sample.timeline.json") as f:
    timeline = json.load(f)

for p in match["info"]["participants"][:2]:
    print(p["participantId"],p["teamId"])


frames = timeline["info"]["frames"]
print(timeline["info"].keys())
print(len(frames))
print(frames[10].keys())
print(frames[10]["timestamp"])

pf = frames[10]["participantFrames"]
print(list(pf.keys()))
print(pf["1"].keys())
print(pf["1"])



types = {e["type"] for fr in frames for e in fr["events"]}
