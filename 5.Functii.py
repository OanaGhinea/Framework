
# 1. Functie care sa calculeze si sa returneze suma a 2 numere

def sum(a,b):
    print(a+b)

# 2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar

def par_impar(x):
  return x % 2 == 0

a=par_impar(11)
print(a)

# 3. Functie care returneaza numarul total de caractere din numele tau complet.
# (nume, prenume, nume_mijlociu)

def caractere_nume(full_name):
  return len(full_name) - full_name.count(' ')

ind_nume = caractere_nume('Oana Maria Ghinea')

print(ind_nume)

Varianta de la tastatura:

def main():
  full_name = str(input("Please enter in a full name: ")).split(" ")

  for x in full_name:
    print(len(x))
y=main()
print(y)

# 4. Functie care returneaza aria dreptunghiului

def arie_dreptunghi(lungime, latime):
  return  lungime * latime
print(arie_dreptunghi(2,3))

# 5. Functie care returneaza aria cercului

import math
def arie_cerc(raza):
  return raza ** 2 * math.pi

raza = float(input("Te rugam sa introduci raza cercului: "))
print(" Aria cercului este:", arie_cerc(raza))

# 6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. False daca nu

	def my_char(a, string):
        return a in string

print(my_char('Hi', 'Hi my dear viewer'))

# 7. Functie fara return, primeste un string si printeaza pe ecran:
# Nr de caractere lower case este x
# Nr de caractere upper case exte y

def funct(my_str):
    up = 0
    low = 0
    for i in my_str:
        if i.isupper():
           up +=1
        else:
           low +=1
    print (f'String original: {my_str}')
    print (f'Numarul caracterelor lower case este: {low}')
    print (f'Numarul caracterelor upper case este: {up}')

# 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
def nr_pozitive(lst):
    lst_init = []
    for n in lst:
        if n > 0:
            lst_init.append(n)

    return lst_init

print(nr_pozitive([1, -6, -4, 22, 5, 3, -9]))


# 9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
# Primul numar x este mai mare decat al doilea nr y
# Al doilea nr y este mai mare decat primul nr x
# Numerele sunt egale.

def nr(a, b):
    if a > b:
        print (f'Primul numar {a} este mai mare decat al 2-lea numar {b}')
    if b > a:
        print (f'Al doilea numar {b} este mai mare decat primul numar {a}')
    if b == a:
        print ('Numerele sunt egale')

nr(1,-8)
#
# 10. Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False
def numere(nr, set):

  for var in nr:
    if var in set:
      print('Nu am adaugat numarul in set. Acesta exista deja')
      return False
    else:
      set.add(var)
      print('Am adaugat numarul nou in set')
      return True


print(numere({1}, {10, 11}))

# c. Optionale (may need google)
#
# 11. Functie care primeste o luna din an si returneaza cate zile are acea luna

from calendar import monthrange
def zile_luna(an=2022, luna=12):
    return monthrange(an, luna)[1]
print(zile_luna(2022, 12))

# 12. Functie calculator care sa returneze 4 valori
# Suma, diferenta, inmultirea, impartirea a 2 numere
#
# In final vei putea face:
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)
def calculator(x, y):
    return x+y, x-y, x*y, x/y

a, b, c, d = calculator(9, 3)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)

# 13. Functie care primeste o lista de cifre (adica doar 0-9)
# Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returneaza un DICT care ne spune de cate ori apare fiecare cifra
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }
from collections import Counter


def digits_count(digits):
    return dict(Counter(digits))

    return digits_count_dict


print(digits_count([1, 3, 1, 5, 9, 7, 7, 5, 5]))

# 14. Functie care primeste 3 numere
# Returneaza valoarea maxima dintre ele

def nr_mare(x, y, z):
    if (x >= y) and (x >= z):
        numar_mare = x
    elif (y >= x) and (y >= z):
        numar_mare = y
    else:
        numar_mare = z
    return numar_mare
print(nr_mare(1, 2, 3))
print(nr_mare(7, 6, 5))
print(nr_mare(4, 6, 4))

# 15. Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
# Ex: daca dam nr 3
# Suma va fi 6 (0+1+2+3)

def suma(n):
    return sum(range(n+1))
suma_nr = suma(6) #1+2+3+4+5+6=21
print(suma_nr)

# 16. Functie care nu primeste argumente, dar cere un input de la tastatura si va printa
# “Numarul ales este pozitiv” sau “Numarul ales este negativ” sau “Numarul ales este 0”, dupa caz, iar daca nu introducem un numar, sa se afiseze “Nu ati ales un numar valid”; la final sa se afiseze “Sfarsitul functiei” indiferent de caz.

def numar_ales():
    num = float(input("Enter a number: "))
    if num > 0:
        print("Positive number")
    elif num == 0:
        print("Zero")
    else:
        print("Negative number")
print(input(numar_ales()))




# BONUS:
#
# 17. Functie care primesete 2 liste de numere (numerele pot fi dublate)
# Returnati numerele comune
#
# Ex:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Raspuns: {2, 3}

def elem_comune(a, b):
	a_set = set(a)
	b_set = set(b)

	if (a_set & b_set):
		print(a_set & b_set)
	else:
		print("No common elements")

print(elem_comune([1,2,3,4,5], [2,3,5,7,8]))
print(elem_comune([1,2,3,4,5], [0,6,7,8]))

# 18. Functie care sa aplice o reducere de pret. Daca apelul functiei nu primeste valoarea reducerii, sa ia valoarea default 10%.
# Daca produsul costa 100 lei si aplicam reducere de 10%
# Pretul va fi 90
# Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida
def discount(price, discount_percent=10):
    if discount_percent in range(0, 100):
        return price - price * discount_percent / 100
    else:
        print("Reducerea nu este valida")


print(discount(100, 50))
print(discount(100))
# 19. Functie care sa afiseze data si ora curenta din ro

def display_date_time():
    now = datetime.now()
    print(f"Date and time Romania: {now}")
    print(f"Date and time China: {now + timedelta(hours=5)}")
display_date_time()
# 20. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la craciun daca nu vrei sa ne zici cand e ziua ta :)

from datetime import date
def nr_zile(zi_curenta, zi_nastere):
    return (zi_curenta-zi_nastere).days
zi_curenta = date(2022, 9, 19)
zi_nastere = date(2022, 12, 3)
print (nr_zile(zi_curenta, zi_nastere), "zile pana la ziua mea")

# 21. Functie in care sa dai un nume romanesc si sa iti printeze pe ecran
# ‘Numele este de baiat’ sau ‘Numele este de fata’
def name_type(name):
    if name[-1] == 'a' or name in (
    'Carmen','Miriam','Joanne'):
        print('Numele este de fata')
    else:
        print('Numele este de baiat')


name_type("Medeea")
name_type("Andrei")