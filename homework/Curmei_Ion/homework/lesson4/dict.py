my_dict = {
    "tuple": (1, 2, 3, 4, 5, 6),
    "list": [100, 200, 300, 400, 500],
    "dict": {
        "Englang": "London",
        "France": "Paris",
        "Spain": "Barcelona",
        "Norway": "Oslo",
        "Austria": "Viena",
    },
    "set": {11, 12, 13, 14, 15},
}

print("last element tuple is :", my_dict["tuple"][-1])

my_dict["list"].append(600)

my_dict["list"].pop(1)

my_dict["dict"][("i am a tuple",)] = "TUPLE"

my_dict["dict"].pop("France")

my_dict["set"].add(20)

my_dict["set"].remove(13)

print("new dict is : ", my_dict)
