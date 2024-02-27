import json, sys


def addValues(obj):
    if isinstance(obj, list): 
        for i in obj:
            addValues(i)
    if isinstance(obj, dict):
        if obj.keys().__contains__("values"):
            addValues(obj["values"])
        value = None; id = obj["id"]
        for i in values['values']:
            if i["id"] == id:
                value = i["value"]
                break
        if value == None:
            value = "passed"
            for dic in obj["values"]:
                if dic["value"] == "failed":
                    value = "failed"
        obj['value'] = value
    

values = json.load(open(sys.argv[1]))
tests = json.load(open(sys.argv[2]))

addValues(tests["tests"])

open(sys.argv[3], "w+").write(json.dumps(tests))
