
#!/usr/bin/python3
# coding=utf-8
import hug
import mysql.connector
import json

cnx = mysql.connector.connect(host='localhost', password = '', user='root', database='db_pokemom')
cursor = cnx.cursor()
#
# @hug.get('/')
# def sayhello():
#      return "Hello every body !"
# ddd

# Afficher tous les pokemon
@hug.get('/getall')
def getallpokemons():

    try:
        cursor.execute("""SELECT *  FROM t_pokedex""")
        rowspokemon= cursor.fetchall()
        if cursor.rowcount > 0:
            return  rowspokemon
        else:
            return {'message' : 'aucun pokemon trouvé dans la base'}
    except mysql.connector.Error as err:
       return  {'error message': str(err)}



# Afficher un pokemon
@hug.get('/getone')
def getsinglepokemon(id: hug.types.number):
   try:
        cursor.execute("""SELECT  * FROM t_pokedex WHERE id=%s""", [id])
        onepokemon=cursor.fetchone()
        if cursor.rowcount >0:
            return onepokemon
        else:
            return {'message': "aucun pokemon corresspondant à l'id " + str(id) }


   except mysql.connector.Error as err:
       return {'error message': str(err)}

     # try:
     #    cursor.execute("""SELECT  * FROM t_pokedex WHERE id=%s""",[id])
     #    onepokemon=cursor.fetchone()
     #    return onepokemon
     #
     # except Exception as e:
     #
     #     resultat = {'message': 'pokemon trouvé  ' + str(id) +'non trouvé'}
     #     return  resultat
     #
     # # finally:
     #     #      cursor.close()
     # # cnx.close()


@hug.post('/create')
def insertpokemon(body):
    # print(body)
    try:

        requete=("INSERT  INTO  t_pokedex (national_number, name, type, total, hp, attack, defense, sp_atk, sp_def, speed)"
             " VALUES(%(national_number)s, %(name)s, %(type)s, %(total)s, %(hp)s, %(attack)s, %(defense)s, %(sp_atk)s, %(sp_def)s, %(speed)s)")
        cursor.execute(requete, body)
        cnx.commit()
        return  {'message': 'pokemon ' + str(cursor.lastrowid) +' ajouté avec succès'}

        # return json.dumps(resultat)
    except mysql.connector.Error as err:
        return {'error message': str(err)}
        # resultat = "échec création nouvel pokemon"
        # resultat = {'message': 'echec ajout nouveau pokemon '}




@hug.put('/update')
def updatepokemon(body):
     try:
         requete = (""" UPDATE `t_pokedex` SET `national_number`=%(national_number)s,`name`=%(name)s,`type`=%(type)s,
         `total`=%(total)s, `hp`=%(hp)s,`attack`=%(attack)s,`defense`=%(defense)s,`sp_atk`=%(sp_atk)s,`sp_def`=%(sp_def)s,`speed`=%(speed)s
             WHERE id=%(id)s  """)
         cursor.execute(requete, body)

         cnx.commit()
         return {'message': 'pokemon ' + str(body.get("id")).replace('b','') + ' mis à jour avec succès'}

     except mysql.connector.Error as err:
          return {'error message': str(err)}


@hug.delete('/delete')
def deletepokemon(id):
    result=""
    # supprimer un pokemeon
    try:
        cursor.execute("""DELETE  FROM t_pokedex WHERE id=%s""",[id])
        cnx.commit()

        # print(cursor.statement)

        # vérifier la suppression
        if cursor.rowcount:
            result = {"message": "pokemon " + str([id]) + " supprimé avec succés"}
        else:
            result = {"message" : "echec suppression pokemen " + str([id])}
        return result
    except mysql.connector.Error as err:
        return {'error message': str(err)}



