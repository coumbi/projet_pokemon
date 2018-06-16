# projet_pokemon
API REST DE  GESTION POKEMON
Cet API REST met à disposition les fonctionnalités CRUD des pokémons en python. Elle est basée sur les données extraites de la page html  https://pokemondb.net/pokedex/all (base de données des pokemons) et offre à l’utilisateur la possibilité de les lire, modifier, supprimer et d’en ajouter de nouveaux.
Avant de Commencer, 
Nous avons d’abord créé une base de données une base de données mysql via le script ci –dessous  CREATE DATABASE db_pokemon
Notre application a dans un premier temps copié la  page  https://pokemondb.net/pokedex/all en local  el l’a ensuite parcouru  ligne par ligne et colonne par colonne pour  extrait les données et  les insérer dans une table t_pokedex de la base de données db_ pokemons  Il faut noter que cette table est créée par le code python en amont de l’insertion. L’ensemble du script se trouve dans le init.py.  situé à la racine du projet.
Les sources peuvent être téléchargées depuis le lien  https://github.com/coumbi/projet_pokemon.
L’API  proprement parlé est implémentée dans le fichier api.py. Comme il s’agit d’un api rest il renvoi ses résultats au format JSON.
Pré requis
Pour exécuter cette application en local sur votre machine, vous aurez besoins d’installer certains composants logiciels tels que: 
1.	Python 3.6.5 + (le télécharger sur le site de python et lancer l’exe en prenant soin cochez la case ajouter python au path

2.	Pip 10.0.1  si vous avez une version antérieure, merci de le mettre jour

3.	Pour la  base de données MYSQL  installer xampp et workbrecnh)

4.	Myslconnector for python
5.	Beautifulsoup4
6.	Requests
7.	Hug  
8.	Postman (application de bureau  télécharger et installer l’exe)
9.	GitHub Desktop (pour utiliser  Git Bash)

Installez ces outils cités du point 4. au point 7.  par commandes pip (pip install   [le nom du composant à installer] voir sur google pour la syntanxe correcte



Pour commencer on execute  la commande hug – f apipy depuis un terminal (pour notre cas c’est Git Bash qui est utilisé )
on va ensuite sur POSTMAN pour lancer les différentes fonctions de l'API.
Ainsi quand l’utilisateur fait appel à la fonction de consultation de tous les  pokemons par exemple, il saisit 
L’url localhost:800/getall
Et il reçoit le résultat ci-dessous : c’est l’affichage au format JSON de l’ensemble des pokemons existants dans la base de données
 
Il peut  en spécifier un seul par le paramètre id (voir structure de la table t_pokedex) et l’afficher dans ce cas l’url c’est  localhost:8000/getone?id=5   où 5 c’est l’identifiant du pokemon en question.
Pour ajouter un nouveau pokemon Invoque l’api en mode post via l’url  localhost:8000/create
 
La suppression se fait par  localhost:8000/delete?id=5  
et la mis à jour par localhost:8000/update?id=5 
Pour une meilleure documentation des fonctions de l’API voir le fichier pokemon_swagger.json

Versioning
L’application en est à sa première version voir (.https://github.com/coumbi/projet_pokemon.)
Vos commentaires et suggestions sont les bienvenues pour son évolution


Auteurs
Coumba BATHILY -  POE JAVA SQLI-ASTON

Remerciements
Mehdi ABERKANE   -  FORMATEUR
Alpha BARRY      -  VOISIN

