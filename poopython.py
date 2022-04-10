import tkinter as tk
from tkinter import *
from tkinter import ttk
from Produit import Produit
from prettytable import PrettyTable
x=PrettyTable()

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.listeproduit=[]
        self.creer_widgets()

    def creer_widgets(self):
        self.geometry("800x600")
        self.label1 = tk.Label(self, text="Référence de l'article : ")
        self.ref = tk.Entry(self)
        
        menubar=Menu(self)
        self.config(menu=menubar)

        menufichier=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Fichier", menu=menufichier)

        menufichier.add_command (label="Quitter", command=self.quit)

        self.label2 = tk.Label(self, text="Description de l'article : ")
        self.desc = tk.Entry(self)

        
        self.label3 = tk.Label(self, text="Type de tarif : ")
        self.typep = ttk.Combobox(self,values=["type1","type2","type3"])

        self.label4 = tk.Label(self, text="Prix de l'article : ")
        self.prix = tk.Entry(self)

        self.label5 = tk.Label(self, text="Quantité en stock : ")
        self.quantite = tk.Entry(self)

        self.bouton1 = tk.Button(self, text="Ajouter", command=self.ajouter)
        #self.bouton2 = tk.Button(self, text="Quitter", command=self.afficher)
        #self.bouton3=tk.Button(self,text="Afficher Objets", command=self.afficher)
        
        self.label1.pack()
        self.ref.pack()

        self.label2.pack()
        self.desc.pack()

        self.label3.pack()
        self.typep.pack()

        self.label4.pack()
        self.prix.pack()

        self.label5.pack()
        self.quantite.pack()

        self.bouton1.pack()
        #self.bouton2.pack()
        #self.bouton3.pack()

        x.field_names = ["Référence","Description","Type","Tarif","Quantité"]
        x.add_row([1,"article1","type1",1234,12])
        x.add_row([2,"article2","type2",5678,13])
        x.add_row([3,"article3","type3",1454,11])
        tableau=x.get_string()
        self.table=tk.Label(self,text=tableau)
        self.table.pack()

    def ajouter(self):
        reference=self.ref.get()
        description=self.desc.get()
        type1=self.typep.get()
        prix1=self.prix.get()
        quantite1=self.quantite.get()
        p = Produit(reference,description,type1,prix1,quantite1)
        print(p.afficher())
        self.listeproduit.append(p)
        self.table.destroy()
        for a in range (len(self.listeproduit)):
            x.add_row([self.listeproduit[a]._reference,self.listeproduit[a]._desc,self.listeproduit[a]._type1,self.listeproduit[a]._prix,self.listeproduit[a]._quantite])
        tableau=x.get_string()
        self.table=tk.Label(self,text=tableau)
        self.table.pack()
        
    #def afficher(self):
        #for a in range(len(self.listeproduit)):
            #print(self.listeproduit[a].afficher())
        #x.add_row([reference,description,type1,prix1,quantite1])
        #tableau=x.get_string()
        #self.table.destroy()
        #self.table=tk.Label(self,text=tableau)
        #self.table.pack()

if __name__ == "__main__":
    app = Application()
    app.title("Article")
    app.mainloop()
