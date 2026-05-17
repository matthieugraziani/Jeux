import io
import random
import sys

reconfigure = getattr(sys.stdout, "reconfigure", None)
if callable(reconfigure):
    reconfigure(encoding='utf-8')
else:
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', line_buffering=True)
    except Exception:
        pass

COULEURS = ['R', 'V', 'B', 'J', 'O', 'M']
NOMS_COULEURS = ['Rouge', 'Vert', 'Bleu', 'Jaune', 'Orange', 'Mauve']
EMOJIS = {'R': '🔴', 'V': '🟢', 'B': '🔵', 'J': '🟡', 'O': '🟠', 'M': '🟣'}
TAILLE = 4
ESSAIS_MAX = 10

def saisir_combinaison():
    while True:
        entree = input("Tapez 4 lettres (ex : RVBJ) : ").upper().replace(" ", "")

        if len(entree) != TAILLE:
            print(f"Il faut exactement {TAILLE} lettres. Réessayez.")
            continue

        if all(c in COULEURS for c in entree):
            return list(entree)
        else:
            print("Lettres invalides. Utilisez suelement : " + " ".join(COULEURS))


def feedback(code, essai):
    bien_places = 0
    mal_places = 0
    code_temp = code.copy()
    essai_temp = essai.copy()

    for i in range(TAILLE):
        if essai[i] == code[i]:
            bien_places += 1
            code_temp[i] = essai_temp[i] = None

    for c in essai_temp:
        if c and c in code_temp:
            mal_places += 1
            code_temp[code_temp.index(c)] = None
    
    return bien_places, mal_places


def afficher_plateau(historique):
    print("\n" + "="*40)
    print("📋 PLATEAU DE JEU")
    print("="*40)
    for i, (essai, bien, mal) in enumerate(historique, 1):
        emojis = "".join(EMOJIS[couleur] for couleur in essai)
        indices = "●" * bien + "○" * mal
        print(f"{i:2d}. {emojis} | {indices}")
    print("="*40)


def main():
    code = random.choices(COULEURS, k=TAILLE)
    historique = []

    print("Devinez la séquence de 4 couleurs")
    print("Couleurs disponibles :")
    for i, nom in enumerate(NOMS_COULEURS):
        print(f"   {COULEURS[i]} = {nom} {EMOJIS[COULEURS[i]]}")

    for tentative in range(ESSAIS_MAX):
        print(f"Il vous reste {ESSAIS_MAX - tentative} tentative(s)")
        essai = saisir_combinaison()

        bien, mal = feedback(code, essai)
        print(f"✅ Bien placés : {bien} | ⚠️ Mal placés : {mal}")
        
        historique.append((essai, bien, mal))
        afficher_plateau(historique)

        if bien == TAILLE:
            code_emojis = "".join(EMOJIS[couleur] for couleur in code)
            print(f"🎉 Bravo ! Le code secret était : {code_emojis}")
            break
    else:
        code_emojis = "".join(EMOJIS[couleur] for couleur in code)
        print(f"💥 Perdu ! Le code était : {code_emojis}")

if __name__ == "__main__":
    main()
