
# Verifica si afiseaza daca x este numar natural sau nu:
# inside:
x = 3
if x >= 0:
    print(f'Numarul {x} este natural')
else:
    print(f'Numarul {x} NU este natural')

x = -1
if x >= 0:
    print(f'Numarul {x} este natural')
else:
    print(f'Numarul {x} NU este natural')

x = 1.5
if x >= 0 and isinstance(x, int):
    print(f'(Numarul {x} este natural')
else:
    print(f'Numarul {x} NU este natural')

#outside:
number = int(input("Please enter a number : "))

if int(number) >=0:
  print('True')
else:
   print('False')

# Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

nr = int(input("Introduceti un numar: "))
if nr == 0:
    print('Nr e neutru')
elif nr < 0:
    print('Nr e negativ')
elif nr > 0:
    print('Nr e pozitiv')

# Verifica si afiseaza daca x este intre -2 si 13

print(x >= -2 and x <= 13)
#another solution
print(x in range(-2, 13))

# Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5

nr = int(input('introduceti un numar:'))
nr_1 = int (input('introduceti un al 2lea numar:'))
if (nr-nr_1)<5:
    print(f'diferenta numerelor este mai mica decat 5')
else:
    print ('diferenta dintre cele 2 numere este mai mare sau egala cu 5')

#Pentru acelasi exercitiu dar tinand cont de numarul mai mare:
x = int(input('Indroduceti x: '))
y = int(input('Indroduceti y: '))
if x >= y:
    diferenta = x - y
else:
    diferenta = y - x

if diferenta < 5:
    print("Diferenta e mai mica decat 5")
else:
    print("Diferenta e mai mare sau egala cu 5")
#  Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)

print(not(x >= 5 and x <= 27))

# x si y (int)
# Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare
x = int(input('Introduceti o valoare'))
y = int(input('Mai introduceti o valoare'))
if x == y:
    print(f"x={x} este egal cu y={y}")
elif x > y:
    print(f"x={x} este mai mare decat y={y}")
else:
    print(f"x={x} este mai mic decat y={y}")

# X, y, z - laturile unui triunghi
# Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.
#
a = int(input('Introduceti valoare latura A'))
b = int(input('Introduceti valoarea laturei B'))
c = int(input('Introduceti valoarea laturei C'))
if a==b and b==c:
    print('triunghiul tau este echilateral')
elif a==b or a==c or b==c:
    print('triunghiul tau este isoscel')
else:
    print ('triunghiul este unul oarecare')

# Citeste o litera de la tastatura
# Verifica si afiseaza daca este vocala sau nu

a = input("Te rog sa introduci orice litera din alfabet: ")
if a in ('a', 'ă', 'î', 'â', 'e', 'i', 'o', 'u'):
	print("%s litera este vocala" % a)

else:
	print("%s litera este consoana" % a)

# Transforma si printeaza notele din sistem romanesc in  >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F
nota = float(input('Introduceti nota copilului pentru a vedea echivalentul in UK:'))
if nota >10:
	print('Introduceti o valoare intre 1-10')
elif nota >= 9:
	print ('A')
elif nota >= 8:
	print('B')
elif nota >= 7:
	print('C')
elif nota >= 6:
	print('D')
elif nota >= 5:
	print('E')
else:
	print('F')

# c. Optionale (may need google)
#
# 11.Verifica daca x are minim 4 cifre (x e int)
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
x = input('x = ')
x = str(x)
if x[0] == '-':
    x = x[1:]
if x[0] == '0':
    x = x[1:]

if x.isnumeric():
    if len(x) < 4:
        print("Nr NU are minim 4 cifre!")
    else:
        print("Nr are minim 4 cifre!")
else:
    print("Nu ati introdus un nr valid")

# Verifica daca x are exact 6 cifre
x = input('x = ')
x = str(x)
if x.replace('-', '', 1).replace('.', '', 1).isnumeric():
    if x[0] == '0':
        x = x[1:]
    if (len(x) == 6 and '.' not in x) or (len(x) == 7 and ('.' in x or '-' in x)) or (len(x) == 8 and '.' in x and '-' in x):
        print('Nr are exact 6 cifre!')
    else:
        print('Nr nu are exact 6 cifre!')
else:
    print("Nu ati introdus un numar valid!")
# 13.
# Verifica daca x este numar par sau impar (x e int)
x = int(input("x = "))
if x % 2 == 0:
    print(f"x={x} e par")
else:
    print(f"x={x} e impar")
# x, y, z (int)
# Afiseaza care este cel mai mare dintre ele?
x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))

if (x == y and x > z) or (x == z and x > y) or (y == z and y > x):
    print("Doua numere sunt egale si mai mari decat al 3-lea..")
else:
    if x > y and x > z:
        print(f"x={x} e cel mai mare")
    elif y > x and y > z:
        print(f"y={y} e cel mai mare")
    else:
        print(f"z={z} e cel mai mare")

# X, y, z - reprezinta unghiurile unui triunghi
# Verifica si afiseaza daca triunghiul este valid sau nu
if x+y<=z or y+z<=x or z+x<=y:
    print("Triunghi invalid")
else:
    print("Triunghi valid")

# Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
# cititi de la tastatura un int x
# afiseaza stringul fara ultimele x caractere
# ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'

my_string = 'Coral is either the stupidest animal or the smartest rock'
x = int(input("Alegeti numarul de caractere care sa se elimine din string: "))
print(my_string[:-x])

# acelasi string
# declara un string nou care sa fie format din primele 5 caractere + ultimele 5

my_string = 'Coral is either the stupidest animal or the smartest rock'
new_string = my_string[:5] + my_string[-5:]
print(new_string)

# citeste de la tastatura un string
# verifica daca primul si ultimul caracter sunt la fel
# se va folosi un assert
# atentie: se doreste ca programul sa fie case insensitive
# 'apA' e acceptat

the_string = input("Introduceti un string: ")
assert the_string[0].lower() == the_string[-1].lower()

# avand stringul '0123456789'
# afisati doar numerele pare
# acum afisati doar numerele impare
# (hint: folositi slicing, controlati din pas)
my_string = '0123456789'
print(f"Numerele pare sunt:  {my_string[::2]}")
print(f"Numerele impare sunt: {my_string[1::2]}")
#or
str = '0123456789'
print(str[0:len(str):2])
print(str[1:len(str):2])
# Bonus la cerere:
# 21.
# Verificare imbarcare persoane
# Tineti urmatoarele date
# Varsta
# Insotit de mama
# Insotit de tata
# Pasaport
# Act permisiune mama
# Act permisiune tata
#
# Conditii de imbarcare
# Daca pers are varsta peste 18 ani si are pasaport
# Daca pers are sub 18 ani, are pasaport si e insotita de ambii parinti
# Daca pers are sub 18 ani, are pasaport, e insotita de cel putin un parinte si are permisiune in scris de la celalat parinte
#
# Aici vreau sa testati codul cu toate variantele posibile
# Sa generati cazuri de test si expected result, apoi sa rulati codul si sa completati actual results
#
# Ex:
# Varsta 19 ani, nu am pasaport => Nu ma pot imbarca
# Varsta 17 ani, am pasaport, ambii parinti => Ma pot imbarca
age = int(input("Introduceti varsta (introduceti o varsta valida): "))
passport = bool(int(input("Persoana are pasaport? (introduceti 1 pt da, 0 pt nu)")))
accompanied_mother = bool(int(input("Persoana e insotita de mama? (introduceti 1 pt da, 0 pt nu): ")))
accompanied_father = bool(int(input("Persoana e insotita de tata? (introduceti 1 pt da, 0 pt nu): ")))
permission_mother = bool(int(input("Persoana are act de permisiune de la mama? (introduceti 1 pt da, 0 pt nu): ")))
permission_father = bool(int(input("Persoana are act de permisiune de la tata? (introduceti 1 pt da, 0 pt nu): ")))

if (age >= 18 and passport) or (age < 18 and passport and accompanied_father and accompanied_mother) or \
(age < 18 and passport and accompanied_father and permission_mother) or (age < 18 and passport and accompanied_mother and permission_father):
    print("Person boarded")
else:
    print("Person cannot board")
# 22. Joc ghicit zarul
# Cauta pe net si vezi cum se genereaza un numar random
# Ne imaginam ca dam cu zarul si salvam acest numar in dice_roll
# Luati un nr ghicit de la utilizator
# Verificati si afisati daca utilizatorul a ghicit
# 3 optiuni
# Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
# Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
# Ai ghicit. Felicitari? Ai ales x si zarul a fost y
#
import random

numar_secret = random.randint(0,6)
numar_ghicit = None
while numar_ghicit != numar_secret:
    numar_ghicit = int(input('Ghiceste un numar intre 0 si 6\n'))
    if numar_secret > numar_ghicit:
        print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {numar_ghicit}, dar a fost {numar_secret}')
    elif numar_secret < numar_ghicit:
        print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {numar_ghicit}, dar a fost {numar_secret}')
    else:
        print(f'Ai ghicit. Felicitări! Ai ales {numar_secret} si zarul a fost {numar_secret}')


