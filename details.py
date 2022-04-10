import tkinter as tk

from tkinter.constants import END, INSERT, LEFT, RIGHT, TOP, Y

from prettytable import PrettyTable

import tkinter.ttk as ttk

from Produit import Produit

from ProduitFixe import ProduitFixe

from ProduitDevis import ProduitDevis

from Bdd import Bdd
from ajouter_image import ajout_image


class detail(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("800x600")
        m=tk.Menu(self)
        sm1=tk.Menu(self)
        m.add_cascade(label="Fichier",menu=sm1)
        sm1.add_command(label="Quitter",command=self.destroy)
        self.config(menu=m,width=200)
        self.creer_widgets()

    def creer_widgets(self):
        self.dref=tk.Label(self,text="Référence :")
        self.ddesc=tk.Label(self,text='Description :')
        self.dprix=tk.Label(self,text='Prix :')
        self.dquantite=tk.Label(self,text="Quantité :")
        self.ddelai=tk.Label(self,text="Délai :")
        self.dtype=tk.Label(self,text="Type :")
    
    def afficher_details(self,desc):
        
        bdd=Bdd()
        myresult=bdd.details_produit(desc)
        print(myresult)
        self.drref = tk.Label(self, text="Référence de l'article : "+myresult[0])
        self.drdesc = tk.Label(self, text="Description de l'article : "+myresult[1])
        self.drprix = tk.Label(self, text="Prix du produit : "+myresult[2])
        self.drquantite = tk.Label(self, text="Quantité d'articles : "+myresult[3])
        self.drdelai = tk.Label(self, text="Délai d'obtention de l'article : "+myresult[4])
        self.drtype = tk.Label(self, text="Type d'article : "+myresult[5])
        self.dref.pack()
        self.drref.pack()

        self.ddesc.pack()
        self.drdesc.pack()

        self.dprix.pack()
        self.drprix.pack()

        self.drquantite.pack()
        self.dquantite.pack()

        self.drdelai.pack()
        self.ddelai.pack()

        self.drtype.pack()
        self.dtype.pack()
        

if __name__=="__main__":
    det=detail()
    det.title("Détails")
    det.mainloop()