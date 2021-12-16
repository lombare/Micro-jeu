import sys

from Personnages import Mage, Guerrier, Pretre

def question(q):
    print(q)
    retour = sys.stdin.readline()[:-1]
    while retour == "":
        retour = sys.stdin.readline()[:-1]
    return retour

class Joueur():
    def __init__(self):
        self.nom = question("Joueur quel est ton nom ?")

        availableClass = [Mage, Guerrier, Pretre]
        i = 0;
        print("Classes disponibles :")
        for a in availableClass:
            print(i, ":", a.__name__)
            i += 1
        a = question("Quelle classe choisissez vous ?")
        if int(a) >= 0 and int(a) < len(availableClass):
            self.personnage = availableClass[int(a)]()


    def Presentation(self):
        print("Je suis", self.nom, "le", self.personnage.Presentation())

    def Attaquer(self, adversaire):
        print("C'est au tour de %s d'attaquer. %d PVs, %d Mana" % (self.nom, self.personnage.pv, self.personnage.mana))
        print("Choisissez votre coup :")
        i = 0
        for attaque in self.personnage.attaques:
            print("%d: %s" % (i, attaque.Description()))
            i += 1

        while True:
            choix = question("Choisissez une attaque :")
            choix = int(choix)
            # Si le choix est une attaque valide (plus ou égale à 0 ou moins du nombre d'attaques disponibles)
            if choix >= 0 and choix < len(self.personnage.attaques):
                attaqueChoisie = self.personnage.attaques[choix]
                if self.personnage.mana < attaqueChoisie.mana:
                    print("Pas assez de mana pour invoquer %s" % (attaqueChoisie.nom))
                    continue
                self.personnage.Attaquer(attaqueChoisie, adversaire.personnage)
                break

    def EstKO(self):
        # Si le personnage a plus de 0 PV alors il n'est pas KO
        if self.personnage.pv > 0:
            return False
        else:
            return True

    def FinTour(self):
        self.personnage.RegenMana()

    def Defaite(self):
        print("%s a été vaincu : %s" % (self.nom, self.personnage.Defaite()))

    def Victoire(self):
        print("%s est victorieux : %s" % (self.nom, self.personnage.Victoire()))
