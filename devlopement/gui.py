from customtkinter import *
from CTkMenuBar import *
import subprocess
import webbrowser
import time
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
        donnees_string += f"{titre} - {recherche}\n"
    
    return donnees_string

def url():
    webbrowser.open("https://github.com/Ento9/Trends-Finder")

def dataCA():
    nom_fichier = "CA/last-research-CA.txt"
    with open(nom_fichier, 'r') as fichier:
        contenu = fichier.read()
    textbox2.configure(state="normal")
    textbox2.delete("1.0", "end")
    textbox2.insert("0.0", contenu)
    textbox2.configure(state="disabled")
    path = "CA/data-CA.txt"
    donnees_en_string = extraire_donnees_en_string(path)
    textbox.configure(state="normal")
    textbox.delete("1.0", "end")
    textbox.insert("0.0", donnees_en_string)
    textbox.configure(state="disabled")
    
    
    
def dataUS():
    nom_fichier = "US/last-research-US.txt"
    with open(nom_fichier, 'r') as fichier:
        contenu = fichier.read()
    textbox2.configure(state="normal")
    textbox2.delete("1.0", "end")
    textbox2.insert("0.0", contenu)
    textbox2.configure(state="disabled")
    path = "US/data-US.txt"
    donnees_en_string = extraire_donnees_en_string(path)
    textbox.configure(state="normal")
    textbox.delete("1.0", "end")
    textbox.insert("0.0", donnees_en_string)
    textbox.configure(state="disabled")
    
    
def dataMX():
    nom_fichier = "MX/last-research-MX.txt"
    with open(nom_fichier, 'r') as fichier:
        contenu = fichier.read()
    textbox2.configure(state="normal")
    textbox2.delete("1.0", "end")
    textbox2.insert("0.0", contenu)
    textbox2.configure(state="disabled")
    path = "MX/data-MX.txt"
    donnees_en_string = extraire_donnees_en_string(path)
    textbox.configure(state="normal")
    textbox.delete("1.0", "end")
    textbox.insert("0.0", donnees_en_string)
    textbox.configure(state="disabled")
    
    
def dataFR():
    nom_fichier = "FR/last-research-FR.txt"
    with open(nom_fichier, 'r') as fichier:
        contenu = fichier.read()
    textbox2.configure(state="normal")
    textbox2.delete("1.0", "end")
    textbox2.insert("0.0", contenu)
    textbox2.configure(state="disabled")
    path = "FR/data-FR.txt"
    donnees_en_string = extraire_donnees_en_string(path)
    textbox.configure(state="normal")
    textbox.delete("1.0", "end")
    textbox.insert("0.0", donnees_en_string)
    textbox.configure(state="disabled")

def aCA():
    label_st.configure(text="STATUS: analyzing...", text_color="#ffdd00")
    label_st.update()
    subprocess.run("python3 CA-search.py", shell=True)
    subprocess.run("python3 US-search.py", shell=True)
    subprocess.run("python3 MX-search.py", shell=True)
    subprocess.run("python3 FR-search.py", shell=True)
    label_st.configure(text="STATUS: done", text_color="#26bf15")
    label_st.update()

def analyse():
    label_st.configure(text="STATUS: analyzing...", text_color="#ffdd00")
    label_st.update()
    subprocess.run("python3 CA-search.py", shell=True)
    subprocess.run("python3 US-search.py", shell=True)
    subprocess.run("python3 MX-search.py", shell=True)
    subprocess.run("python3 FR-search.py", shell=True)
    label_st.configure(text="STATUS: done", text_color="#26bf15")
    label_st.update()


def pref():
    pref_menu = CTkToplevel(root)
    pref_menu.title("Trends Finder V0.3 Pre Release - Preference")
    label_p1 = CTkLabel(pref_menu, text="Preference", font=('Arial', 12))
    label_p1.pack()

    pref_frame = CTkFrame(pref_menu, border_width=1, border_color="#595959", width=470, height=400)
    pref_frame.pack(padx=10)

    label_type = CTkLabel(pref_frame, text="Sources", font=('Arial', 12)).grid(row=0, column=0, pady=5, padx=50)
    label_folder = CTkLabel(pref_frame, text="Directory", font=('Arial', 12)).grid(row=0, column=1, pady=5, padx=50)

    button_folder = CTkButton(pref_frame, text="Files", command=dataFR, font=('Arial', 10), text_color="white", fg_color="transparent", corner_radius=32, border_color="#6d7ea3", border_width=2,).grid(row=1, column=1, padx=5, pady=5)
    
    label_p3 = CTkLabel(pref_frame, text="Current Source", font=('Arial', 10)).grid(row=1, column=0, padx=5)
    textbox_pref = CTkTextbox(pref_frame, height=15).grid(row=2, column=0, padx=5, pady=5)

    pref_menu.geometry("400x500")
    pref_menu.resizable(0,0)
    

root = CTk()
root.geometry("400x500")
root.resizable(0,0)
set_appearance_mode("dark")

root.title("Trends Finder V0.4")



menu = CTkMenuBar(root)
btn_link = menu.add_cascade("Link")
dropdown1 = CustomDropdownMenu(widget=btn_link)
dropdown1.add_option(option="Project Page", command=url)

#btn_option = menu.add_cascade("Settings")
#dropdown2 = CustomDropdownMenu(widget=btn_option)
#dropdown2.add_option(option="Preferences", command=pref)

label = CTkLabel(root, text="Trends Finder", font=('Arial', 20, 'bold'), bg_color="#4484bd", width=200)
label.pack(pady=5)

label2 = CTkLabel(root, text="By Ento9", font=('Arial', 15, 'bold'), bg_color="#6381bf", width=150)
label2.pack(pady=1)

label3 = CTkLabel(root, text="DATA:", font=('Arial', 12))
label3.pack(pady=1)

textbox = CTkTextbox(root, font=('Arial', 15), width=275, height=150)
textbox.pack()

buttonFrame = CTkFrame(root)
buttonFrame.pack(pady=10)
buttonCA = CTkButton(buttonFrame, text="View Canada", command=dataCA, font=('Arial', 10), text_color="white", fg_color="transparent", corner_radius=32, border_color="#6d7ea3", border_width=2).grid(row=0, column=0, padx=5, pady=5)
buttonUS = CTkButton(buttonFrame, text="View USA", command=dataUS, font=('Arial', 10), text_color="white", fg_color="transparent", corner_radius=32, border_color="#6d7ea3", border_width=2).grid(row=0, column=1, padx=5, pady=5)
buttonMX = CTkButton(buttonFrame, text="View Mexico", command=dataMX, font=('Arial', 10), text_color="white", fg_color="transparent", corner_radius=32, border_color="#6d7ea3", border_width=2).grid(row=1, column=0, padx=5, pady=5)
buttonFR = CTkButton(buttonFrame, text="View France", command=dataFR, font=('Arial', 10), text_color="white", fg_color="transparent", corner_radius=32, border_color="#6d7ea3", border_width=2,).grid(row=1, column=1, padx=5, pady=5)

buttonAnalyse = CTkButton(root, text="Analyse", command=analyse, font=('Arial', 15), text_color="white", fg_color="transparent", corner_radius=32, border_color="#a30b0b", border_width=2, width=290)
buttonAnalyse.pack()

label = CTkLabel(root, text="Last Analyse", font=('Arial', 10, 'bold'))
label.pack()

textbox2 = CTkTextbox(root, font=('Arial', 15), width=275, height=15)
textbox2.pack()

label_st = CTkLabel(root, text="STATUS: none", font=('Arial', 10, 'bold'))
label_st.pack()

textbox.configure(state="disabled")
textbox2.configure(state="disabled")

root.mainloop()

