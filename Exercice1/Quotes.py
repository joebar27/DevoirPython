import random


class Quotes:
    # Initialisation des attributs :
    def __init__(self):
        self.quotes = [
            "La programmation est une compétence de résolution de problèmes avant d'être une compétence en écriture de code. - Ada Lovelace",
            "La meilleure chose à propos d'être un bon programmeur, c'est que vous pouvez rapidement devenir meilleur qu'un mauvais programmeur. - Martin Fowler",
            "Tout d'abord, résolvez le problème. Ensuite, écrivez le code. - John Johnson",
            "L'une des meilleures compétences en programmation que vous pouvez avoir, c'est savoir quand reculer et considérer les options. - Douglas Crockford",
            "Le code est comme l'humour. Quand vous devez l'expliquer, c'est mauvais. - Cory House",
            "Il faut toujours viser la lune, car même en cas d'échec, on atterrit dans les étoiles. - Oscar Wilde",
            "La vie, c'est comme une bicyclette, il faut avancer pour ne pas perdre l'équilibre. - Albert Einstein",
            "Le succès, c'est d'aller d'échec en échec sans perdre son enthousiasme. - Winston Churchill",
            "La vraie sagesse, c'est de ne pas sembler sage. - Isaïe Berlin",
        ]

    # Méthode qui retourne une citation aléatoire
    def random_quotes(self):
        return random.choice(self.quotes)
