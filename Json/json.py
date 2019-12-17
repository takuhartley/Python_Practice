import check as c
import json as j

# parse x:
# y = json.loads(t.x)
y = j.dumps(c.x)
print(y)

# the result is a Python dictionary:
# print(y["age"])