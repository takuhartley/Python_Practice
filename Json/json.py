import check as c
import json as j

# parse x:
# y = json.loads(t.x)
y = j.dumps(c.x)
print(y)
json.dumps(x, indent=4)
json.dumps(x, indent=4, separators=(". ", " = "))
json.dumps(x, indent=4, sort_keys=True)
# the result is a Python dictionary:
# print(y["age"])