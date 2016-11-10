#apply = wywolanie funkcji z parametrami uzyskanymi z rozpakowania sekwencji
dziel = lambda x,y,z: (x+y)/2
print dziel(7,4,6)

xyz=(7,4,6)
print apply(dziel,xyz)

#map = wywoluje funkcje dla kazdego elemenyu sekwencji z osobna
print map(lambda x: x*x*x, range(10))
print map(dziel,range(10),range(10),[2]*10)

#zip = sluzy do konsolidacji danych wartosc pojedynczego elementu listy wynikowej zalezy od wartosci pojedynczych elementow list zrodlowych
print zip("abcdef",[1,2,3,4,5,6])
print zip(range(1,10),range(9,0,-1))
print zip ("zip",range(0,9),zip (range(0,9)))

#filter = filtruje dane
samogloska = lambda x: x.lower() in 'aeiou'
print samogloska('A')
print filter (samogloska, "ala ma kota")

#filtrowanie innych znakow
print filter(lambda x: not samogloska(x), "Ala ma kota")

#reduce = agregowanie danych, operacja policzenia pojedynczego wyrazenia zaleznie od wszystkich elementow listy zrodlowej
#suma
print reduce(lambda x,y: x+y, [1,2,3])

#suma kwadratow elementow
print reduce(lambda x,y: x+y, map(lambda x: x*x, range(1,3)))