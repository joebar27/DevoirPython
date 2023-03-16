'''
Créer un script python qui va contenir un dictionnaire (par exemple une personne, avec des attributs comme l'âge, le prénom, le genre...). Retourner ce dictionnaire sous forme d'objet JSON dans le terminal (voir le package 'json' pour plus d'info)
En POO également, vous devez initialiser le dictionnaire soit dans le constructeur soit avec un setter après instanciation de la classe.
'''

import json
from Person import Person

def main():

    # Création d'une instance de la classe Person :
    person = Person()

    # Affichage du dictionnaire sous forme d'objet JSON, avec indentation a l'affichage :
    print(json.dumps(person.get_person(), indent=4))

if __name__ == "__main__":
    main()
