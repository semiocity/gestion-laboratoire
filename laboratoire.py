'''Les opérations sur un laboratoire'''

class LaboException(Exception):
    """ Généralise les exceptions du laboratoire."""
    pass

class AbsentException(LaboException):
    pass

class PresentException(LaboException):
    pass

def Laboratoire ():
    return {}

def enregistrer_arrivee (labo, nom, bureau):
    '''Documentation'''
    if nom in labo:
        raise PresentExcept
    labo[nom] = bureau

def enregistrer_depart (labo, nom,):
    '''Documentation'''
    if nom not in labo:
        raise AbsentExcept
    labo.pop(nom)

def changer_bureau (labo, nom, bureau):
    labo[nom] = bureau

def changer_nom (labo, nom, nouveau_nom):
    labo[nouveau_nom] = labo.pop(nom)

def chercher_nom (labo, nom):
    if nom in labo.keys():
        print("{} travaille bien dans ce laboratoire".format(nom))
    else:
        print ("{} ne travaille pas dans ce laboratoire".format(nom))

def chercher_bureau (labo, nom):
    if nom in labo.keys():
        print("{} travaille dans le bureau {}".format(nom, labo[nom]))
    else:
        raise AbsentExcept

def affichage_bureaux (labo):
    bureaux = {}
    for bureau in set(labo.values()):
        occupants_bureau = []
        for personnel, bureau_personnel in labo.items():
            if bureau_personnel == bureau:
                occupants_bureau.append(personnel)
        bureaux[bureau] = occupants_bureau
    for bureau, personnels in bureaux.items():
        print ("{}: ".format(bureau))
        for personnel in personnels:
            print ("_ {}".format(personnel))

    input("Appyez sur \"Entrée pour revenir au menu\"")

