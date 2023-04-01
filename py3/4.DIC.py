print("ansh kothari\nKFBSC(IT)033")
person = {
    "name": "John",
    "age": 30,
    "gender": "Male",
    "occupation": "Software Engineer"
}

print("Person details:", person)
print("Age:", person["age"])
person["occupation"] = "Data Scientist"
print("Updated person details:", person)
person["location"] = "New York"
print("Person details after adding location:", person)
del person["gender"]
print("Person details after removing gender:", person)