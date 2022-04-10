import tkinter as tk

from tkinter.constants import END, INSERT, LEFT, RIGHT, TOP, Y

from prettytable import PrettyTable

import tkinter.ttk as ttk

from Produit import Produit

from ProduitFixe import ProduitFixe

from ProduitDevis import ProduitDevis

from Bdd import Bdd
from ajouter_image import ajout_image
from details import detail
from functools import partial



class Application(tk.Tk):

    def __init__(self):

        # instanciation de la BDD

        # self.__bdd = Bdd()

        # self.__bdd.recordProduct()

        

        tk.Tk.__init__(self)

        self.geometry('800x600')

        m = tk.Menu(self)

        sm1 = tk.Menu(self)

        m.add_cascade (label = "Fichier", menu = sm1)

        sm1.add_command (label = "Quitter", command = self.destroy)

        self.config(menu = m, width = 200)

        self.creer_widgets()

        self.creerPrettyListe()



        self.__listeProduits = []

        self.__chargerDepuisBDD()

    

    def __chargerDepuisBDD(self):

        bdd = Bdd()

        resu = bdd.chargerLesProduits()

        for unProd in resu:

            if(unProd[5] == "FIXE"):

                leNew = ProduitFixe(unProd[0], unProd[1], unProd[2], unProd[3])

            else:

                leNew = ProduitDevis(unProd[0], unProd[1], unProd[4])

            self.__listeProduits.append(leNew)

            print(unProd)

        self.updateListe()

        #self.__listeProduits = 

#<bound method Bdd.descriProduit of <Bdd.Bdd object at 0x7fb9d5006c10>>

    def creer_widgets(self):

        # Partie gauche pour afficher la liste des produits

        self.liste = tk.Label(self, text="Liste des produits")



        self.reference = tk.Label(self, text="Référence de l'article : ")

        self.referenceEntry = tk.Entry ()

        self.description = tk.Label(self, text="Description de l'article : ")

        self.descriptionEntry = tk.Entry ()

        self.typeProduit = tk.Label(self, text="Type de tarif : ")

        self.typeProduitListe = ttk.Combobox(self, values=["Tarif fixe", "Sur devis"])

        self.prix = tk.Label(self, text="Prix de l'article : ")

        self.prixEntry = tk.Entry ()

        self.quantite = tk.Label(self, text="Quantité en stock : ")

        self.quantiteEntry = tk.Entry ()

        self.boutonOk = tk.Button(self, text="Ajouter", command=self.ajouter)

        bdd=Bdd()
        myresult=bdd.descriProduit()
        tableau=[]
        for result in myresult:
            tableau.append(result[0])

        self.descriptionProduit = ttk.Combobox(self)
        self.descriptionProduit["values"]=tableau
        desc=self.descriptionProduit.get()
        
        det=detail()
        details_arg = partial(det.afficher_details, "RTX 3080")
        test=partial(print,desc)
        self.detail=ttk.Button(self,text="Détails",command= details_arg)#details_arg    #JE N'ARRIVE PAS A RECUPERER LA VALUE DE LA COMBOBOX
        # ajout=ajout_image()       #j'ai essayé un print mais cela ne retourne seulement une ligne vide
        # self.image=ttk.Button(self,text="Ajouter une image",command=ajout.ajout_image)
        #DONC DANS LA FONCTION afficher_details, je ne peux rien afficher car je n'aurai pas de desc qui fait fonctionner la fonction.

        self.liste.pack(side=LEFT, fill = Y)



        self.reference.pack(side=TOP)

        self.referenceEntry.pack(side=TOP)

        self.description.pack(side=TOP)

        self.descriptionEntry.pack(side=TOP)

        self.typeProduit.pack(side=TOP)

        self.typeProduitListe.pack(side=TOP)

        self.prix.pack(side=TOP)

        self.prixEntry.pack(side=TOP)

        self.quantite.pack(side=TOP)

        self.quantiteEntry.pack(side=TOP)

        self.boutonOk.pack(side=TOP)

        self.descriptionProduit.pack(side=TOP)
        
        self.detail.pack(side=TOP)
        # self.image.pack(side=TOP)


    def creerPrettyListe(self):

        win=self



        self.listeP=tk.Text(win)#Inside text widget we would put our table



        x=PrettyTable()



        x.field_names = ["Référence", "Description", "Type", "Tarif", "Quantité"]



        x.add_row(["p0001", "Pneu michelin 205/50/17", "Fixe", 129.95, 18])

        x.add_row(["p0002", "Pneu michelin 205/45/17", "Fixe", 139.95, 8])

        x.add_row(["p0003", "Changement amortisseurs", "Devis", 0, 0])

        x.add_row(["p0004", "Pneu Uniroyal pluie plus 205/50/17", "Fixe", 149.95, 12])



        self.listeP.insert(INSERT,x)#Inserting table in text widget

        self.listeP.pack(side=LEFT)



    def creerListe(self):

         # take the data

        lst = [(1,'Raj','Mumbai',19),

            (2,'Aaryan','Pune',18),

            (3,'Vaishnavi','Mumbai',20),

            (4,'Rachna','Mumbai',21),

            (5,'Shubham','Delhi',21)]

        

        # find total number of rows and

        # columns in list

        total_rows = len(lst)

        total_columns = len(lst[0])

        # code for creating table

        for i in range(total_rows):

            for j in range(total_columns):

                  

                self.e = tk.Entry(self, width=20, fg='blue',

                               font=('Arial',16,'bold'))

                  

                self.e.pack()

                # self.e.grid(row=i, column=j)

                self.e.insert(END, lst[i][j])

  

       

    

    def ajouter(self):

        unProduit = Produit("X001", "Pelle à neige")

        unProduit.affiche()

        """

        unProduitFixe = ProduitFixe("X0002", "Savon de marseille", 4.90, 50)

        unProduitFixe.affiche()



        unProduitDevis = ProduitDevis("X0003", "Assistance mise en service", 7)

        unProduitDevis.affiche()



        self.__listeProduits.append(unProduit)

        self.__listeProduits.append(unProduitFixe)

        self.__listeProduits.append(unProduitDevis)

        """

        laRef = self.referenceEntry.get()

        leLib = self.descriptionEntry.get()

        leType = self.typeProduitListe.get()



        if (leType == "Sur devis"):

            leNew = ProduitDevis(laRef, leLib, 7)

        else:

            lePrix = self.prixEntry.get()

            laQte = self.quantiteEntry.get()

            leNew = ProduitFixe(laRef, leLib, lePrix, laQte)



        self.__listeProduits.append(leNew)

        self.updateListe()



        print('Produit ajouté avec succès')



    def updateListe(self):        

        self.listeP.destroy()

        self.listeP=tk.Text(self)

        x=PrettyTable()



        x.field_names = ["Référence", "Description", "Type", "Tarif", "Quantité"]

        for p in self.__listeProduits:

            if(isinstance(p, ProduitFixe)):

                x.add_row([p.getReference(), p.getLibelle(), "Fixe", p.getPrix(), p.getQuantite()])

            else:

                x.add_row([p.getReference(), p.getLibelle(), "Devis", 0, 0])



        self.listeP.insert(INSERT, x)#Inserting table in text widget

        self.listeP.pack(side=LEFT)



if __name__ == "__main__":

    app = Application()

    app.title("Ma Première App :-)") 

    app.mainloop()

    