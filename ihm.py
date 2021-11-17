from laboratoire import *
from menu import *

def traiter (labo, menu, choix):
    if choix!=0:
        _,action = menu [choix-1]
        action (labo)

def gerer_arrivee (labo):
    nom = input("Nom : ")
    bureau = input("Bureau : ")
    enregistrer_arrivee (labo, nom, bureau)

def gerer_demenagement (labo):
    nom = input("Nom : ")
    bureau = input("Nouveau bureau : ")
    changer_bureau (labo, nom, bureau)

def gerer_depart (labo):
    nom = input("Nom : ")
    enregistrer_depart (labo, nom)

def gerer_changement_nom (labo):
    nom = input("Nom à modifier : ")
    nouveau_nom = input ("Nouveau nom : ")
    changer_nom (labo, nom, nouveau_nom)

def gerer_recherche_personne (labo):
    nom = input("Nom de la personne à chercher : ")
    chercher_nom (labo, nom)

def gerer_recherche_bureau (labo):
    nom = input("Nom de la personne dont on cherche le bureau : ")
    chercher_bureau (labo, nom)

def gerer_affichage_bureaux (labo):
    print("Juste avant appel fonction")
    affichage_bureaux (labo)


def main ():
    labo = Laboratoire() # initialisation d'un laboratoire vierge

    # construction du menu
    menu_labo = Menu()
    ajouter_menu(menu_labo, "Enregistrer arrivée", gerer_arrivee)
    ajouter_menu(menu_labo, "Enregistrer départ", gerer_depart)
    ajouter_menu(menu_labo, "Changer de bureau", gerer_demenagement)
    ajouter_menu(menu_labo, "Changer le nom d'une personne", gerer_changement_nom)
    ajouter_menu(menu_labo, "Chercher une personne", gerer_recherche_personne)
    ajouter_menu(menu_labo, "Chercher le bureau d'une personne", gerer_recherche_bureau)
    ajouter_menu(menu_labo, "Occupation des bureaux", gerer_affichage_bureaux)

    choix = None
    while choix != 0:
        afficher_menu(menu_labo)
        choix = choix_utilisateur(menu_labo)
        traiter (labo, menu_labo, choix)
        print ("Labo:", labo)

if __name__=="__main__":
    main()