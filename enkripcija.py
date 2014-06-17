import string
import math
import binascii
import random

def WatsonCrick(DNArijec):
	DNArijec2=""
	for i in range(len(DNArijec)):
		if (DNArijec[i]=='A'): DNArijec2+='T'
		if (DNArijec[i]=='T'): DNArijec2+='A'
		if (DNArijec[i]=='G'): DNArijec2+='C'
		if (DNArijec[i]=='C'): DNArijec2+='G'
	return DNArijec2

rijec="DNA"
sifrat=[]
lista=['A','C','G','T']
rijec=list(rijec)
rijecBin=""
m=0
for i in range(len(rijec)):
	rijec[i]=bin(ord(rijec[i]))
	rijec[i]=rijec[i][2:len(rijec[i])]
	if (len(rijec[i])<7) : 
		rijec[i]=''.join('0' for i in range(7-len(rijec[i])))+rijec[i]
	m+=len(rijec[i])
	rijecBin+=rijec[i]
	
kljuc=''.join(random.choice(lista) for i in range(len(rijecBin)*10))
print "Otvoreni tekst: " + rijecBin 
print "Kljuc: "
for i in range (len(kljuc)/10):
	print kljuc[i*10:(i+1)*10]
k=0
for i in range (len(rijecBin)):
	rijecS=""
	if(rijecBin[i]=="1"):
		rijecS+=WatsonCrick(kljuc[(m-i-1) * 10 : (m-i-1) * 10 + 10]) 
		rijecS+=str(k)
		k=k+1
		sifrat.append(rijecS)
print "Blokovi sifrata:"
print sifrat
"""Dekripcija podataka"""
invKljuc=""
myInd=0
bini=""
for i in range(len(kljuc)/10):
	invKljuc+=kljuc[(m-i-1)*10:(m-i-1)*10+10]
for i in range(len(sifrat)):
	p=int(sifrat[i][10:len(sifrat[i])])
	sifrat[i]=sifrat[i][0:10]
	if (i==0):myIndPrev=0;
	else: myIndPrev=myInd;
	myInd=invKljuc.find(WatsonCrick(sifrat[i]), p*10)/10
	bini=bini+''.join('0' for i in range(myInd-myIndPrev -1))+'1'
print "Dekriptirani sifrat: " + bini
print "Provjera: otvoreni tekst==sifrat: " + str(bini==rijecBin)