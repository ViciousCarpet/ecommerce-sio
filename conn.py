import tkinter as tk

from tkinter.constants import END,INSERT,LEFT,RIGHT, TOP,YES

import tkinter.ttk as ttk
from pythonprof import Application
from Bdd import Bdd

class Conn(tk.Tk):
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
        self.llogin=tk.Label(self,text="Login :")
        self.login=tk.Entry()
        self.lmdp=tk.Label(self,text='Mot de passe :')
        self.mdp=tk.Entry(self, show="*")
        self.llogin.pack()
        self.login.pack()
        self.lmdp.pack()
        self.mdp.pack()
        self.valider=tk.Button(self,text="Valider",command= self.connecter)
        self.valider.pack()
    
    def connecter(self):
        lgn=self.login.get()
        mdp=self.mdp.get()
        bdd=Bdd()
        if(bdd.connexion(lgn,mdp))==True:
            self.destroy()
            app=Application()
            print("Ca rentre comme dans du beurre")
        

if __name__=="__main__":
    co=Conn()
    co.title("Connexion")
    co.mainloop()
