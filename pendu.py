from tkinter import Tk, Canvas, Frame, Button, PhotoImage, StringVar, CENTER, NW, E, W, BOTTOM
from numpy import random
from PIL import ImageTk
import tkinter.font as font
import string
import PIL.Image
import sys

#------------------------------------ paramétrage de la fenêtre -----------------------------
app = Tk()
#définition de la taille max et min
app.minsize(400, 380)
app.maxsize(400, 570)
#icon de la fenêtre, titre et le background
app.iconbitmap('Hangman.ico')
app.title("Pendu")
app.config(bg = "white")
#------------------------------------ paramétrage de la fenêtre -----------------------------

#------------------------------------------ widgets -----------------------------------------
#creation d'un canvas où on va dessiner les différentes images
WIDTH = 400
HEIGTH = 400
canvas = Canvas(app, width = WIDTH, height = HEIGTH, bg = "white", bd = 0)
#Image.photoimage : charge les images et les convertisses en objets image compatibles Tkinter
#pil.image.open : qui va charger l'image en mémoire
#pil.image.antialias : pour avoir une image plus nette
images = [ImageTk.PhotoImage(PIL.Image.open("pendu_1.gif").resize((WIDTH, HEIGTH), PIL.Image.Resampling.LANCZOS)),
		ImageTk.PhotoImage(PIL.Image.open("pendu_2.gif").resize((WIDTH, HEIGTH), PIL.Image.Resampling.LANCZOS)),
		ImageTk.PhotoImage(PIL.Image.open("pendu_3.gif").resize((WIDTH, HEIGTH), PIL.Image.Resampling.LANCZOS)),
		ImageTk.PhotoImage(PIL.Image.open("pendu_4.gif").resize((WIDTH, HEIGTH), PIL.Image.Resampling.LANCZOS)),
		ImageTk.PhotoImage(PIL.Image.open("pendu_5.gif").resize((WIDTH, HEIGTH), PIL.Image.Resampling.LANCZOS)),
		ImageTk.PhotoImage(PIL.Image.open("pendu_6.gif").resize((WIDTH, HEIGTH), PIL.Image.Resampling.LANCZOS)),
		ImageTk.PhotoImage(PIL.Image.open("morgan_pendu.png").resize((WIDTH, HEIGTH), PIL.Image.Resampling.LANCZOS)),
		ImageTk.PhotoImage(PIL.Image.open("morgan_merci.jpg").resize((WIDTH, HEIGTH), PIL.Image.Resampling.LANCZOS)),
		ImageTk.PhotoImage(PIL.Image.open("pot.jpg").resize((WIDTH, HEIGTH), PIL.Image.Resampling.LANCZOS))
	]
img = canvas.create_image(0, 0, anchor = NW, image = images[8])
canvas.pack(ipadx = 0, ipady = 0)
#création d'un widget frame où l'on va stocker d'autres widjets [ le clavier et les bouton play et quitter]
frame2 = Frame(app, bg = "white", bd = 0)
frame2.pack(pady = 5, ipadx = 0, ipady = 0)
alpha = Frame(frame2, width = 400, height = 45, bg = "white", bd = 0)
f = font.Font(family='Helvetica', slant = "italic")
btn0 = Button(alpha, text = "a", command = lambda: choix.set(alphabet[0]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn1 = Button(alpha, text = "b", command = lambda: choix.set(alphabet[1]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn2 = Button(alpha, text = "c", command = lambda: choix.set(alphabet[2]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn3 = Button(alpha, text = "d", command = lambda: choix.set(alphabet[3]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn4 = Button(alpha, text = "e", command = lambda: choix.set(alphabet[4]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn5 = Button(alpha, text = "f", command = lambda: choix.set(alphabet[5]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn6 = Button(alpha, text = "g", command = lambda: choix.set(alphabet[6]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn7 = Button(alpha, text = "h", command = lambda: choix.set(alphabet[7]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn8 = Button(alpha, text = "i", command = lambda: choix.set(alphabet[8]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn9 = Button(alpha, text = "j", command = lambda: choix.set(alphabet[9]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn10 = Button(alpha, text = "k", command = lambda: choix.set(alphabet[10]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn11 = Button(alpha, text = "l", command = lambda: choix.set(alphabet[11]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn12 = Button(alpha, text = "m", command = lambda: choix.set(alphabet[12]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn13 = Button(alpha, text = "n", command = lambda: choix.set(alphabet[13]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn14 = Button(alpha, text = "o", command = lambda: choix.set(alphabet[14]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn15 = Button(alpha, text = "p", command = lambda: choix.set(alphabet[15]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn16 = Button(alpha, text = "q", command = lambda: choix.set(alphabet[16]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn17 = Button(alpha, text = "r", command = lambda: choix.set(alphabet[17]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn18 = Button(alpha, text = "s", command = lambda: choix.set(alphabet[18]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn19 = Button(alpha, text = "t", command = lambda: choix.set(alphabet[19]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn20 = Button(alpha, text = "u", command = lambda: choix.set(alphabet[20]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn21 = Button(alpha, text = "v", command = lambda: choix.set(alphabet[21]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn22 = Button(alpha, text = "w", command = lambda: choix.set(alphabet[22]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn23 = Button(alpha, text = "x", command = lambda: choix.set(alphabet[23]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn24 = Button(alpha, text = "y", command = lambda: choix.set(alphabet[24]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn25 = Button(alpha, text = "z", command = lambda: choix.set(alphabet[25]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn26 = Button(alpha, text = "-", command = lambda: choix.set(alphabet[26]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn27 = Button(alpha, text = "é", command = lambda: choix.set(alphabet[27]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn28 = Button(alpha, text = "è", command = lambda: choix.set(alphabet[28]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
btn29 = Button(alpha, text = "à", command = lambda: choix.set(alphabet[29]), bg = "white", fg = "black" , width = 3, font = f, border = 0)
photo1 = PhotoImage(file = "quitter.png")
photoimage1 = photo1.subsample(10)
ferme = Button(frame2,image = photoimage1, bg = "white", bd = 0, anchor = E)
photo2 = PhotoImage(file = "play.png")
photoimage2 = photo2.subsample(10)
photo3 = PhotoImage(file = "replay.png")
photoimage3 = photo3.subsample(10)
play = Button(frame2, image = photoimage2, bg = "white", bd = 0, anchor = W)

#------------------------------------------ widgets -----------------------------------------

#------------------------------------ fonctions et variables  -------------------------------
alphabet = list(string.ascii_lowercase)
alphabet.append(list(string.punctuation)[12])
alphabet.append("é")
alphabet.append("è")
alphabet.append("à")
liste1 = []
liste2 = []
choix = StringVar()
erreurs = 0

def creer_carre_mot(mot = "Bienvenue, je vous attendais.."
	"\n Mr Morgan risque la pendaison.."
	"\n Pourrez-vous le sauver ?!",couleur_fond = "",couleur_texte = "black",x1 = 20,y1 = 340,x2 = 240,y2 = 400):
	global canvas
	carre_mot = canvas.create_rectangle(x1, y1, x2, y2, fill = couleur_fond)
	txt_mot = canvas.create_text(int(x2 - x1) / 2 + x1,int(y2 - y1) / 2 + y1,text = mot,justify = CENTER,state = DISABLED,fill = couleur_texte)
	liste1 = [carre_mot,txt_mot]
	return liste1
def creer_carre_erreur(erreurs = 0,couleur_fond = "",x1 = 300,y1 = 340,x2 = 380,y2 = 400):
	global canvas
	carre_erreur = canvas.create_rectangle(x1, y1, x2, y2, fill = couleur_fond)
	txt_erreur = canvas.create_text(int(x2 - x1) / 2 + x1,int(y2 - y1) / 2 + y1,text = "Erreurs {}".format(erreurs),justify = CENTER,state = DISABLED)
	liste2 = [carre_erreur,txt_erreur]
	return liste2

def fermer():
	globals()["choix"].set("ferme")
	sys.exit()

def compte_index(a):
	dico = {}
	b = 0
	for i in range(len(alphabet)):
		dico[alphabet[i]] = i
	for x in dico:
		if x == a:
			b = dico[a]
	del(dico)
	return b

def commencer():
	global mot_c,choix
	liste3 = []
	fichier = open("test.txt", "rt")
	for x in fichier:
		liste3.append(x.rstrip("\n"))
	mot = liste3[random.randint(len(liste3) - 1)]
	mot_l = list(mot)
	code = []
	for i in range(len(mot_l)):
		code.append("*")
	a = "*"
	while a in code and choix.get() != "ferme":
		if globals()["erreurs"] < 6:
			for i in globals()["liste1"]:
				globals()["canvas"].delete(i)
			for i in globals()["liste2"]:
				globals()["canvas"].delete(i)
			globals()["liste1"] = creer_carre_mot(code)
			globals()["liste2"] = creer_carre_erreur(erreurs)
			app.wait_variable(choix)
			lettre = choix.get()
			print(lettre)
			b = lettre.capitalize()
			if lettre in mot_l or b in mot_l:
				for x in range(len(mot_l)):
					if lettre == mot_l[x] or b == mot_l[x]:
						code[x] = mot_l[x]
				for i in globals()["liste1"]:
					globals()["canvas"].delete(i)
				for i in globals()["liste2"]:
					globals()["canvas"].delete(i)
				globals()["liste1"] = creer_carre_mot(code)
				globals()["liste2"] = creer_carre_erreur(erreurs)
			else:
				globals()["erreurs"] += 1
				for i in globals()["liste1"]:
					globals()["canvas"].delete(i)
				for i in globals()["liste2"]:
					globals()["canvas"].delete(i)
				if globals()["erreurs"] == 1:
					globals()["canvas"].itemconfigure(globals()["img"], image = globals()["images"][1])
					globals()["canvas"].image = globals()["images"][1]
				elif globals()["erreurs"] == 2:
					globals()["canvas"].itemconfigure(globals()["img"], image = globals()["images"][2])
					globals()["canvas"].image = globals()["images"][2]
				elif globals()["erreurs"] == 3:
					globals()["canvas"].itemconfigure(globals()["img"], image = globals()["images"][3])
					globals()["canvas"].image = globals()["images"][3]
				elif globals()["erreurs"] == 4:
					globals()["canvas"].itemconfigure(globals()["img"], image = globals()["images"][4])
					globals()["canvas"].image = globals()["images"][4]
				elif globals()["erreurs"] == 5:
					globals()["canvas"].itemconfigure(globals()["img"], image = globals()["images"][5])
					globals()["canvas"].image = globals()["images"][5]
				globals()["liste1"] = creer_carre_mot(code)
				globals()["liste2"] = creer_carre_erreur(erreurs)
			globals()["btn%s" %(compte_index(lettre))].config(state = "disable")
		else:
			for i in globals()["liste1"]:
				globals()["canvas"].delete(i)
			for i in globals()["liste2"]:
				globals()["canvas"].delete(i)
			globals()["canvas"].itemconfigure(globals()["img"], image = globals()["images"][6])
			globals()["canvas"].image = globals()["images"][6]
			globals()["liste1"] = creer_carre_mot("Vous n'aviez plus assez d'essais pour"
				"\ncontinuer .Le mot était « %s »"
				"\nVous avez perdu !!!" %(mot),couleur_fond = "#800000",couleur_texte = "white")
			globals()["erreurs"] = 0
			for ligne in range(3):
				for colonne in range(10):
					globals()["btn%d" %((ligne * 10) + colonne)].config(state = "disable")
			globals()["play"].config(image = photoimage3)
			globals()["play"].config(state = "normal")
			break
	if a not in code:
		for i in globals()["liste1"]:
			globals()["canvas"].delete(i)
		for i in globals()["liste2"]:
			globals()["canvas"].delete(i)
		globals()["canvas"].itemconfigure(globals()["img"], image = globals()["images"][7])
		globals()["canvas"].image = globals()["images"][7]
		globals()["liste1"] = creer_carre_mot("Bravo vous avez trouvé"
			"\nle mot « %s » !!!"
			"\nMr Morgan est sauvé."%(mot),couleur_fond = "#4d79ff",couleur_texte = "white")
		for ligne in range(3):
				for colonne in range(10):
					globals()["btn%d" %((ligne * 10) + colonne)].config(state = "disable")
		globals()["play"].config(image = photoimage3)
		globals()["play"].config(state = "normal")
	globals()["erreurs"] = 0

globals()["liste1"] = creer_carre_mot(couleur_fond = "white")
def jouer():
	globals()["canvas"].itemconfigure(globals()["img"], image = globals()["images"][0])
	globals()["canvas"].image = globals()["images"][0]
	globals()["play"].config(state = "disable")
	globals()["alpha"].pack()
	for ligne in range(3):
		for colonne in range(10):
			globals()["btn%d" %((ligne * 10) + colonne)].grid(row = ligne , column = colonne)
			if globals()["btn%d" %((ligne * 10) + colonne)]["state"] == "disabled":
				globals()["btn%d" %((ligne * 10) + colonne)]["state"] = "normal"
	commencer()

ferme.config(command = fermer)
play.config(command = jouer)
ferme.pack(side = BOTTOM, padx = 10, pady = 5)
play.pack(side = BOTTOM, padx = 10, pady = 5)
#------------------------------------ fonctions et variables  -------------------------------

app.protocol("WM_DELETE_WINDOW", fermer)
app.mainloop()