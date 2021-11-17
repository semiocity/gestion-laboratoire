def Menu():
    return []

# Ajouter un texte et une action à un menu
def ajouter_menu (menu, texte, action):
    menu.append((texte, action))

def afficher_menu(menu):
    for num, (text,_) in enumerate (menu,1):
        print (f"{num:2} {text}")
    print (f"{0:2} - Quitter")

def choix_utilisateur (menu):
    return(int(input("Votre choix : ")))