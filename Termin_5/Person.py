import json
import datetime as dt
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
        """ Eine Funktion der Nachname, Vorname als ein String übergeben wird
        und die die Person als Dictionary zurück gibt"""

        person_data = Person.load_person_data()
        #print(suchstring)
        if suchstring == "None":
            return {}

        two_names = suchstring.split(", ")
        vorname = two_names[1]
        nachname = two_names[0]

        for eintrag in person_data:
            print(eintrag)
            if (eintrag["lastname"] == nachname and eintrag["firstname"] == vorname):
                print()

                return eintrag
        else:
            return {}
        
    def __init__(self, person_dict) -> None:
        self.date_of_birth = person_dict["date_of_birth"]
        self.firstname = person_dict["firstname"]
        self.lastname = person_dict["lastname"]
        self.picture_path = person_dict["picture_path"]
        self.id = person_dict["id"]

#Erstelle eine Funktion um das Alter der Personen aus dem JSON zu berechnen
    def calc_age(self):
        data_used_for_age_calc = Person.find_person_data_by_name(self)
        birthdate = data_used_for_age_calc["date_of_birth"]
        year = dt.date.today().year
        """A Function to calculate the age of a person"""
        age = year - birthdate
        return age
    

    #Funktion um max_HR basierend auf Alter zu berechnen
    def calc_max_heart_rate(self):
        age_used = Person.calc_age(self)
        max_heart_rate = 220 - age_used
        return max_heart_rate
#Funktion um die Daten einer Person anhand der ID zu laden
    def load_by_id(person_id):
        person_data = Person.load_person_data()
        for eintrag in person_data:
            if eintrag["id"] == person_id:
                return eintrag
        else:
            return {}
        
        
        

if __name__ == "__main__":
    print("This is a module with some functions to read the person data")
    persons = Person.load_person_data()
    person_names = Person.get_person_list(persons)
    print(person_names)
    print(Person.find_person_data_by_name("Huber, Julian"))
    print(Person.calc_age("Huber, Julian"))
    print(Person.calc_max_heart_rate("Heyer, Yannic"))
    print(Person.load_by_id(3))