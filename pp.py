import requests,json
data = requests.get("http://saral.navgurukul.org/api/courses")
data2  = json.loads(data.text)
d={}
with open("json.json","w") as mybase:
    json.dump(data2,mybase, indent=4)