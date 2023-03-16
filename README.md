 DevoirPython
3 Exercices Python en devoir noté

---
# Sommaire
1. [Instructions](#instructions)
2. [Énoncés](#énoncés)
3. [Installation des packets](#installation-des-packets)

# Instructions
 --- DEVOIR INDIVIDUEL PYTHON ---  
 TOUT EST À FAIRE EN POO.

# Énoncés

### --- PARTIE 1 ---

 Créer un script python qui va afficher dans le terminal une phrase aléatoire,
 venant d'un tableau que vous aurez préalablement rempli de quelques citations par exemple   
 /!\ En POO même s'il y a peu d'attributs/getters/setters à faire /!\

### --- PARTIE 2 ---

 Créer un script python qui va contenir un dictionnaire (par exemple une personne, avec des attributs comme l'âge, le prénom, le genre...)
 Retourner ce dictionnaire sous forme d'objet JSON dans le terminal (voir le package 'json' pour plus d'info)   
 /!\ En POO également, vous devez initialiser le dictionnaire soit dans le constructeur soit avec un setter après instanciation de la classe /!\

### --- PARTIE 3 ---

 Créer un script python qui va récupérer les informations systèmes (voir les packages 'platform', 'cpuinfo', 'socket' et 'os' pour plus d'info)
 Avec le moteur de templating jinja, afficher dans un beau template HTML (avec du CSS dans un fichier CSS séparé) ces informations systèmes
 Évidemment, le tout en POO...   
 /!\ Je demande pas le site de l'année, mais faites un effort sur le CSS svp /!\

# Instalation des packets

Pour creer un environnement virtuel, il faut taper dans le terminal :   

    - python -m venv venv

---

Pour activé l'environnement virtuel, il faut taper dans le terminal :   

    - venv\Scripts\activate 

---  

Puis pour installer les packets, il faut taper dans le terminal :   

    - pip install flask
    
---

Efin pour lancer le serveur, il faut taper dans le terminal :

    - flask --app exercice3 run 
    ('exercice3' étant le nom du fichier principal)   
