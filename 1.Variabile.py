# Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
# variabilă:

marca_parfum =  'Dior' #sir de caractere  raspuns:<class 'str'>
an_fabricatie = 2021      #nr intreg  <class 'int'>
pret = 470.50           #nr zecimal  <class 'float'>
original = True          # True/False   <class 'bool'>

# Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.

print(type(marca_parfum))
print(type(an_fabricatie))
print(type(pret))
print(type(original))

# Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în aceeași variabilă (suprascriere):
# Verifică tipul acesteia.<class 'int'>
weight = round(pret)
print(type(pret))

# Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile.
# Rezolvă nepotrivirile de tip prin ce modalitate dorești.
# numar = '33'
# print(type(numar))    <class 'str'>
# daca vreau sa schimb in int voi scrie:
#     numar = 33 print(type(numar))    <class 'int'>
#   DACA VREAU SA TRANSF FLOAT IN INT:
#     a=33.33333
#  print(float(a)) # intoarce ca float
# print(int(float(a))) # intoarce ca int
# print(bool(float(a))) # intoarce ca bool TRUE

print(f"My favorite fragrance brand {marca_parfum}")
print(f"The manufacture year of my parfum is {an_fabricatie}")
print(f"The parfume cost is {pret}")
print(f'The parfume on Elefant.ro are original?{original}' )

# Citește de la tastatură:
# - numele;
# - prenumele.
# Afișează: 'Numele complet are x caractere'.
last_name = input("Add your first name: ")
first_name = input("Add your last name: ")

print(f"Your name has {len(last_name+first_name)} characters")

#  citeste de la tastatura lungimea
# # citeste de la tastatura latimea
# # afiseaza 'Aria dreptunghiului este x'
#
length = input("Introduceti lungimea dreptunghiului: ")
width = input("Introduceti latime dreptunghiului: ")

print(f"Aria dreptunghiului este: {int(length)*int(width)}")

# Avand stringul: 'Coral is either the stupidest animal or the smartest rock' afisati de cate ori apare cuvantul 'the'
# the_string = 'Coral is either the stupidest animal or the smartest rock'

my_string = 'Coral is either the stupidest animal or the smartest rock'
print(my_string.count("the"))

# acelasi string -inlocuieste the cu THE peste tot
# # printeaza rezultatul

my_string = 'Coral is either the stupidest animal or the smartest rock'
my_string = my_string.replace('the', "THE")

 # citeste de la tastatura un string de dimensiune impara
# afiseaza caracterul din mijloc
my_string = input("Introduceti un string de dimensiune impara: ")

mid_index = len(my_string) // 2
print(f'Caracterul din mijloc este {my_string[mid_index]}')

# 2. Folosind o singură linie de cod :
#
# - citește un string de la tastatură (ex: 'alabala portocala');
# - salvează fiecare cuvânt într-o variabilă;
# - printează ambele variabile pentru verificare.

my_string = input("Introduceti un string alcatuit din 2 cuvinte: ")

s1, s2 = my_string.split()
print(s1, s2)

# . EXERCIȚII SESIUNI STUDIU ÎN ECHIPĂ
#  Exercițiu:
# - citește un string de la tastatură (ex: alabala portocala);
# - salvează primul caracter într-o variabilă - indiferent care este el, încearcă
# cu 2 stringuri diferite;
# - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
# caracter => alAbAlA portocAla.

my_string = input("Introduceti un string: ")

first_character = my_string[0]
my_string = my_string[0] + my_string[1:-1].replace(first_character, first_character.upper()) + my_string[-1]
print(my_string)

# Cum facem sa afisam valoare lui pi cu doar 2 zecimale? presupunem pi = 3.146712
# pi = 3.146712

print(round(pi,2))
print(str(pi)[:4])
print(f"{pi:.2f}")

# Avand my_string = "Hello Pythonistas" , vrem sa afisam stringul: "eoyoss"
my_string = "Hello Pythonistas"
print(my_string[1::3])