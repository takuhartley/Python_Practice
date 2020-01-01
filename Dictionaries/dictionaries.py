cars = {
  "brand": "Tesla",
  "model": "Model X",
  "year": 2019
}

people = {
  "name": "Robert",
  "age": 22,
  "gender": "Male"
}
print(cars)

x = cars["model"]
print(x)

x = cars.get("model")
print(x)

people["age"] = 1995
print(people)

for x in people:
  print(x)

for x in people:
  print(people[x])

for x in people.values():
  print(x)

for x, y in people.items():
  print(x, y)

if "model" in cars:
  print("Yes, 'model' is one of the keys in the people dictionary")

print(len(people))

people["name"] = "Alex"
print(people)

cars.pop("model")
print(cars)

cars.popitem()
print(cars)

x = cars.setdefault("model", "Bronco")
print(x)

cars.update({"color": "White"})
print(cars)

x = cars.values()
print(x)