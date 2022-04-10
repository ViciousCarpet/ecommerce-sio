import mysql.connector

class Bdd:
    
    def __init__(self):
        
        self.__mydb= mysql.connector.connect(
            # host="172.19.0.16",
            # user="sio",
            # password="0550002D",
            host="localhost",
            user="root",
            password="",
            database="ecommerce"
        )
    
    def chargerLesProduits(self):
        query="SELECT * FROM produit"
        mycursor= self.__mydb.cursor()
        mycursor.execute(query)
        myresult=mycursor.fetchall()
        return myresult

    def connexion(self,log,mdp):
        query="SELECT count(id_conn) FROM conn WHERE login='"+log+"' AND mdp='"+mdp+"'"
        mycursor= self.__mydb.cursor()
        mycursor.execute(query)
        myresult=mycursor.fetchone()
        donnee = myresult[0]
        if myresult[0]==0:
            verif=False
            print(verif)
        else:
            verif=True
            print(myresult[0])
            print(verif)
        return verif

    def descriProduit(self):
        query="SELECT description FROM produit"
        mycursor= self.__mydb.cursor()
        mycursor.execute(query)
        myresult=mycursor.fetchall()
        
        return myresult

    def details_produit(self,desc):
        query="SELECT * FROM produit WHERE description='"+desc+"'"
        mycursor= self.__mydb.cursor()
        mycursor.execute(query)
        myresult=mycursor.fetchall()

        return myresult

    def recordProduct(self):

        mycursor = self.__mydb.cursor()

        try:

            #sql = "INSERT INTO produit (reference, libelle, type, prix, quantite, delais) VALUES ('John', 'Highway 21', 'Fixe', 9, 10, 0)"

            sql = "INSERT INTO produit (reference, libelle, type, prix, quantite, delais) VALUES (%s, %s, %s, %s, %s, %s)"

            val = ("COUT001", "Couteau Suisse", "Fixe", 9, 10, 0)

            mycursor.execute(sql, val)

            self.__mydb.commit()

            print("ok")

        except:

            print("An exception occurred")

        