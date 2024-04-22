import tkinter as tk
from tkinter import *
import subprocess
import webbrowser
import os
import re

def extraire_donnees_en_string(nom_fichier):
    with open(nom_fichier, 'r') as fichier:
        texte = fichier.read()

    pattern = r'<div class="title ng-binding">(.*?)</div>\s*<div class="traffic-count ng-binding">(.*?)</div>'
    
    resultats = re.findall(pattern, texte, re.DOTALL)
    
    donnees_string = ""
    
    for titre, recherche in resultats:

        recherche = recherche.replace('searches', '').strip()
        donnees_string += f"{titre} - {recherche} searches\n"
    
    return donnees_string

def url():
    webbrowser.open("https://github.com/Ento9/Trends-Finder")

def dataCA():
    path = "CA/data-CA.txt"
    donnees_en_string = extraire_donnees_en_string(path)
    textbox.config(state="normal")
    textbox.delete(1.0, tk.END)
    textbox.insert(tk.INSERT, donnees_en_string)
    textbox.config(state="disabled")
    
def dataUS():
    path = "US/data-US.txt"
    donnees_en_string = extraire_donnees_en_string(path)
    textbox.config(state="normal")
    textbox.delete(1.0, tk.END)
    textbox.insert(tk.INSERT, donnees_en_string)
    textbox.config(state="disabled")
    
def dataMX():
    path = "MX/data-MX.txt"
    donnees_en_string = extraire_donnees_en_string(path)
    textbox.config(state="normal")
    textbox.delete(1.0, tk.END)
    textbox.insert(tk.INSERT, donnees_en_string)
    textbox.config(state="disabled")
    
def dataFR():
    path = "FR/data-FR.txt"
    donnees_en_string = extraire_donnees_en_string(path)
    textbox.config(state="normal")
    textbox.delete(1.0, tk.END)
    textbox.insert(tk.INSERT, donnees_en_string)
    textbox.config(state="disabled")
    

def analyse():
    commande = "./RUN"
    subprocess.Popen(["x-terminal-emulator", "-e", "bash", "-c", commande])

root = tk.Tk()
root.resizable(0,0)

root.geometry("600x750")
root.title("Trends Finder V0.2 & GUI")

menu = tk.Menu(root)

link_menu = tk.Menu(menu, tearoff=0)
link_menu.add_command(label='Project Page', command=url)
menu.add_cascade(label='Link', menu=link_menu)

label = tk.Label(root, text="Trends Finder", font=('Arial', 20, "bold"))
label.pack(padx=20, pady=20)

label3 = tk.Label(root, text="By Ento9", font=('Arial', 8))
label3.pack()
label3.config(bg= "gray51", fg= "white")

label2 = tk.Label(root, text="Data:", font=('Arial', 15))
label2.pack(padx=20, pady=5)

textbox = tk.Text(root)
textbox.pack(padx=20, pady=20)


button = tk.Button(root, text="Analyze", command=analyse, font=('Arial', 15), width=15, height=1)
button.pack()

buttonCA = tk.Button(root, text="View Canada", command=dataCA, font=('Arial', 10))
buttonCA.pack()

buttonUS = tk.Button(root, text="View USA", command=dataUS, font=('Arial', 10))
buttonUS.pack()

buttonMX = tk.Button(root, text="View Mexico", command=dataMX, font=('Arial', 10))
buttonMX.pack()

buttonFR = tk.Button(root, text="View France", command=dataFR, font=('Arial', 10))
buttonFR.pack()

root.configure(menu=menu)

root.mainloop()










