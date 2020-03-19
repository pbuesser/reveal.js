# -*- coding: utf-8 -*-
#fonctions de service definie au debut du module
def erreur(message):
	print "Erreur: " + message
	from sys import exit
	exit()
	
def pgcd(a, b):
	#pas besoin de tester b==a ici
	#ce sera fait avec b % a == 0 ou a % b == 0
	if b > a:
		if b % a == 0:
			return a
		else:
			return pgcd(b % a, a)
	else:
		if a % b == 0:
			return b
		else:
			return pgcd(b, a % b)
#classes:-----------------------------------------------------------
class Fraction():

	def __init__(self, num, den):
		self.num = num
		if(den ==0):
			erreur("Denominateur nul")
		self.den = den
	def __str__(self):
		return str(self.num)+"/"+str(self.den)
	def plus(self,f):
		resultat = Fraction(self.num*f.den+ f.num*self.den,self.den*f.den)
		return resultat.simplifier()
	def __add__(self,f):
		resultat = Fraction(self.num*f.den+ f.num*self.den,self.den*f.den)
		return resultat.simplifier()
	def moins(self, f):
		resultat = Fraction(self.num * f.den - self.den * f.num, self.den * f.den)
		if (resultat.num < 0):
		# changer de signe avant de simplifier
			resultat.num = - resultat.num
			resultat = resultat.simplifier()
			resultat.num = - resultat.num
			return resultat
		else: 
			return resultat.simplifier()
	def simplifier(self):
		p = pgcd(self.num,self.den)
		self.den = self.den/p
		self.num = self.num/p
		return self
	def fois(self, f):
		resultat = Fraction(self.num * f.num, self.den * f.den)
		return resultat.simplifier()
	def div(self, f):
		resultat = Fraction(self.num * f.den, self.den * f.num)
		return resultat.simplifier()
#utilisation:------------------------------------------------------------		
f1 = Fraction(2,4)
print f1
f1.simplifier()
print f1
f2 = Fraction(7,8)
print f1.plus(f2)
print f1 + f2
