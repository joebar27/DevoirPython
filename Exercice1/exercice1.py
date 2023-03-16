'''
Créer un script python qui va afficher dans le terminal une phrase aléatoire,
 venant d'un tableau que vous aurez préalablement rempli de quelques citations par exemple.
 En POO même s'il y a peu d'attributs/getters/setters à faire
'''
from Quotes import Quotes

def main():
    # Création d'une instance de la classe Citations :
    quote_generator = Quotes()

    # Affichage d'une citation aléatoire :
    print(quote_generator.random_quotes())

# Exécution du script :
if __name__ == "__main__":
    main()
