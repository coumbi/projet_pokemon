#!/usr/bin/python3
# coding=utf-8
import requests
from bs4 import BeautifulSoup
import mysql.connector
from html.parser import  HTMLParser


# sss
# print(cursor.statement)

# enregistrement de la page pokedex en local
'''
url = "https://pokemondb.net/pokedex/all"
response =requests.get(url)
html=str(response.content)
with open("pokemon_page.html", "w") as fichier:
    fichier.write(html)
'''

#  création de la base de données dans le code (ne marhe pas à tous les coups)
'''
# cnx = mysql.connector.connect(host='localhost', password = '', user='root')
# cursor = cnx.cursor()
def createdatabase():
    try:
        cursor.execute("""DROP DATABASE IF EXISTS db_pokemom; CREATE DATABASE db_pokemom;""", multi=True)
        cnx.commit()
        cnx.database = 'db_pokemom'
        return  True
    except mysql.connector.Error as err:
            print(err)
            return False
'''

cnx = mysql.connector.connect(host='localhost', password = '', user='root',database = 'db_pokemom')
cursor = cnx.cursor()


#  Création de la table qui va stocker les données des pokemons

# cnx = mysql.connector.connect(host='localhost', password = '', user='root', database='db_pokemom')
# cursor = cnx.cursor()
def createtables():
    try:
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
        return  True
    except  mysql.connector.Error as err:
        print(err)
        return False
            # exit()

#  réinitialiser la table
def truncatetable():
    try:
        cursor.execute("""TRUNCATE TABLE t_pokedex;""")
    except mysql.connector.Error as err:
        print(err)

#  parcourir la page HTML pour récupérer les données des pokemon et les insérer dans la base de données
def loadpokemon():
    try:
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
                        data_pokemon.append(separatetype(l.text))
                    else:
                        data_pokemon.append(str(l.text).strip(" "))
                # print(str("tableau N° " + str(i) + str(data_pokemon)) + " a une taille  de  " + str(len(data_pokemon)))
                # if taille != 10:
                #      print(str("tableau N° " + str(i) +  str(data_pokemon)) +" a une taille  de  " + str(taille))


                if(len(data_pokemon) > 0):
                    cursor.execute(""" INSERT  INTO  `t_pokedex`(`national_number`, `name`, `type`, `total`, `hp`, `attack`, `defense`, `sp_atk`, `sp_def`,
                               `speed`)
                   VALUES(%s, %s, %s, %s, %s, %s,%s, %s, %s, %s)""", data_pokemon)

                    # print(l.text)
                   # print("\n")

        cnx.commit()
    except  mysql.connector.Error as err:
        print(err)
        cnx.rollback()

def separatetype(typepokemon):

    separer = False
    tab_type = list(typepokemon)

    for lettre in tab_type[-(len(tab_type) - 1):]:
        if lettre.isupper():
            separer = True
            break

    if (separer):

        for lettre in enumerate(tab_type[-(len(tab_type) - 1):]):
            caractere = lettre[1]
            index = lettre[0]

            if (caractere.isupper()):
                tab_type[index + 1] = " " + caractere

        typepokemon = "".join(tab_type)
    return typepokemon

############################################### FIN DEFINITION DES FONCTIONS ################################################################

 # Appell des fonctions

# if(createdatabase()) :
#     cnx.database = 'db_pokemom'
if(createtables()):
    truncatetable()
    loadpokemon()

cursor.close()
cnx.close()





