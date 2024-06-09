import json
from datetime import datetime

class Person:
    
    @staticmethod
    def load_person_data():
        """A Function that knows where te person Database is and returns a Dictionary with the Persons"""
        file = open("person_db.json")
        person_data = json.load(file)
        return person_data

    @staticmethod
    def get_person_list(person_data):
        """A Function that takes the persons-dictionary and returns a list auf all person names"""
        list_of_names = []

        for eintrag in person_data:
            list_of_names.append(eintrag["lastname"] + ", " +  eintrag["firstname"])
        return list_of_names
    
    @staticmethod
    def find_person_data_by_name(suchstring):
        """A function where last name, first name is passed as a string and returns the person as a dictionary."""
        if not isinstance(suchstring, str):
            raise TypeError("The argument must be a string")
        
        person_data = Person.load_person_data()
        if suchstring == "None":
            return {}

        try:
            nachname, vorname = suchstring.split(", ")
        except ValueError:
            raise ValueError("The name string should be in the format 'Lastname, Firstname'")

        for entry in person_data:
            if entry["lastname"] == nachname and entry["firstname"] == vorname:
                return entry
        return {}
        
    @staticmethod
    def load_by_id(ID):
        '''A function that loads a person by id and returns the person as a dictionary.'''
        person_data = Person.load_person_data()

        if ID == "None":
            return None

        for eintrag in person_data:
            if eintrag["id"] == ID:
                return eintrag
        else:
            return {}
        
    def __init__(self, person_dict) -> None:
        self.date_of_birth = person_dict["date_of_birth"]
        self.firstname = person_dict["firstname"]
        self.lastname = person_dict["lastname"]
        self.picture_path = person_dict["picture_path"]
        self.id = person_dict["id"]

    def calc_age(self):
        '''A function that calculates the age of a person based on the date of birth.'''

        today = datetime.today()
        age = today.year - self.date_of_birth
        
        return age


    def calc_max_heart_rate(self):
        '''A function that calculates the maximum heart rate of a person.'''

        age = self.calc_age()
        max_heart_rate = 220 - age

        return max_heart_rate


if __name__ == "__main__":
    print("This is a module with some functions to read the person data")
    persons = Person.load_person_data()
    person_names = Person.get_person_list(persons)
    person1 = Person(Person.find_person_data_by_name("Huber, Julian"))
    print(person1.calc_max_heart_rate())
    print(Person.load_by_id(1))
    