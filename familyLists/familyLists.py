# Import required libraries
import json

# Define dictionaries for Mom, Dad, Sarah, Linda, Grandma, Grandpa
mom = {
    "name": "Sherry Wen",
    "gender": "female",
    "age": 51,
    "birthplace": "China"
}

dad = {
    "name": "Peter Xie",
    "gender": "male",
    "age": 53,
    "birthplace": "China"
}

me = {
    "name": "Sarah Xie",
    "gender": "female",
    "age": 16,
    "birthplace": "Canada"
}

sister = {
    "name": "Linda Xie",
    "gender": "female",
    "age": 27,
    "birthplace": "Canada"
}

gMa = {
    "name": "Yue Wen",
    "gender": "female",
    "age": 84,
    "birthplace": "China"
}

gPa = {
    "name": "Shu Wen",
    "gender": "male",
    "age": 87,
    "birthplace": "China"
}

# Combine the dictionaries into a 'family' list
family = [mom, dad, me, sister, gMa, gPa]

# Printing the family members from the list to the console
print("\nFamily data incoming from the list of dictionaries!\n")
for person in family:
    print(f"{person['name']} is a {person['gender']} who is {person['age']}"
          f" years old and was born in {person['birthplace']}")

# Turn the dictionary into a JSON file
with open("family.json", "w") as file:
    json.dump(family, file, indent=4)

# Get the data from the JSON file
with open("family.json") as file:
    familyData = json.load(file)

# print from the JSON file data to the console
print("\nExtra cool family data incoming from the JSON file!\n")
for person in familyData:
    print(f"{person['name']} is a {person['gender']} who is {person['age']}"
          f" years old and was born in {person['birthplace']}")
    print("😎")

# Returning the JSON file to a dictionary with the key "family"
familyDict = {
    "family": familyData
}

# Create new dictionaries using the family key, that have parets and grandparents key

# the blank starter dictionary that we're going to append to
relationDict = {
    "parents" : [],
    "grandparents": []
}

# iterate through the people and use logic to pair the right people with the right keys
for person in familyDict["family"]:

    if (person["name"] == "Sherry Wen") or (person["name"] == "Peter Xie"):
        relationDict["parents"].append(person)
    elif (person["name"] == "Yue Wen") or (person["name"] == "Shu Wen"):
        relationDict["grandparents"].append(person)

# print my parents and gradparents using the key value pairs

# print the parents
print("\nThese are my parents!\n")
for person in relationDict["parents"]:
    print(f"{person['name']} is a {person['gender']} who is {person['age']}"
          f" years old and was born in {person['birthplace']}")

# print the grandparents
print("\nThese are my grandparents!\n")
for person in relationDict["grandparents"]:
    print(f"{person['name']} is a {person['gender']} who is {person['age']}"
          f" years old and was born in {person['birthplace']}")
