'''
Créer un script python qui va afficher dans le terminal une phrase aléatoire,
 venant d'un tableau que vous aurez préalablement rempli de quelques citations par exemple.
 En POO même s'il y a peu d'attributs/getters/setters à faire
'''

import random

class Quotes:
    # Initialisation des attributs
    def __init__(self):
        self.quotes = [
            "La vie est ce que notre caractère veut qu'elle soit. - Ralph Waldo Emerson",
            "Il faut toujours viser la lune, car même en cas d'échec, on atterrit dans les étoiles. - Oscar Wilde",
            "La vie, c'est comme une bicyclette, il faut avancer pour ne pas perdre l'équilibre. - Albert Einstein",
            "Le succès, c'est d'aller d'échec en échec sans perdre son enthousiasme. - Winston Churchill",
            "La vraie sagesse, c'est de ne pas sembler sage. - Isaïe Berlin",
        ]
        
    # Méthode qui retourne une citation aléatoire
    def random_quotes(self):
        return random.choice(self.quotes)

def main():
    # Création d'une instance de la classe Citations
    quote_generator = Quotes()

    # Affichage d'une citation aléatoire
    print(quote_generator.random_quotes())

if __name__ == "__main__":
    main()
