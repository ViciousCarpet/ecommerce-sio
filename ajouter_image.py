import tkinter as tk

from tkinter.constants import END, INSERT, LEFT, RIGHT, TOP, Y

from prettytable import PrettyTable

import tkinter.ttk as ttk

from Produit import Produit

from ProduitFixe import ProduitFixe

from ProduitDevis import ProduitDevis

from Bdd import Bdd
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import mysql.connector
import io
from tkinter import ttk

class ajout_image(tk.Tk):
    def __init__(self):
        self.geometry("800x600")
        m=tk.Menu(self)
        sm1=tk.Menu(self)
        m.add_cascade(label="Fichier",menu=sm1)
        sm1.add_command(label="Quitter",command=self.destroy)
        self.config(menu=m,width=200)
        self.creer_widgets()
    
    def creer_widgets(self):
        id = Entry(self, width=10, font=("Helvetica", 20), bd=3)
        id.pack()

        browse_button = Button(self,text ='Browse',command = lambda:open_file())
        browse_button.pack()

        display_button = Button(self,text ='display',command =lambda:display_file())
        display_button.pack()

        display_table_button = Button(self,text ='display Table',command =lambda:display_Table())
        display_table_button.pack()
    
    def display_Table(self):

        query = "SELECT * FROM image_db"
        person = mysql.connector.connect(host="localhost", user="root", password="", database="image")
        cursor_variable = person.cursor()
        cursor_variable.execute(query)

        vertical_scrollbar = ttk.Scrollbar(root)
        vertical_scrollbar.pack(side=RIGHT, fill=Y)

        my_tree = ttk.Treeview(root, yscrollcommand= vertical_scrollbar.set)
        my_tree.pack()

        vertical_scrollbar.config(command= my_tree.yview)

        style = ttk.Style(root)
        style.theme_use("winnative")
        style.configure(".", font=("Helvetica", 11))
        style.configure("Treeview.Heading", font=("Helvetica", 11, "bold"))

        my_tree['columns'] = ("id", "data")
        my_tree.column("#0", width=0, stretch='NO')
        my_tree.column("id", width=50, anchor='w')
        my_tree.column("data", width=130, anchor='w')


        my_tree.heading("#0", anchor='w', text='Label')
        my_tree.heading("id", anchor='w', text="Id")
        my_tree.heading("data", anchor='w', text="Image")

        count = 0

        for record in cursor_variable:
            # print(record)
            my_tree.insert(parent='', index='end', iid=count, text='Parent',
                                values=(record[0], record[1]))
            count += 1

        person.close()


def display_file(self):

    id2 = id.get()
    person = mysql.connector.connect(host="localhost", user="root", password="", database="image")
    cursor_variable = person.cursor()
    sql = "SELECT data FROM image_db WHERE id = '" + id2 + "'"
    cursor_variable.execute(sql)
    all_data = cursor_variable.fetchall()
    image = all_data[0][0]
    image = Image.open(io.BytesIO(image))
    image.show()
    person.commit()
    person.close()


def open_file(self):
    self.filename = filedialog.askopenfilename(initialdir="/Users/write/PycharmProjects/slider/img", title='Select a File',
                                               filetypes=(('png files', '*.png'), ('jpeg files', '*.jpeg'),
                                                          ('jpg files', '*.jpg')))
    my_label = Label(self, text=self.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(self.filename))
    path = self.filename
    id1 = id.get()


    person = mysql.connector.connect(host="localhost", user="root", password="", database="image")
    cursor_variable = person.cursor()
    thedata = open(self.filename, 'rb').read()
    sql = "INSERT INTO image_db (id,data) VALUES ('" + id1 + "',%s)"
    cursor_variable.execute(sql, (thedata,))
    person.commit()
    person.close()

if __name__=="__main__":
    addimg=ajout_image()
    addimg.title("Ajout d'image")
    addimg.mainloop()
    addimg.mainloop()
