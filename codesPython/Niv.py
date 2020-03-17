# -*- coding: utf-8 -*-
class Niv():
	compteur = 0
	def __init__(self, nom):
		self.nom = nom
		self.sup = None  # par défaut pas de supérieur
		self.inf = []    # par défaut liste vide de subalternes
		Niv.compteur += 1

	@staticmethod
	def nombreinstances() : return Niv.compteur

	def addNiv(self, niveau):
		niveau.sup = self
		self.inf.append(niveau)

	def organigramme(self):
		for f in self.inf:
			print self.nom, "dirige ", f.nom
			f.organigramme()
pdg = Niv("dir")
pdg.organigramme()
pdg.addNiv(Niv("export"))
pdg.addNiv(Niv("natl"))
pdg.addNiv(Niv("assist"))
print pdg.inf
pdg.organigramme()
pdg.inf[0].addNiv(Niv("Am"))
pdg.inf[0].addNiv(Niv("Asia"))
pdg.inf[0].addNiv(Niv("Eu"))
pdg.inf[0].addNiv(Niv("RoW"))
pdg.inf[2].addNiv(Niv("CustSat"))
pdg.inf[2].addNiv(Niv("Repair"))
pdg.inf[2].inf[1].addNiv(Niv("site"))
pdg.inf[2].inf[1].addNiv(Niv("remote"))
pdg.organigramme()
import gc
print pdg.nombreinstances()
print pdg.inf[1].nom
del pdg.inf[1]
print gc.collect(), "objets inatteignables"
pdg.inf[1].nom
del pdg.inf[1]
print gc.collect(), "objets inatteignables"
print gc.collect(), "objets inatteignables"
