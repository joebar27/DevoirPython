class Person:
    # Initialisation des attributs :
    def __init__(self):
        self.person = {
            "first_name": "Romain",
            "last_name": "Anger",
            "age": 35,
            "genre": "homme",
            "developer": {
                "language": ["Python", "PHP", "C++", "JavaScript", "SQL", "HTML", "CSS"],
                "framework": ["Flask", "Bootstrap", "Tailwind", "VueJS", "Laravel", "Symfony", "REACT"],
            },
        }

    # Getter et Setter de l'attribut person :
    def get_person(self):
        return self.person

    def set_person(self, first_name, last_name, age, genre):
        self.person = {
            "first_name": first_name,
            "last_name": last_name,
            "age": age,
            "genre": genre,
            "developer": {
                "language": [],
                "framework": [],
            }
        }
