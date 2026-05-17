import tkinter
import random
gameOver = False
score = 0
carrésAVérifier = 0

def jouer_démineur():
    créer_terrainMiné(terrainMiné)
    fenêtre = tkinter.Tk()
    configuration_fenêtre(fenêtre)
    fenêtre.mainloop()
    
terrainMiné = []

def créer_terrainMiné(terrainMiné):
    global carrésAVérifier
    for rangée in range(0,10):
        listeRangée = []
        for colonne in range(0,10):
            if random.randint(1,100) < 20:
                listeRangée.append(1)
            else:
                listeRangée.append(0)
                carrésAVérifier = carrésAVérifier + 1
        terrainMiné.append(listeRangée)
    #printTerrain(terrainMiné)
    
def printTerrain(terrainMiné):
    for listeRangée in terrainMiné:
        print(listeRangée)
        
def configuration_fenêtre(fenêtre):
    for numéroRangée, listeRangée in enumerate(terrainMiné):
        for numéroColonne, entréeColonne in enumerate(listeRangée):
            if random.randint(1,100) < 25:
                carré = tkinter.Label(fenêtre, text = "    ", bg = "darkgreen")
            elif random.randint(1,100) < 75:
                carré = tkinter.Label(fenêtre, text = "    ", bg = "seagreen")
            else:
                carré = tkinter.Label(fenêtre, text = "    ", bg = "green")
            carré.grid(row = numéroRangée, column = numéroColonne)
            carré.bind("<Button-1>", quand_cliqué)
def quand_cliqué(event):
    global score
    global gameOver
    global carrésAVérifier

    carré = event.widget
    rangée = int(carré.grid_info()["row"])
    colonne = int(carré.grid_info()["column"])
    texteActuel = carré.cget("text")
    if gameOver == False:
        if terrainMiné[rangée][colonne] == 1:
            gameOver = True
            carré.config(bg = "red")
            print("GAME OVER ! Tu as touché une bombe !")
            print("Ton score :", score)
        elif texteActuel == "    ":
            carré.config(bg = "brown")
            totalBombes = 0

            if rangée < 9:
                if terrainMiné[rangée+1][colonne] == 1:
                    totalBombes = totalBombes + 1

            if rangée > 0:
                if terrainMiné[rangée-1][colonne] == 1:
                    totalBombes = totalBombes + 1

            if colonne > 0:
                if terrainMiné[rangée][colonne-1] == 1:
                    totalBombes = totalBombes + 1

            if colonne < 9:
                if terrainMiné[rangée][colonne+1] == 1:
                    totalBombes = totalBombes + 1

            if rangée > 0 and colonne > 0:
                if terrainMiné[rangée-1][colonne-1] == 1:
                    totalBombes = totalBombes + 1

            if rangée < 9 and colonne > 0:
                if terrainMiné[rangée+1][colonne-1] == 1:
                    totalBombes = totalBombes + 1

            if rangée > 0 and colonne < 9:
                if terrainMiné[rangée-1][colonne+1] == 1:
                    totalBombes = totalBombes + 1

            if rangée < 9 and colonne < 9:
                if terrainMiné[rangée+1][colonne+1] == 1:
                    totalBombes = totalBombes + 1

            carré.config(text = " " + str(totalBombes) + " ")

            carrésAVérifier = carrésAVérifier - 1

            score = score + 1

            if carrésAVérifier == 0:
                gameOver = True
                print("Bravo, tu as trouvé tous les carrés non minés.")
                print("Ton score :", score)

jouer_démineur()