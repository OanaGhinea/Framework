
# Avand lista
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# Folositi un for ca sa iterati prin toata lista si sa afisati
# ‘Masina mea preferata este x’
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes' 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for fav_mas in masini:
     print(f'Masina preferata este {fav_mas}')

# Faceti acelasi lucru cu un for each ?
for idx in range(len(masini)):
    print(f"Masina mea preferata este {masini[idx]}")
# Faceti acelasi lucru cu un while
idx = 0
while idx < len(masini):
    print(f"Masina mea preferata este {masini[idx]}")
    idx += 1

# Aceeasi lista.Folosit un for in for.
# Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul (v1 - caracter, v2 - element)
# Printati varianta finala a listei.
# Incercati sa rezolvati atat v1 => output: ['aUDi', 'vOLVo', 'bMw', 'mERCEDEs', 'aSTON MARTIn', 'lASTUn', 'fIAt', 'tRABANt', 'oPEl']
# Cat si v2 => output: ['audi', 'VOLVO', 'BMW', 'MERCEDES', 'ASTON MARTIN', 'LASTUN', 'FIAT', 'TRABANT', 'opel']

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for brand in masini:
    print(brand[0].lower()+brand[1:-1].upper()+brand[-1].lower())

 # v1 - 1 for and building a new list, not modifing the initial one
masini_final = []
for masina in masini:
    masina_modif = masina[0].lower() + masina[1:-1].upper() + masina[-1]
    masini_final.append(masina_modif)
print(masini_final)

# v2 => ['audi', 'VOLVO', 'BMW', 'MERCEDES', 'ASTON MARTIN', 'LASTUN', 'FIAT', 'TRABANT', 'opel']  - using enumerate
for idx, masina in enumerate(masini):
    if idx == 0 or idx == len(masini) - 1:
        masini[idx] = masina.lower()
    else:
        masini[idx] = masina.upper()
print(masini)

# Aceeasi lista,
# Vine un cumparator care doreste sa cumpere un Mercedes
# Iterati prin ea prin for each
# Daca masina e mercedes (if)
#    Printam ‘am gasit masina dorita de dvs’
#    Iesim din ciclu folosind un cuvant cheie care face acest lucru
# Altfel
#    Printam Am gasit masina X. Mai cautam
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for brand in masini:
    if brand =='Mercedes':
        print('am gasit masina  dorita de dvs.')
        break
    else:
        print(f'Am gasit masina {brand}. Mai cautam')

# Aceasi lista
# Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
# Daca masina e Trabant sau Lastun
#    Folositi un cuvant cheie care sa dea skip la ce urmeaza
# Printati S-ar putea sa va placa masina x
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for brand in masini:
    if brand =='Trabant':
        continue
    if brand == 'Lastun':
        continue
    print(f'S-ar putea sa va placa masina {brand}')
#
# Modernizati parcul de masini
# Creati o lista goala, masini_vechi
# Iterati prin masini
# Cand gasiti Lastun sau Trabant:
# Salvati aceste masini in masini_vechi
# Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
# Printati Modele vechi: x
# Modele noi: x
# cars = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# old_cars = []

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

masini_vechi = []
for a in range(len(masini)):
    if masini[a] in ('Trabant', 'Lastun'):
        masini_vechi.append(masini[a])
        masini[a] = 'Tesla'
print(f"Modele vechi: {masini_vechi}")
print(f"Modele noi: {masini}")

# or
for brand in cars:
    if brand =='Lastun':
        cars.remove('Lastun')
        old_cars.append('Lastun')
        cars.insert(7,'Tesla')
    elif brand == 'Trabant':
        cars.remove('Trabant')
        old_cars.append('Trabant')
        cars.insert(5,'Tesla')
        print(cars)
        print(old_cars)

# Avand dict
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro
# Prezentati doar masinile care se incadreaza in acest buget
# Iterati prin dict.items() si accesati masina si pretul
# Printati Pentru un buget de sub 15000 euro puteti alege masina x
# Iterati prin lista
carprice = {'Dacia': 6800,'Lastun': 500,'Opel': 1100,'Audi': 19000,'BMW': 23000}
for brand, amount in carprice.items():
    if amount <= 15000:
        print(f'Pentru un buget de sub 15000 puteti alege masina {brand}')

# Avand lista
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterati prin ea
# Afisati de cate ori apare 3
# (nu aveti voie sa folositi count)

l = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
print(len([i for i in l if i == 3]))
# or:
print(sum(i == 3 for i in l))

# Aceeasi lista
# Iterati prin ea
# Calculati si afisati suma numerelor
# (nu aveti voie sa folositi sum)

l = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
t=0

for nr in range(len(l)):
    t= t + l[nr]

print("Suma tuturor elementelor din lista este ", t)

# Aceeasi lista
# Iterati prin ea
# Afisati cel mai mare numar
# (nu aveti voie sa folositi max)
l = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# sorting the list
l.sort()

print('Cel mai mare element este:', l[-1])


cu for in:

a = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
nr_ref = 0
for i in a:
    if i > nr_ref:
        nr_ref = i
print(nr_ref)

#
# Aceeasi lista
# Iterati prin ea
# Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
# Ex: daca e 3, sa devina -3
# Afisati noua lista

nr = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for i in range(0, len(nr)):
    if (i>=0):
        nr[i] = (-abs(nr[i]))
print(nr)


# c. Optionale (may need google)
#
# 11.
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Iterati prin lista alte_numere
# Populati corect celelalte liste
# Afisati cele 4 liste la final

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for i in alte_numere:
    if (i%2 == 0):
        numere_pare.append(i)
    else:
        numere_impare.append(i)
    if (i>0):
        numere_pozitive.append(i)
    else:
        numere_negative.append(i)

print(numere_pare)
print(numere_impare)
print(numere_pozitive)
print(numere_negative)

# Aceeasi lista
# Ordonati crescator lista fara sa folositi sort
# Va puteti inspira vizual de aici
# https://www.youtube.com/watch?v=lyZQPjUT5B4
lst = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

for i in range(0, len(lst)-1):
    for j in range(i+1, len(lst)):
        if lst[j] < lst[i]:
            lst[i], lst[j] = lst[j], lst[i]
print(lst)

# Ghicitoare de numar
# numar_secret = Generati un numar random intre 1 si 30
# Numar_ghicit = None
# Folosind un while
#    User alege un numar
#    Programul ii spune:
# Nr secret e mai mare
# Nr secret e mai mic
# Felicitari! Ai ghicit!
import random
secret_nr = random.randint(1,30)
guessed_nr = None

while guessed_nr != secret_nr:
    guessed_nr = int(input("Ghiceste un nr intre 1 si 30: "))
    if guessed_nr == secret_nr:
        print("Felicitari! Ai ghicit!")
    elif guessed_nr < secret_nr:
        print("Nr secret e mai mare!")
    else:
        print("Nr secret e mai mic!")

#
# Alegeti un numar de la tastatura
# Ex:7
# Scrieti un program care sa genereze in consola urmatoarea piramida
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777


x = int(input("Introduceti un numar pentru a genera piramida: "))
for i in range(1,x+1):
    print(i*str(i))


# tastatura_telefon = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
# Iterati prin lista 2d
# Printati ‘Cifra curenta este x’
# (hint: nested for - adica for in for)

tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
for numar in tastatura_telefon:
    for tasta in numar:
        print(f"Cifra curenta este {tasta}")


