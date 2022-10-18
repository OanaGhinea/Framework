# Declara o lista note_muzicale in care sa pui do re mi etc pana la do
# Afiseaz-o
# Inverseaza ordinea folosind slicing si suprascrie aceasta lista
# Printeaza varianta actuala (inversata)
# Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea. (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)
# Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala
#
# Concluzii: slicing e temporar, daca vrei sa pastrezi noua varianta va trebuie sa suprascrii lista sau sa o salvezi intr-o lista noua. Metoda gasita de tine, face suprascrierea automat si permanentizeaza aceste modificari. Ambele variante isi gasesc utilitatea in functie de ce ne dorim in acel moment.

note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(note_muzicale)
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
print(list(reversed(note_muzicale))


# De cate ori apare ‘do’?

print(note_muzicale.count('do'))

# Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
# Gasiti 2 variante sa le uniti intr-o singura lista.
l1 = [3, 1, 0, 2]
l2 = [6, 5, 4]
l1 = [3, 1, 0, 2]
l2 = [6, 5, 4]
print(l1+l2)
l1.extend(l2)
print(l1)

# Sortati si afisati lista generata la ex anterior
# Stergeti numarul 0 folosind o functie
# Afisati iar lista

l = [3, 1, 0, 2, 6, 5, 4]
l.sort()
print(l)
print(sorted(l))
l.remove(0)
print(l)

# Folosind un if verificati lista generata la ex3 si afisati
# Lista este goala
# Lista nu este goala

l = [3, 1, 0, 2, 6, 5, 4]

if len(l)==0:
	print('Lista e goala')
else:
	print('Lista nu e goala')

# Folositi o functie care sa stearga lista de la ex3
l = [3, 1, 0, 2, 6, 5, 4]
del l[:]
print(l)

# Copy paste la ex 5. Verificati inca o data.
# Acum ar trebui sa se afiseze ca lista e goala
l = [3, 1, 0, 2, 6, 5, 4]
del l[:]
print(l)
if len(l)==0:
	print('Lista e goala')
else:
	print('Lista nu e goala')

raspuns:
[]
Lista e goala
# sau
l = [3, 1, 0, 2, 6, 5, 4]
print(f"Lista inainte de golire: {l}")
l.clear()
print(f"Lista dupa golire: {l}")

# Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folositi o functie ca sa afisati Elevii (cheile)

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())

# Printati cei 3 elevi si notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o veti lua folosindu-va de cheie

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
for elev, nota in dict1.items():
	print(f'\n{elev.title()} a luat nota {nota}')

# sau
student = input("Introduceti numele elevului pentru care vreti nota: ")
print(f"{student} a luat nota {dict1[student]}")

# Dorel a facut contestatie si a primit 6
# Modificati nota lui Dorel in 6
# Printati nota dupa modificare

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
dict1['Dorel']=6
print(dict1)


# Gigel se transfera din clasa
# Cautati o functie care sa il stearga
# Vine un coleg nou. Adaugati Ionica, cu nota 9
# Printati noii elevi

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
del dict1['Gigel']
dict1['Ionica']=9
print(dict1)

rasp:
{'Ana': 8, 'Gigel': 10, 'Dorel': 6}
{'Ana': 8, 'Dorel': 5, 'Ionica': 9}

# Set zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}, weekend = {'sambata', 'duminica'}.
# Adaugati in zilele_sapt ‘luni’. Afisati zile_sapt

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(zile_sapt)
Set
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
# Adaugati in zilele_sapt ‘luni’
# Afisati zile_sapt

zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(zile_sapt)

# Folositi un if si verificati daca
# Weekend este un subset al zilelor din sapt
# Weekend nu este un subset al zilelor din sapt
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
if weekend.issubset(zile_sapt):
	print('Weekend este un subset al zilelor din sapt')
else:
	print('Weekend nu este un subset al zilelor din sapt')

# Afisati diferentele dintre aceste 2 seturi

print(zile_sapt.difference(weekend))

# Afisati intersectia elementelor din aceste 2 seturi

print(weekend.intersection(zile_sapt))
print(zile_sapt.intersection(weekend))

c. Optionale (may need google)

16.
Ne imaginam o echipa de fotbal pt teren sintetic.
3 Schimbari maxime admise

Declara o Lista cu 5 jucatori
Schimbari_efectuate = va jucati voi cu valori diferite
Schimbari_max = 3

Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
Efectuam schimbarea 
Stergem jucatorul scos din lista
Adaugam jucatorul intrat
Afisam a intra x, a iesit y, mai aveti z schimbari
Daca jucatorul nu e in teren:
Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
Afisati ‘mai aveti z schimbari’

Testati codul cu diferite valori

Google search hint
“how to check if item is in list python”

jucatori = ["Andi", "Bodo", "Jorge", "Michael", "Abdel"]
substituire = ["Sam", "Benjamin", "Dan", "Costa", "Micu"]
substituire_max = 3

substituire_facuta = int(input("Introduceti cate schimbari au fost efectuate pana acum dintr-un maxim de 3: "))
jucator_de_schimbat = input(f"Introduceti numele unui jucator pe care sa il schimbati dintre {jucatori}:")
if jucator_de_schimbat in jucatori:
    if substituire_facuta < substituire_max:
       jucator_teren = substituire.pop()
       jucatori.remove(jucator_de_schimbat)
       jucatori.append(jucator_teren)
    print(f"A intrat {jucator_teren}, a iesit {jucator_de_schimbat}, mai aveti {substituire_max - substituire_facuta} schimbari")
    print(f"Mai aveti {substituire_max - substituire_facuta} schimbari ")
else:
    print(f"Nu se poate efectua schimbarea, deoarece jucatorul {jucator_de_schimbat} nu e in teren!")







