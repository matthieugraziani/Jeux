import random

cartes = {'As': 1, 'Deux': 2, 'Trois': 3, 'Quatre': 4, 'Cinq': 5, 'Six': 6, 'Sept': 7, 'Huit': 8, 'Neuf': 9, 'Dix': 10, 'Valet': 10, 'Dame': 10, 'Roi': 10}
jeu_de_cartes = {}

def distribuer_cartes(nombre_jeux):
    global jeu_de_cartes
    jeu_de_cartes = list(cartes.keys()) * 4 * nombre_jeux
    random.shuffle(jeu_de_cartes)
    main_joueur = [jeu_de_cartes.pop() for _ in range(2)]
    main_croupier = [jeu_de_cartes.pop() for _ in range(2)]
    return main_joueur, main_croupier

def calculer_score(main):
    score = 0
    as_present = False
    for carte in main:
        score += cartes[carte]
        if carte == 'As':
            as_present = True
    if as_present and score <= 11:
        score += 10
    return score

def demander_decision():
    choix = input("Voulez-vous tirer une autre carte (o/n) ?")
    return choix.lower() == 'o'

def tirer_carte():
    carte = jeu_de_cartes.pop(0)
    return carte

def jouer_main_joueur(main_joueur):
    while True:
        score_joueur = calculer_score(main_joueur)
        print("Votre main: ", main_joueur)
        print("Votre score: ", score_joueur)
        if score_joueur == 21:
            print("Blackjack ! vous avez gagné !")
            break
        elif score_joueur > 21:
            print("Vous avez dépassé 21. Vous avez perdu.")
            break
        choix = demander_decision()
        if choix:
            main_joueur.append(tirer_carte())
        else:
            break

def jouer_main_croupier(main_croupier):
    while True:
        score_croupier = calculer_score(main_croupier)
        if score_croupier >= 17:
            break
        else:
            main_croupier.append(tirer_carte())

def afficher_resultats(main_joueur, main_croupier):
    score_joueur = calculer_score(main_joueur)
    score_croupier = calculer_score(main_croupier)
    print("Votre main: ", main_joueur)
    print("Votre score: ", score_joueur)
    print("Croupier main: ", main_croupier)
    print("Croupier score: ", score_croupier)
    if score_joueur > 21:
        print("Vous avez dépassé 21. Vous avez perdu.")
    elif score_croupier > 21:
        print("Le croupier a dépassé 21")
    elif score_joueur == score_croupier:
        print("Egalité")
    elif score_joueur == 21:
        print("Blackjack ! vous avez gagné !")
    elif score_joueur > score_croupier:
        print("vous avez gagné !")
    else:
        print("Le croupier a gagné !")



def jouer_black_jack():
    print('Bienvenue au jeu de blackjack !')

    nombre_jeux = 2
    main_joueur, main_croupier = distribuer_cartes(nombre_jeux)

    jouer_main_joueur(main_joueur)
    if calculer_score(main_joueur) <= 21:
        jouer_main_croupier(main_croupier)
        afficher_resultats(main_joueur, main_croupier)

jouer_black_jack()