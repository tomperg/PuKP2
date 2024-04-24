import json

# Opening JSON file
file = open("data/person_db.json")

# Loading the JSON File in a dictionary
person_data = json.load(file)


def load_person_data():
    """A Function that knows where the person database is and returns a dictionary with the persons"""

    file = open("data/person_db.json")

    person_data = json.load(file)

    return person_data

def get_person_list():
    namenliste = []

    for name in person_data: 
        namenliste.append(name["firstname"] + ", " + name["lastname"])

    return namenliste

print(get_person_list())