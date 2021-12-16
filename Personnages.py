import sys

from Capacites import Soin, Attaque, VolVie

class Personnage:

    def __init__(self, nom = "", pv = 100, mana = 20):
        self.nom = nom
        self.pv = pv
        self.mana = mana
        self.regenMana = 15

    def Presentation(self):
        return self.nom

    def PrendreAttaque(self, attaque):
        self.pv -= attaque.degats
        print(self.nom, "perds", attaque.degats, "PVs")

    def Attaquer(self, attaque, ennemi):
        attaque.Utiliser(self, ennemi)
        self.mana -= attaque.mana

    def RegenMana(self):
        self.mana += self.regenMana

class Mage(Personnage):
    def __init__(self):
        # La ligne ci-dessous sers à faire référence au __init__ de Personnage.
        # C'est ce __init__ qui crée le nom, les pv et le mana des personnages.
        super().__init__("Gandalf", 80, 150)
        self.regenMana = 20
        self.attaques = [
            Soin("Incantation Lunaire", 20, 40),
            Attaque("Bâton des arcanes", 15, 30, 1.5, 0.3),
            Attaque("Incantation des démons", 30, 20, 2, 0.6),
            VolVie("Vampirisme", 20, 0.5, 30, 1.8, 0.5)
        ]

    def Defaite(self):
        return "Je dois revoir mes incantations. La prochaine fois sera différente !"

    def Victoire(self):
        return "De bonnes incantations, du talent et la magie fait le reste"

    def Presentation(self):
        return "mage %s" % (self.nom)

class Guerrier(Personnage):
    def __init__(self):
        super().__init__("Guerrier", 300, 100)
        self.attaques = [
            Soin("Tournée générale", 20, 30),
            Attaque("Giga massue", 20, 10, 1.4, 0.5),
            Attaque("Danse des lames", 30, 30, 2, 0.2),
            Attaque("Duel", 50, 50, 2.5, 0.1),
        ]

    def Defaite(self):
        return "MES MUSCLES .... N'ETAIENT ..... PAS ..... ASSEZ FORTS !"

    def Victoire(self):
        return "PAS BESOIN D'UN GROS CERVEAU. DES MUSCLES SUFFISENT !"

class Pretre(Personnage):
    def __init__(self):
        super().__init__("Prêtre", 75, 200)
        self.attaques = [
            Soin("Prêche", 20, 10),
            Attaque("Intervention Divine", 40, 50, 1.5, 0.3),
            Attaque("Invocation Demoniaque", 30, 40, 1.5, 0.4),
            Attaque("Bâton des arcanes", 15, 30, 3, 0.3),
        ]

    def Defaite(self):
        return "Les divins s'occuperont de votre cas"

    def Victoire(self):
        return "Que vos ames soient épargnées"
