import sys
import random

# Dans ce fichier tu as pleins de lignes avec des '#'.
# Ce sont des commentaires. Ils ne sont là que pour
# donners des infos sur le code et ce qu'il fait.
# Ces lignes sont totallement ignorées par python

class Capacite:

    def __init__(self, nom, mana = 5, tauxCrit = 1, probaCrit = 0):
        self.nom = nom
        self.mana = mana
        # Taux du coup critique. Un nombre a virgule
        # Si plus grand que 1 augmente les soins / dégâts sinon les réduits
        self.tauxCrit = tauxCrit
        # Probabilité de coup critiques entre 0 et 1
        self.probaCrit = probaCrit

    def Utiliser(self, invocateur, ennemi):
        print("Cette capacité n'est ni un soin ni une attaque. Sans effets")

class Soin(Capacite):

    def __init__(self, nom = "Soin", soin = 10, mana = 5, tauxCrit = 1, probaCrit = 0.5):
        super().__init__(nom, mana, tauxCrit, probaCrit)
        self.soin = soin

    def Utiliser(self, invocateur, ennemi):
        pvASoigner = self.soin
        tirage = random.random()
        # Si le nombre tiré est entre 0 et probaCrit alors ce coup est critique
        if tirage <= self.probaCrit:
            pvASoigner *= self.tauxCrit

        invocateur.pv += pvASoigner

        print("%s utilise %s. Il récupère %d PVs" % (invocateur.nom, self.nom, pvASoigner))

    def Description(self):
        return "%s: %d Soin | %d Mana | %d%% chances de Crit | %d%% taux de crit" % (self.nom, self.soin, self.mana, self.probaCrit * 100, self.tauxCrit * 100)

class Attaque(Capacite):

    def __init__(self, nom = "Attaque", degats = 10, mana = 5, tauxCrit = 1, probaCrit = 0.5):
        super().__init__(nom, mana, tauxCrit, probaCrit)
        self.degats = degats

    def Utiliser(self, invocateur, ennemi):
        pvARetirer = self.degats
        tirage = random.random()
        # Si le nombre tiré est entre 0 et probaCrit alors ce coup est critique
        if tirage <= self.probaCrit:
            pvARetirer *= self.tauxCrit
            print("COUP CRITIQUE !")

        ennemi.pv -= pvARetirer

        print("%s utilise %s. %s perds %d PVs" % (invocateur.nom, self.nom, ennemi.nom, pvARetirer))

    def Description(self):
        return "%s: %d Degats | %d Mana | %d%% chances de Crit | %d%% taux de crit" % (self.nom, self.degats, self.mana, self.probaCrit * 100, self.tauxCrit * 100)

class VolVie(Capacite):

    def __init__(self, nom = "Vol de vie", degats = 10, volVie = 0.7, mana = 5, tauxCrit = 1, probaCrit = 0.5):
        super().__init__(nom, mana, tauxCrit, probaCrit)
        self.degats = degats
        # VolVie est une valeur entre 0 et 1.
        # Elle détermine quel pourcentage de degats sont convertis en soin
        # La valeur de soin est déterminée en faisant degats * volvie
        self.volVie = volVie

    def Utiliser(self, invocateur, ennemi):
        pvARetirer = self.degats
        tirage = random.random()
        # Si le nombre tiré est entre 0 et probaCrit alors ce coup est critique
        if tirage <= self.probaCrit:
            pvARetirer *= self.tauxCrit
            print("COUP CRITIQUE !")
        soin = pvARetirer * self.volVie

        ennemi.pv -= pvARetirer
        invocateur.pv += soin

        print("%s utilise %s. %s perds %d PVs" % (invocateur.nom, self.nom, ennemi.nom, pvARetirer))
        print("%s récupère %d PVs" % (invocateur.nom, soin))

    def Description(self):
        return "%s: %d Degats | %d Mana | %d%% chances de Crit | %d%% taux de crit. Effet special : %d%% taux vol vie" % (self.nom, self.degats, self.mana, self.probaCrit * 100, self.tauxCrit * 100, self.volVie * 100)
