from tkinter import Tk, Canvas, Button, Label, PhotoImage, ALL, N, W, E
from random import randrange
import os
import pickle
import time

def EcranDePresentation():
    global DebutJeu
    if DebutJeu!=1:
        AffichageScore.configure(text="",font=('Fixedsys',16))
        AffichageVie.configure(text="",font=('Fixedsys',16))
        can.delete(ALL)
        fen.after(1500,Titre)

# On afficher le nom du jeu � l'�cran

def Titre():
    global DebutJeu
    if DebutJeu!=1:
        can.create_text(320,240,font=('Fixedsys',24),text="SPACE INVADERS",fill='blue')
        fen.after(2000,Titre2)

# On affiche le nom de l'auteur ( It's me !! :p )

def Titre2():
    global DebutJeu
    if DebutJeu!=1:
        can.create_text(320,270,font=('Freshbot',18),text="By Matt",fill='red')
        fen.after(3000,LoadMeilleurScore)

# Cette fonction va permettre d'enregistrer
# le meilleur score

def SaveMeilleurScore(resultat):
    FichierScore=open('HighScore','rb')
    lecture=pickle.load(FichierScore)

    # Si le score r�alis� � la fin de la partie
    # est sup�rieur � celui d�j� enregistr� dans le fichier
    # alors on remplace ce dernier par le nouveau score record
    
    if resultat>lecture:
        FichierScore=open('HighScore','wb')
        pickle.dump(resultat,FichierScore)
        FichierScore.close()
        fen.after(2000,MessageRecord)
    else:
        fen.after(15000,EcranDePresentation)
    FichierScore.close()

# Cette fonction affiche un message
# lui indiquant qu'il a �tabli un
# nouveau record :D

def MessageRecord():
    can.delete(ALL)
    can.create_text(320,240,font=('Georgia',18),text="Vous avez �tabli un nouveau record !!",fill='red')
    fen.after(3000,LoadMeilleurScore)
        
# Quant � cette fonction elle va permettre
# de lire le meilleur score afin de l'afficher

def LoadMeilleurScore():
    global DebutJeu
    if DebutJeu!=1:
        FichierScore=open('HighScore','rb')
        lecture=pickle.load(FichierScore)
        can.delete(ALL)
        can.create_text(320,240,font=('Fixedsys',24),text="HIGH SCORE",fill='blue')
        can.create_text(320,270,font=('Fixedsys',24),text=str(lecture),fill='blue')
        FichierScore.close()
        fen.after(3000,EcranDePresentation)

# Cette fonction permet de v�rifier
# l'existence d'un fichier

def existe(fname):
    try:
        f=open(fname,'r')
        f.close()
        return 1
    except:
        return 0

# Cette fonction permet de r�initialiser le jeu
# selon la volont� du joueur de recommencer une partie

def new_game():
    global xe,ye,xe2,ye2,xe3,ye3,LimiteAvancement,dx,ListeCoordEnnemis,ListeEnnemis,ObusEnnemi,flag,photo,NbreEnnemis,Score,ViesJoueur
    global ListeAbri,CoordonneesBriques,projectile,feu,feuEnnemi,PasAvancement
    global dyobus,dyobusEnnemi,DebutJeu,BonusActif,dxeb,EnnemiBonus,Mort,photo,PasMax,NbreEnRangees
    
    DebutJeu=1

    # On remet l'image d'origine

    base_path = os.path.dirname(os.path.abspath(__file__))
    photo=PhotoImage(file=os.path.join(base_path, 'earth.gif'))
    can.create_image(320,240,image=photo)

    Mort=0

    # On efface tout l'cran
    
    can.delete(ALL)
    can.create_image(320,240,image=photo)

    # Coordonnes de dpart des ennemis
    # pour chaque catgorie
    
    xe,ye=20,20
    xe2,ye2=20,80
    xe3,ye3=20,160
    
    LimiteAvancement=1
    if len(ObusEnnemi)==1:
        can.delete(ObusEnnemi[0])
    dx=1

    # Pas d'avancement d'un obus
    # tir par le joueur
    
    dyobus=20

    # Pas d'avancement d'un obus
    # tir par un ennemi
    
    dyobusEnnemi=10
    feu=0
    ViesJoueur=3
    Score=0
    feuEnnemi=0
    
    Ennemis1=[]
    Ennemis2=[]
    Ennemis3=[]
    ListeEnnemis=[Ennemis1,Ennemis2,Ennemis3]
    
    Ennemis=[]
    projectile=[]
    
    CoordEnnemis1=[]
    CoordEnnemis2=[]
    CoordEnnemis3=[]
    ListeCoordEnnemis=[CoordEnnemis1,CoordEnnemis2,CoordEnnemis3]
    
    NbreEnnemis1=6
    NbreEnnemis2=6
    NbreEnnemis3=6
    PasAvancement=0
    NbreEnnemis=[NbreEnnemis1,NbreEnnemis2,NbreEnnemis3]
    
    v=0

    BonusActif=0
    dxeb=5
    EnnemiBonus=[]

    Creation_Abris()
    Creation_CanonMobile()

    # On dtermine de manire alatoire
    # le nombre de temps avant qu'apparaisse
    # le premier ennemi bonus du jeu :)
    
    fen.after(randrange(60000,100000,100),CreationEnnemiBonus)


    AffichageScore.configure(text="Score : "+str(Score),font=('Fixedsys',16))
    AffichageVie.configure(text="Lives : "+str(ViesJoueur),font=('Fixedsys',16))
    

    # Appel des fonctions de cration des ennemis
    # pour recrer un bataillon de vaisseaux hostiles
    # prts en dcoudre nouveau avec le joueur !!
    
    while v<6:
        Ennemi_Categorie1()
        Ennemi_Categorie2()
        Ennemi_Categorie3()
        v+=1

    flag=1
   
        
# Cette fonction permet de cr�er les abris
# assurant la d�fense en papier du canon mobile XD

def Creation_Abris():
    global ListeAbris,CoordonneesBriques

    ListeAbris=[]
    CoordonneesBriques=[]

    i=0

    x=40
    y=340

    while i<3:
        limX=x+120
        limY=y+60
        departx=x
        while y<limY:
            while x<limX:
                ListeAbris.append(can.create_rectangle(x,y,x+20,y+20,fill='grey'))
                CoordonneesBriques.append([x,y])
                x+=20
            x=departx
            y+=20
        i+=1
        x+=220
        y-=60

# Cette fonction permet de cr�er le nerf de la guerre
# ==> Le canon mobile \o/

def Creation_CanonMobile():
    global canon,xc1,xc2,yc1,yc2
    canon=[]

    xc1=20
    yc1=440

    # Cr�ation du canon

    canon.append(can.create_rectangle(xc1,yc1,xc1+20,yc1+20,fill='green'))

    xc2=xc1-20
    yc2=yc1+20

    # Cr�ation de la plate-forme du canon

    canon.append(can.create_rectangle(xc2,yc2,xc2+60,yc2+20,fill='green'))
    
    

# Les 3 fonctions ci-dessous vont permettre de cr�er les ennemis du jeu

# Cr�ation de la 1er cat�gorie d'ennemis du jeu

def Ennemi_Categorie1():
    global ListeEnnemis,ListeCoordEnnemis,xe,ye
    ListeCoordEnnemis[0].append([xe,ye])
    Ennemis=[]
    Ennemis.append(can.create_rectangle(xe,ye,xe+60,ye+20,fill='blue'))
    Ennemis.append(can.create_rectangle(xe,ye,xe+20,ye+40,fill='blue'))
    Ennemis.append(can.create_rectangle(xe+40,ye,xe+60,ye+40,fill='blue'))
    ListeEnnemis[0].append(Ennemis)
    xe=xe+80

# Cr�ation de la 2e cat�gorie d'ennemis du jeu

def Ennemi_Categorie2():
    global ListeEnnemis,ListeCoordEnnemis,xe2,ye2
    ListeCoordEnnemis[1].append([xe2,ye2])
    Ennemis=[]
    Ennemis.append(can.create_rectangle(xe2,ye2,xe2+20,ye2+40,fill='violet'))
    Ennemis.append(can.create_rectangle(xe2+40,ye2,xe2+60,ye2+40,fill='violet'))
    Ennemis.append(can.create_rectangle(xe2+20,ye2+20,xe2+40,ye2+60,fill='violet'))
    ListeEnnemis[1].append(Ennemis)
    xe2=xe2+80

# Cr�ation de la 3e cat�gorie d'ennemis du jeu

def Ennemi_Categorie3():
    global ListeEnnemis,ListeCoordEnnemis,xe3,ye3
    ListeCoordEnnemis[2].append([xe3,ye3])
    Ennemis=[]
    Ennemis.append(can.create_rectangle(xe3+20,ye3,xe3+40,ye3+60,fill='brown'))
    Ennemis.append(can.create_rectangle(xe3,ye3+20,xe3+60,ye3+40,fill='brown'))
    ListeEnnemis[2].append(Ennemis)
    xe3=xe3+80

# Cette fonction va permettre de cr�er
# l'ennemi bonus du jeu

def CreationEnnemiBonus():
    global EnnemiBonus,xeb,yeb,BonusActif,DebutJeu,CoordEnnemiBonus,dxeb,flag

    if flag!=0:
        if BonusActif!=1:
            BonusActif=1
            dxeb=5
            hasard=randrange(0,10,1)
            if hasard>=5:
                xeb=0
                dxeb=dxeb
            else:
                xeb=630
                dxeb=-dxeb
            yeb=randrange(80,400,10)
            EnnemiBonus.append(can.create_oval(xeb,yeb,xeb+35,yeb+15,fill='red'))
            EnnemiBonus.append(can.create_oval(xeb+5,yeb+5,xeb+10,yeb+10,fill='yellow'))
            EnnemiBonus.append(can.create_oval(xeb+15,yeb+5,xeb+20,yeb+10,fill='yellow'))
            EnnemiBonus.append(can.create_oval(xeb+25,yeb+5,xeb+30,yeb+10,fill='yellow'))
    
        

# Cette fonction va permettre d'animer
# le mouvement de l'ennemi bonus

def AnimationEnnemiBonus():
    global EnnemiBonus,xeb,yeb,dxeb,xtir,ytir,DebutJeu,BonusActif,projectile,flag,feu,Score

    if flag!=0 and DebutJeu!=0 and BonusActif!=0 :


        # Si l'ennemi bonus atteint l'autre bout de l'�cran
        # il s'auto-d�truit !! XD

        if dxeb>0:
            if xeb>=640:
                BonusActif=0
                can.delete(EnnemiBonus[0])
                can.delete(EnnemiBonus[1])
                can.delete(EnnemiBonus[2])
                can.delete(EnnemiBonus[3])
                xeb=0
                yeb=0
                EnnemiBonus=[]

                # D�termination al�atoire du temps d'appel
                # de la fonction qui va permettre de proc�der
                # � la cr�ation d'un nouvel ennemi bonus
                
                fen.after(randrange(60000,100000,100),CreationEnnemiBonus)
        else:
            if xeb<=20:
                BonusActif=0
                can.delete(EnnemiBonus[0])
                can.delete(EnnemiBonus[1])
                can.delete(EnnemiBonus[2])
                can.delete(EnnemiBonus[3])
                xeb=0
                yeb=0
                EnnemiBonus=[]
                fen.after(randrange(60000,100000,100),CreationEnnemiBonus)
                

        # On fait l'ennemi bonus avancer
                
        xeb=xeb+dxeb

        if len(EnnemiBonus)!=0:
            can.coords(EnnemiBonus[0],xeb,yeb,xeb+35,yeb+15)
            can.coords(EnnemiBonus[1],xeb+5,yeb+5,xeb+10,yeb+10)
            can.coords(EnnemiBonus[2],xeb+15,yeb+5,xeb+20,yeb+10)
            can.coords(EnnemiBonus[3],xeb+25,yeb+5,xeb+30,yeb+10)

        # On v�rifie si l'obus tir� par le joueur
        # touche l'ennemi bonus si tel est le cas
        # l'ennemi bonus est d�truit et on l'efface
        # de l'ecran pour faire le joueur empocher 300 pts !!

        if feu!=0:
            if ytir<=yeb and ytir>=yeb-25:
                if xtir>=xeb-10 and xtir<=xeb+40:
                    BonusActif=0

                    # On efface l'ennemi bonus
                    # ainsi que l'obus qui l'a touch�

                    if len(projectile)!=0:
                        can.delete(projectile[0])
                    can.delete(EnnemiBonus[0])
                    can.delete(EnnemiBonus[1])
                    can.delete(EnnemiBonus[2])
                    can.delete(EnnemiBonus[3])

                    # On utlise la fonction score afin
                    # d'afficher le nombre de points gagn�s
                    # � la suite de la destruction de
                    # l'ennemi bonus
                    
                    score(300,xeb,yeb,17.5,7.5)

                    # Gain de points ==> Modification du score du joueur
                    
                    Score+=300
                    AffichageScore.configure(text="Score : "+str(Score),font=('Fixedsys',16))

                    # On remet les coordonn�es de l'ennemi
                    # bonus � z�ro pour n'engendrer aucune
                    # erreur
                    
                    xeb,yeb=0,0
                    xtir,ytir=0,0

                    # On d�sactive l'animation de l'obus
                    # tir� par le joueur

                    feu=0

                    EnnemiBonus=[]

                    fen.after(randrange(15000,25000,100),CreationEnnemiBonus)
                
        # On reboucle le tout
        
        fen.after(50,AnimationEnnemiBonus)
    else:
        fen.after(50,AnimationEnnemiBonus)

# Cette fonction permet d'afficher
# le nombre de points gagn�s � la suite
# de la destruction d'un ennemi

def score(donnee,x,y,x2,y2):
    global afficherScore
    afficherScore.append(can.create_text(x+x2,y+y2,font=('Fixedsys',8),text=str(donnee)+' pts',fill='red'))
    fen.after(1500,EffacerScore)

# Cette fonction permet d'effacer
# le nombre de point gagn�s et affich�s
# suite � la destruction d'un ennemi

def EffacerScore():
    global afficherScore
    i=0
    while i<len(afficherScore):
        can.delete(afficherScore[i])
        i+=1

# La fonction ci-dessous permet
# d'animer le canon mobile selon
# la direction choisie par le joueur

def move(dx):
    global xc1,xc2,yc1,yc2,ViesJoueur,flag

    if ViesJoueur!=0 or flag!=0:
   
        xc1=xc1+dx
        xc2=xc2+dx

        # Si on arrive au bord de l'�cran
        # le canon mobile se retrouve bloqu�
        # afin de ne pas aller plus loin :p
        
        if xc2<=0:
            xc1=20
            xc2=0
            can.coords(canon[0],xc1,yc1,xc1+20,yc1+20)
            can.coords(canon[1],xc2,yc2,xc2+60,yc2+20)
        elif xc2>=600:
            xc1=600
            xc2=580
            can.coords(canon[0],xc1,yc1,xc1+20,yc1+20)
            can.coords(canon[1],xc2,yc2,xc2+60,yc2+20)
        else:
            can.coords(canon[0],xc1,yc1,xc1+20,yc1+20)
            can.coords(canon[1],xc2,yc2,xc2+60,yc2+20)

# Cette fonction va s'occuper de faire les ennemis se d�placer
# automatiquement dans le canevas histoire qu'ils puissent esquiver
# les tirs du joueur ( un genre d'IA � deux balles quoi !! XD )

def ennemis():
    global dx,feuEnnemi,NbreEnnemis,Xobus,Yobus,ListeCoordEnnemis,DebutJeu,NbreEnRangees
    global ListeEnnemis,PasAvancement,NbreEnnemis,flag,LimiteAvancement,BonusActif,PasMax

    if flag!=0 and len(NbreEnnemis)>=1 and DebutJeu!=0:

        # Si tous les ennemis ont �t� d�truits
        # ce n'est pas la peine d'ex�cuter l'animation
        # de quelque chose qui n'existe plus :p

        if NbreEnnemis!=0:
            i=0
            t=0
            PasAvancement+=1

            # On active le syst�me de tir des m�chants :p
            # ==> Armement des canons ==> Pr�t � d�truire l'ennemi ( le joueur )
            # Yes sir !! XD

            tir_ennemi()

            # Si jamais les ennemis atteignent le bas
            # de l'�cran la partie s'arr�te et le joueur
            # a perdu !! :p
           
            while i<len(ListeCoordEnnemis):
                while t<len(ListeCoordEnnemis[i]):
                    if ListeCoordEnnemis[i][t][1]>=420:
                        can.delete(ALL)
                        image()
                        flag=0
                        can.create_text(320,240,font=('Fixedsys',18),text="Game Over !!",fill='red')
                        feu=0
                        ArretAnimation=0
                        can.delete(canon[0])
                        can.delete(canon[1])
                        DebutJeu=0
                        SaveMeilleurScore(Score)
                        xc1,yc1=0,0
                        xc2,yc2=0,0
                    t+=1
                t=0
                i+=1

            i=0

            # Si les ennemis arrive au bout de l'�cran
            # leur direction s'inverse et ils vont
            # dans le sens oppos�

            dy=0
            

            if dx>0:

                # On va utiliser cette 2e variable afin
                # de s'assurer de l'inversion de la direction
                # des ennemis
                
                dx2=dx
                if len(ListeCoordEnnemis[0])!=0:
                    if ListeCoordEnnemis[0][len(ListeCoordEnnemis[0])-1][0]>=560:
                        dx=-dx2
                        dy=10
                if len(ListeCoordEnnemis[1])!=0:
                    if ListeCoordEnnemis[1][len(ListeCoordEnnemis[1])-1][0]>=560:
                        dx=-dx2
                        dy=10
                if len(ListeCoordEnnemis[2])!=0:
                    if ListeCoordEnnemis[2][len(ListeCoordEnnemis[2])-1][0]>=560:
                        dx=-dx2
                        dy=10
            elif dx<0:
                dx2=dx
                if len(ListeCoordEnnemis[0])!=0:
                    if ListeCoordEnnemis[0][0][0]<=20:
                        dx=-dx2
                        dy=10
                if len(ListeCoordEnnemis[1])!=0:
                    if ListeCoordEnnemis[1][0][0]<=20:
                        dx=-dx2
                        dy=10
                if len(ListeCoordEnnemis[2])!=0:
                    if ListeCoordEnnemis[2][0][0]<=20:
                        dx=-dx2
                        dy=10

            i=0
            t=0

            # On fait avancer tous les ennemis
            # du canevas
            
            while i<len(ListeCoordEnnemis):
                while t<len(ListeCoordEnnemis[i]):
                    ListeCoordEnnemis[i][t][0]=ListeCoordEnnemis[i][t][0]+dx
                    ListeCoordEnnemis[i][t][1]=ListeCoordEnnemis[i][t][1]+dy
                    t+=1
                i+=1
                t=0
            i=0
            while i<NbreEnnemis[0]:
                can.coords(ListeEnnemis[0][i][0],ListeCoordEnnemis[0][i][0],ListeCoordEnnemis[0][i][1],ListeCoordEnnemis[0][i][0]+60,ListeCoordEnnemis[0][i][1]+20)
                can.coords(ListeEnnemis[0][i][1],ListeCoordEnnemis[0][i][0],ListeCoordEnnemis[0][i][1],ListeCoordEnnemis[0][i][0]+20,ListeCoordEnnemis[0][i][1]+40)
                can.coords(ListeEnnemis[0][i][2],ListeCoordEnnemis[0][i][0]+40,ListeCoordEnnemis[0][i][1],ListeCoordEnnemis[0][i][0]+60,ListeCoordEnnemis[0][i][1]+40)
                i+=1
            i=0
            while i<NbreEnnemis[1]: 
                can.coords(ListeEnnemis[1][i][0],ListeCoordEnnemis[1][i][0],ListeCoordEnnemis[1][i][1],ListeCoordEnnemis[1][i][0]+20,ListeCoordEnnemis[1][i][1]+40)
                can.coords(ListeEnnemis[1][i][1],ListeCoordEnnemis[1][i][0]+40,ListeCoordEnnemis[1][i][1],ListeCoordEnnemis[1][i][0]+60,ListeCoordEnnemis[1][i][1]+40)
                can.coords(ListeEnnemis[1][i][2],ListeCoordEnnemis[1][i][0]+20,ListeCoordEnnemis[1][i][1]+20,ListeCoordEnnemis[1][i][0]+40,ListeCoordEnnemis[1][i][1]+60)
                i+=1
            i=0
            while i<NbreEnnemis[2]:
                can.coords(ListeEnnemis[2][i][0],ListeCoordEnnemis[2][i][0]+20,ListeCoordEnnemis[2][i][1],ListeCoordEnnemis[2][i][0]+40,ListeCoordEnnemis[2][i][1]+60)
                can.coords(ListeEnnemis[2][i][1],ListeCoordEnnemis[2][i][0],ListeCoordEnnemis[2][i][1]+20,ListeCoordEnnemis[2][i][0]+60,ListeCoordEnnemis[2][i][1]+40)
                i+=1
            fen.after(50,ennemis)
    else:
        fen.after(50,ennemis)



# Cette fonction g�re le tir des ennemis
# et v�rifie si un a atteint le canon
# mobile du joueur

def tir_ennemi():
    global feuEnnemi,Xobus,Yobus,ObusEnnemi,ListeCoordEnnemis,EnnemiChoisi,ChoixTireur,NbreEnnemis,flag,DebutJeu
    if flag!=0:
        if DebutJeu!=0:
            if feuEnnemi!=1 :
                feuEnnemi=1
                ObusEnnemi=[]
                i=0
                while i<len(EnnemiChoisi):
                    if EnnemiChoisi[i]==0:
                        del EnnemiChoisi[i]
                    i+=1
                    
                if len(EnnemiChoisi)==1:
                    Choix=0
                else:
                    Choix=randrange(0,len(EnnemiChoisi),1)

                # En fonction de la cat�gorie d'ennemis choisie
                # les coordonn�es d'un obus tir� ne seront pas
                # les m�mes pour tout le monde

                if len(ObusEnnemi)!=1:
                    if Choix==0:
                        if NbreEnnemis[0]!=0:

                            # La portion de code ci-dessous va permettre aux
                            # ennemis de choisir le canon avec lequel ils vont
                            # canarder le joueur et ses d�fenses

                            CanonChoisi=randrange(0,3,1)
                            
                            ChoixTireur=[]
                            ChoixTireur.append([ListeCoordEnnemis[0][randrange(0,NbreEnnemis[0],1)][0],ListeCoordEnnemis[0][randrange(0,NbreEnnemis[0],1)][1]])
                            Xobus=ChoixTireur[0][0]+9
                            Yobus=ChoixTireur[0][1]+40
                            
                            if CanonChoisi==1:
                                ObusEnnemi.append(can.create_rectangle(Xobus,Yobus,Xobus+2,Yobus+40,fill='orange'))
                            else:
                                Xobus=Xobus+40
                                ObusEnnemi.append(can.create_rectangle(Xobus,Yobus,Xobus+2,Yobus+40,fill='orange'))

                    elif Choix==1:
                        if NbreEnnemis[1]!=0:
                    
                            ChoixTireur=[]
                            ChoixTireur.append([ListeCoordEnnemis[1][randrange(0,NbreEnnemis[1],1)][0],ListeCoordEnnemis[1][randrange(0,NbreEnnemis[1],1)][1]])
                            Xobus=ChoixTireur[0][0]+29
                            Yobus=ChoixTireur[0][1]+60
                        
                            ObusEnnemi.append(can.create_rectangle(Xobus,Yobus,Xobus+2,Yobus+40,fill='orange'))

                    elif Choix==2:
                        if NbreEnnemis[2]!=0:
                        
                            ChoixTireur=[]
                            ChoixTireur.append([ListeCoordEnnemis[2][randrange(0,NbreEnnemis[2],1)][0],ListeCoordEnnemis[2][randrange(0,NbreEnnemis[2],1)][1]])
                            Xobus=ChoixTireur[0][0]+29
                            Yobus=ChoixTireur[0][1]+60
                            
                            
                            ObusEnnemi.append(can.create_rectangle(Xobus,Yobus,Xobus+2,Yobus+40,fill='orange'))

                    # On d�marre l'animation de l'obus
                    # tir� par un des ennemis
                       
                    AnimationObusEnnemi()
        

# Cette fonction permet d'animer l'obus tir�
# par un ennemi

def AnimationObusEnnemi():
    global xe,ye,dyobusEnnemi,Yobus,Xobus,ObusEnnemi,feuEnnemi,xc1,xc2,yc1,yc2,feu,ViesJoueur
    global PartieFinie,flag,projectile,DebutJeu,Score,Mort,ArretAnimation,canon
    if flag!=0:
        if feuEnnemi==1:
            Yobus=Yobus+dyobusEnnemi
            abri()
                                
            if Yobus>=480:
                if len(ObusEnnemi)==1:
                        can.delete(ObusEnnemi[0])
                feuEnnemi=0

            # Si un tir ennemi parvient � son objectif en
            # touchant le canon mobile du joueur ben il cr�ve ==> partie termin�e !! :p
                
            elif Xobus>=xc2 and Xobus<=xc2+60 and Yobus>=yc2 or Xobus>=xc1 and Xobus<=xc1+20 and Yobus>=yc1:
                can.delete(canon[0])
                can.delete(canon[1])
                if len(projectile)!=0:
                    can.delete(projectile[0])
                if len(ObusEnnemi)!=0:
                    can.delete(ObusEnnemi[0])
                feuEnnemi=0
                feu=1

                # Diminution du capital de vies
                # du joueur
                
                ViesJoueur=ViesJoueur-1
                ArretAnimation=1
                Mort=1

                # On affiche les vies restantes du joueur

                if ViesJoueur>=0:
                    AffichageVie.configure(text="Lives : "+str(ViesJoueur),font=('Fixedsys',16))

                # Si le nombre de vie est non nul
                # le joueur ressucite cela va de soi !
                
                if ViesJoueur>0:
                    fen.after(500,Ressurection_joueur)
                else:

                    # On efface l'�cran
                    
                    can.delete(ALL)
                    image()
                    can.create_text(320,240,font=('Fixedsys',18),text="Game Over !!",fill='red')
                    feu=0
                    ArretAnimation=0
                    can.delete(canon[0])
                    can.delete(canon[1])
                    DebutJeu=0

                    # On v�rifie le score
                    
                    SaveMeilleurScore(Score)
                    
                    xc1,yc1=0,0
                    xc2,yc2=0,0

                    # Suspension des animations
                    
                    flag=0
            if len(ObusEnnemi)==1:
                can.coords(ObusEnnemi[0],Xobus,Yobus,Xobus+2,Yobus+40)
            fen.after(50,AnimationObusEnnemi)

# Cette fonction va permettre d'afficher un
# paysage post-apocalyptique si le joueur
# fait un game over !! :( :(

def image():
    global photo
    base_path = os.path.dirname(os.path.abspath(__file__))
    photo=PhotoImage(file=os.path.join(base_path, 'apocalypse.gif'))
    can.create_image(320,240,image=photo)
    

# Cette fonction permet de ressuciter
# le d�funt joueur \o/ Amen !! XD

def Ressurection_joueur():
    global canon,xc1,xc2,yc1,yc2,feu,flag,ArretAnimation,projectile,Mort
    if flag!=0:
        if len(projectile)!=0:
            can.delete(projectile[0])
        Mort=0
        ArretAnimation=0
        xc1=20
        yc1=440
        can.delete(canon[0])
        can.delete(canon[1])
        canon=[]
        canon.append(can.create_rectangle(xc1,yc1,xc1+20,yc1+20,fill='green'))
        xc2=xc1-20
        yc2=yc1+20
        canon.append(can.create_rectangle(xc2,yc2,xc2+60,yc2+20,fill='green'))
        feu=0
    

    
# Cette fonction va permettre de g�rer le tir du canon
# ainsi que les collisions avec les cibles situ�es en
# haut du canevas :)

def tir_joueur(event):
    global xc2,yc2,xtir,ytir,projectile,feu,VieEnnemi,flag,DebutJeu
    if DebutJeu!=0:
        if flag!=0:
            if feu!=1 :
                feu=1
                xtir=xc2+20
                ytir=yc2-40
                projectile=[(can.create_oval(xtir,ytir,xtir+20,ytir+20,fill='yellow'))]
                time.sleep(0.09)

                # On lance l'animation de l'obus
                # tir� par le joueur
                
                AnimationObus()

# Cette fonction va g�rer l'int�raction d'un obus avec une
# brique composant l'un des abris ainsi si le joueur tire sur
# l'un des abris qui lui sont offerts ceux-ci se d�sagr�geront
# sous l'effet de ses tirs maladroits :p

def abri():
    global CoordonneesBriques,ListeAbris,xtir,ytir,feu,Xobus,Yobus,feuEnnemi,CoordEnnemis,ObusEnnemi,projectile
    i=0
    t=0
    while i<len(CoordonneesBriques): 
        x=CoordonneesBriques[i][t]
        y=CoordonneesBriques[i][t+1]

        # Si le joueur tire sur l'une des briques
        # composant les abris celle-ci est d�truite
        
        if xtir==x and ytir==y :
            can.delete(ListeAbris[i])
            can.delete(projectile[0])
            feu=0
            del CoordonneesBriques[i]
            del ListeAbris[i]
        t=0
        i+=1
    i=0
    t=0
    if feuEnnemi==1:
        while i<len(CoordonneesBriques): 
            x=CoordonneesBriques[i][t]
            y=CoordonneesBriques[i][t+1]

            # Si l'ennemi tire sur l'une des briques
            # composant les abris celle-ci est
            # �galement d�truite
            
            if Xobus>=x and Xobus<=x+20 and Yobus>=y:
                can.delete(ListeAbris[i])
                if len(ObusEnnemi)==1:
                    can.delete(ObusEnnemi[0])
                ObusEnnemi=[]
                feuEnnemi=0
                del CoordonneesBriques[i]
                del ListeAbris[i]
            t=0
            i+=1 

# Cette fonction va permettre d'animer l'obus tir� par
# le canon mobile

def AnimationObus():
    global projectile,xtir,ytir,dxobus,feu,ycible,xcible,xe,ye,xe2,ye2,xe3,ye3,PasAvancement,dx,ListeAbris,BonusActif
    global VieEnnemi,feuEnnemi,NbreEnnemis,ListeCoordEnnemis,Score,NbreEnnemis,ListeEnnemis,flag,LimiteAvancement
    global xeb,yeb,EnnemiBonus,ArretAnimation

    if flag!=0 and len(projectile)==1 and ArretAnimation!=1:
        if feu==1:
            ytir=ytir-dyobus
            abri()
            if ytir<=20:
                feu=0
                can.delete(projectile[0])

            # Le bloc d'instructions qui suit permet de g�rer l'int�raction entre
            # un tir d'obus provoqu� par le joueur et un ennemi, donc si l'obus
            # touche un ennemi il est logique de dire que celui-ci est d�truit
            
            i=0
            t=0

            while i<len(ListeCoordEnnemis):

                # Pour qu'il n'y ai pas d'erreur au cas o�
                # La liste des coordonn�es des ennemis est vide
                # on execute le bloc d'instructions suivant
                # uniquement quand la liste des coordonn�es n'est
                # pas vide
                
                if len(ListeCoordEnnemis)>=1:
                    if len(ListeCoordEnnemis[i])>=1:
                        while t<len(ListeCoordEnnemis[i]):
                            if xtir+5>=ListeCoordEnnemis[i][t][0] and xtir-5<=ListeCoordEnnemis[i][t][0]+60 :
                                if ytir<=ListeCoordEnnemis[i][t][1]+5 and ytir>=ListeCoordEnnemis[i][t][1]-60 :
                                    Score=Score+50
                                    feu=0
                                    AffichageScore.configure(text="Score : "+str(Score),font=('Fixedsys',16))
                                    can.delete(projectile[0])
                                    score(50,ListeCoordEnnemis[i][t][0],ListeCoordEnnemis[i][t][1],30,20)
                                    if i==0:
                                        NbreEnnemis[0]=NbreEnnemis[0]-1
                                        can.delete(ListeEnnemis[i][t][0])
                                        can.delete(ListeEnnemis[i][t][1])
                                        can.delete(ListeEnnemis[i][t][2])
                                        del ListeEnnemis[i][t]
                                        del ListeCoordEnnemis[i][t]
                                    elif i==1:
                                        NbreEnnemis[1]=NbreEnnemis[1]-1
                                        can.delete(ListeEnnemis[i][t][0])
                                        can.delete(ListeEnnemis[i][t][1])
                                        can.delete(ListeEnnemis[i][t][2])
                                        del ListeEnnemis[i][t]
                                        del ListeCoordEnnemis[i][t]
                                    elif i==2:
                                        NbreEnnemis[2]=NbreEnnemis[2]-1
                                        can.delete(ListeEnnemis[i][t][0])
                                        can.delete(ListeEnnemis[i][t][1])
                                        del ListeEnnemis[i][t]
                                        del ListeCoordEnnemis[i][t]

                            t+=1
                    t=0
                    i+=1

            # Quand il n'y a plus d'ennemis ben on recommence
            # le carnage mais cette fois en rendant la bataille
            # plus �pic�e !! T_T
            
            if NbreEnnemis[0]+NbreEnnemis[1]+NbreEnnemis[2]==0:

                # On efface le canon mobile pour le recr�er

                can.delete(canon[0])
                can.delete(canon[1])

                Creation_CanonMobile()

                # On reprend tous les param�tres de d�part
                # afin qu'il n'y ai aucune erreur

                xe,ye=20,20
                xe2,ye2=20,80
                xe3,ye3=20,160

                # On efface l'ennemi bonus

                if len(EnnemiBonus)!=0:
                    can.delete(EnnemiBonus[0])
                    can.delete(EnnemiBonus[1])
                    can.delete(EnnemiBonus[2])
                    can.delete(EnnemiBonus[3])

                xeb,yeb=0,0

                # Avant de passer au niveau suivant
                # il faut effacer les briques restantes
                # � l'�cran
                
                if len(ListeAbris)!=0:
                    i=0
                    while i<len(ListeAbris):
                        can.delete(ListeAbris[i])
                        i+=1

                # On recr�e les abris du joueur

                Creation_Abris()
                
                LimiteAvancement+=1
                if len(ObusEnnemi)==1:
                    can.delete(ObusEnnemi[0])
                if dx<0:
                    dx=-dx

                # On accel�re la cadence des ennemis !!
                # Caramba !! XD
                    
                dx=dx+1
                
                flag=0

                # Le joueur et les ennemis pourront
                # � nouveau tirer !!
                
                feu=0
                feuEnnemi=0

                BonusActif=0
                
                Ennemis1=[]
                Ennemis2=[]
                Ennemis3=[]
                ListeEnnemis=[Ennemis1,Ennemis2,Ennemis3]
                
                Ennemis=[]
                
                CoordEnnemis1=[]
                CoordEnnemis2=[]
                CoordEnnemis3=[]
                
                ListeCoordEnnemis=[CoordEnnemis1,CoordEnnemis2,CoordEnnemis3]
                
                NbreEnnemis1=6
                NbreEnnemis2=6
                NbreEnnemis3=6
                PasAvancement=0
                NbreEnnemis=[NbreEnnemis1,NbreEnnemis2,NbreEnnemis3]
                
                v=0

                # Appel des fonctions de cr�ation des ennemis
                # pour recr�er un bataillon de vaisseaux hostiles
                # pr�ts � en d�coudre � nouveau avec le joueur !!
                
                while v<6:
                    Ennemi_Categorie1()
                    Ennemi_Categorie2()
                    Ennemi_Categorie3()
                    v+=1
                flag=1
            else:
                can.coords(projectile[0],xtir,ytir,xtir+20,ytir+20)
                fen.after(50,AnimationObus)
    

# Les deux fonctions ci-dessous permettent
# de diriger le canon mobile de gauche � droite

def right(event):
    global flag,DebutJeu
    if DebutJeu!=0:
        if flag!=0:
            move(20)

def left(event):
    global flag,DebutJeu
    if DebutJeu!=0:
        if flag!=0:
            move(-20)

# Cette fonction permet d'effectuer une pause en cours de partie

def pause(event):
    global flag,pause_text,feu,DebutJeu,feu,Mort,BonusActif,feuEnnemi,ArretAnimation

    # Si le jeu n'a pas commenc
    # la fonction ne dmarre pas
    # Il en est de mme si le joueur
    # est mort :p

    if DebutJeu!=0 and Mort!=1:    
        if flag==1:
            pause_text=can.create_text(320,240,font=('Fixedsys',18),text="PAUSE")
            flag=0
        elif flag==0:
            flag=1
            if pause_text is not None:
                can.delete(pause_text)
                pause_text = None
            AnimationObusEnnemi()
            if feu==1:
                ArretAnimation=0
                AnimationObus()
                
            
#######################
#                     #
# Programme principal #
#                     #
#######################

# Cr�ation de la fen�tre principale

fen=Tk()

# Titre de la fen�tre

fen.title('Space invaders')

# D�finition du canevas ( Ecran de jeu )

can=Canvas(fen,width=640,height=480,bg='black')

# D�finition des touches qui vont permettre
# de diriger le canon mobile

can.bind_all("<Right>",right)
can.bind_all("<Left>",left)
can.bind_all("<space>",tir_joueur)
can.bind_all("<p>",pause)

can.grid(row=1,column=0,columnspan=2,rowspan=3)

# Installation d'une image de fond
# pour �tre plus dans l'ambiance 8)

base_path = os.path.dirname(os.path.abspath(__file__))
photo=PhotoImage(file=os.path.join(base_path, 'earth.gif'))
can.create_image(320,240,image=photo)

# D�finition des boutons

# Ce bouton permet de commencer une nouvelle partie

Button(fen,text="New game",font=("Fixedsys"),command=new_game).grid(row=2,column=2,sticky=N,padx=5)
Button(fen,text="Quit",font=("Fixedsys"),command=fen.destroy).grid(row=3,column=2,sticky=N,padx=5)



# On cr�e les abris

ListeAbris=[]
CoordonneesBriques=[]

i=0

x=40
y=340

while i<3:
    limX=x+120
    limY=y+60
    departx=x
    while y<limY:
        while x<limX:
            ListeAbris.append(can.create_rectangle(x,y,x+20,y+20,fill='grey'))
            CoordonneesBriques.append([x,y])
            x+=20
        x=departx
        y+=20
    i+=1
    x+=220
    y-=60



# Coordonn�es du canon mobile

canon=[]

xc1=0
yc1=0
xc2=0
yc2=0

# Cr�ation des ennemis situ�s en haut du canevas

Ennemis1=[]
Ennemis2=[]
Ennemis3=[]

ListeEnnemis=[Ennemis1,Ennemis2,Ennemis3]
Ennemis=[]

# Cette liste contiendra les coordonn�es
# de position des ennemis dans le canevas

CoordEnnemis1=[]
CoordEnnemis2=[]
CoordEnnemis3=[]
ListeCoordEnnemis=[CoordEnnemis1,CoordEnnemis2,CoordEnnemis3]

NbreEnnemis1=6
NbreEnnemis2=6
NbreEnnemis3=6

NbreEnnemis=[NbreEnnemis1,NbreEnnemis2,NbreEnnemis3]

# D�finition des coordonn�es de d�part
# de chacune des rang�es d'ennemis

xe,ye=0,0
xe2,ye2=0,0
xe3,ye3=0,0

i=0
t=0

# On dessine chacune des cat�gories
# d'ennemis dans le canevas en utilisant
# les fonctions qui sont d�di�es � leur cr�ation

while i<6:
    Ennemi_Categorie1()
    Ennemi_Categorie2()
    Ennemi_Categorie3()
    i+=1

# D�termination al�atoire de l'ennemi
# qui tira en premier et ainsi de suite

RangEnnemiChoisi=randrange(0,3,1)

Ennemi1Choisi=randrange(0,NbreEnnemis[0],1)
Ennemi2Choisi=randrange(0,NbreEnnemis[1],1)
Ennemi3Choisi=randrange(0,NbreEnnemis[2],1)

EnnemiChoisi=[Ennemi1Choisi,Ennemi2Choisi,Ennemi3Choisi]

# D�finition de l'ennemi bonus

EnnemiBonus=[]
CoordEnnemiBonus=[]

# Coordonn�es de l'ennemi bonus

xeb=-20
yeb=80

# Indicateur renseignant sur l'activation
# et le passage de l'ennemi bonus dans le canevas

BonusActif=0

# Pas d'avancement de l'ennemi bonus

dxeb=1

# D�finition des coordonn�es d'un obus

xtir=xc2
ytir=yc2-20

ObusEnnemi=[]

feu=0
feuEnnemi=0
VieEnnemi=1

dyobus=20
dyobusEnnemi=10
dx=0

ChoixTireur=[]
ChoixTireur.append([ListeCoordEnnemis[0][randrange(0,NbreEnnemis[0],1)][0],ListeCoordEnnemis[0][randrange(0,NbreEnnemis[0],1)][1]])

Xobus=ChoixTireur[0][0]+9
Yobus=ChoixTireur[0][1]+40

# Le compteur de score

Score=0

# Le nombre de vies du joueur avant de morfler d�finitivement XD

ViesJoueur=3

# Cette variable va nous permettre d'ajuster
# le pas d'avancement des ennemis en fonction
# de leur vitesse afin qu'il n'y ai pas d'erreurs

LimiteAvancement=0
projectile=[]
PasAvancement=0
flag=0

# On affiche les indications concernant
# le score et les vies restantes du joueur

AffichageScore=Label(fen,font=('Fixedsys',16))
AffichageVie=Label(fen,font=('Fixedsys',16))
AffichageScore.grid(row=0,column=0,sticky=W)
AffichageVie.grid(row=0,column=1,sticky=E)

# Cette variable va permettre de suspendre certaines
# fonctions durant l'affichage de l'�cran de pr�sentation

DebutJeu=0

# Cette variable indique
# si le joueur est mort ==> Canon mobile d�truit
# de plus si cette variable vaut 1 certaines fonctions
# seront par cons�quent d�sactiv�es

Mort=0

ArretAnimation=0

pause_text = None  # Initialisation de pause_text pour éviter les erreurs

# Si le fichier contenant les scores n'existe pas
# on le cr�e avec comme valeur de d�part ==> 0

if existe('HighScore')==0: 
    FichierScore=open('HighScore','wb')
    pickle.dump(0,FichierScore)
    FichierScore.close()

# Cette liste va permettre d'afficher
# les scores suite � la destruction d'un ennemi

afficherScore=[]

# On d�marre la danse en mettant les ennemis en sc�ne !!

ennemis()

AnimationEnnemiBonus()

# On affiche l'�cran de pr�sentation du jeu

EcranDePresentation()

# On met le gestionnaire d'�v�nements en route

fen.mainloop()

