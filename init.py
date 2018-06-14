#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
# coding=utf-8
import mysql.connector
from html.parser import  HTMLParser
cnx = mysql.connector.connect(host='localhost', password = '', user='root', database='db_pokemom')
cursor = cnx.cursor()
print(cursor.statement)

# enregistrement de la page pokedex en local
'''
url = "https://pokemondb.net/pokedex/all"
response =requests.get(url)
html=str(response.content)
with open("pokemon_page.html", "w") as fichier:
    fichier.write(html)
'''

#  création de la base de données dans le code
# cursor.execute("""DROP DATABASE IF EXISTS db_pokemom; CREATE DATABASE db_pokemom;""")
#  A revoir essayer avec une autre connexion

#  Création de la table qui va stocker les données des pokemons
'''
cursor.execute("""CREATE TABLE IF NOT EXISTS t_pokedex ( id INT(11) NOT NULL AUTO_INCREMENT, PRIMARY KEY(id),
national_number VARCHAR(3) ,
name varchar(30), 
type varchar(255),
total int,
hp int,
attack int,
defense int,
sp_atk int,
sp_def int,
speed int
);""")

#  réinitialiser la table
cursor.execute("""TRUNCATE TABLE t_pokedex;""")

'''
#  parcourir la page HTML pour récupérer les données des pokemon et les insérer dans la base de données
with open("pokemon_page.html", "r") as html:
    soup=BeautifulSoup(html, "html.parser")
    tab=soup.find(id="pokedex")

    i = 0
    for link in tab.find_all("tr"):
        data_pokemon = []
        i = i+1
        numero = 0
        for l in link.find_all("td"):
            numero = numero + 1
            #  séparer les noms de type pokemon pour ceux en ont plusieurs
            if(numero == 3):
                typepokemon = list(l.text)
                print(typepokemon)
                debut=typepokemon[0]
                # typepokemon=typepokemon[-(len(typepokemon)-1):]
                print(debut)

                print(typepokemon)
                # print(type(typepokemon))

                # for lettre in enumerate(typepokemon):
                for lettre in enumerate(typepokemon[-(len(typepokemon) - 1):]):
                    caractere = lettre[1]
                    index = lettre[0]

                    if(caractere.isupper()):
                        # lettre = lettre + " "
                        print(caractere)
                        typepokemon[index+1] = " " + caractere
                        print(typepokemon)
                        print("\n\n")
                        typepokemon = "".join(typepokemon)
                        print(str(typepokemon))

                # print("Les nom des types de pokemon:  " + l.text
                data_pokemon.append(typepokemon)

            data_pokemon.append(str(l.text).strip(" "))


        # print(str("tableau N° " + str(i) + str(data_pokemon)) + " a une taille  de  " + str(len(data_pokemon)))
        # if taille != 10:
        #      print(str("tableau N° " + str(i) +  str(data_pokemon)) +" a une taille  de  " + str(taille))

'''
        if(len(data_pokemon) > 0):
            cursor.execute(""" INSERT  INTO  `t_pokedex`(`national_number`, `name`, `type`, `total`, `hp`, `attack`, `defense`, `sp_atk`, `sp_def`,
                       `speed`)
           VALUES(%s, %s, %s, %s, %s, %s,%s, %s, %s, %s)""" , data_pokemon)
'''
            # print(l.text)
           # print("\n")
'''
    cnx.commit()
    cursor.close()
    cnx.close()

'''



