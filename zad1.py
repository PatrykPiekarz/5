'''
napisz skrypt wykonujacy nastepujace czynnosci: (uniwersalne metody)
a) utworz liste o rozmiarach podanych przez uzytkownika
b) uzupelnij liste losowymi wartosciami z zakresu podanego przez uzytkownika
c wyswietl liste
d)wyszyka wielokrotnosci liczby 2,3,5 i zapisze kazda nowych list (osobno dla 2,3,5)
e)wyszuka duplikat z kazdej listy i utworzy z nich nowa liste
f)zastapi duplikaty w oryginalnej liscie znakiem 'X'
g)usunie duplikaty z listy a)
h)obliczy wartosc srednia i podniesie kazda wartosc do potegi 3
i)zastapi wielokrotnosc liczby 2 litera A, 3 litera E, 5 litera L
j)wyszuka liczby pierwsze i zastapi je litera Z
k)wyszuka litery w liscie i utworzy z nich losowe napisy
'''

import random

def dupes(lst1,lst2):
    for i in lst1:
        if (lst1.count(i)>1):
            lst2.append(i)

n=raw_input("n:")
n=int(n)
m=raw_input("m:")
m=int(m)
lsta = []
for i in range (0,n):
    lsta.append(random.randint(0,m))
print lsta
lstb=[x for x in lsta if x%2==0]
lstc=[x for x in lsta if x%3==0]
lstd=[x for x in lsta if x%5==0]
print lstb
print lstc
print lstd
lste=[]
print "lsita a:"
dupes(lsta,lste)
print "lsita |2:"
dupes(lstb,lste)
print "lsita |3:"
dupes(lstc,lste)
print "lsita |5:"
dupes(lstd,lste)
print "duplikaty:"
print lste
j=0
for i in lsta:
    if lsta.count(i)>1:
        lsta[j]='X'
        j=j+1
print "lsita a po zmianie duplikatow na X:"
print lsta
lstpom = []
for i in lsta:
    if i!='X':
        lstpom.append(i)
lsta=lstpom
print "lsita a po usunieciu duplikatow:"
print lsta
srednia=0.0
for i in lsta:
    srednia+=i
print "srednia:"
print srednia/lsta.__len__()
for i in lsta:
    i=i*i*i
for i in range(0,lsta.__len__()):
    if lsta[i]%2==0:
        lsta[i]='A'
    if lsta[i]%3==0:
        lsta[i]='E'
    if lsta[i]%5==0:
        lsta[i]='L'

print "lsita a po zmianie liczb podzielnych przez 2,3,5 na A,E,L:"
print lsta

class sito:

    boles=[]
    n=0

    def __init__(self,n):
        self.n=n
        i=1
        while i != self.n+1:
            self.boles.append(i)
            i+=1
        return

    def sito(self):
        m=self.n**0.5
        boles=self.boles
        i=1
        while i < m:
            for j in boles:
                if (not (j % i) and not (i == j)) and i != 1:
                    boles.remove(j)
            j = boles.index(i) + 1
            i = boles[j]
        return

x = sito(n)
x.sito()
x.boles.remove(1)


for i in range(0,lsta.__len__()):
    if x.boles.count(lsta[i])>0:
        lsta[i]='Z'


print "lsita a po zmianie liczb pierwszych na Z:"
print lsta

