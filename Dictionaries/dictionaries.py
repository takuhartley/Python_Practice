cars = {
  "brand": "Tesla",
  "model": "Model X",
  "year": 2019
}

print(cars)

x = cars["model"]
print(x)

x = cars.get("model")
print(x)

people = {
  "name": "Robert",
  "age": 22,
  "gender": "Male"
}

people["year"] = 2018
print(people)

for x in people:
  print(x)

for x in people:
  print(people[x])

for x in people.values():
  print(x)

for x, y in people.items():
  print(x, y)

people = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

print(len(thisdict))

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()

print(car)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

print(x)