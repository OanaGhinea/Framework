# Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite si apelati toate metodele clasei
# Clasa Cerc
# Atribute: raza, culoare
# Constructor pt ambele atribute

# Metode:
# descrie_cerc() - va PRINTA culoarea si raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()

class Cerc_initial():
    def __init__(self, r, c):
        self.raza = r
        self.culoare = c

    def descriere_cerc(self):
        print(f"Circle radius is {self.raza} and color is {self.culoare}")

    def area(self):
        return self.raza ** 2 * 3.14

    def diametru(self):
        return 2 * self.raza

    def circumferinta(self):
        return 2 * self.raza * 3.14


Cerc = Cerc_initial(8, 'red')
Cerc.descriere_cerc()
print(Cerc.area())
print(Cerc.diametru())
print(Cerc.circumferinta())
Cerc2 = Cerc_initial(10, 'green')
Cerc.descriere_cerc()
print(Cerc.area())
print(Cerc.diametru())
print(Cerc.circumferinta())

# Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pt toate atributele
# Metode:
# descrie()
# aria()
# perimetrul()
# schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().

class Dreptunghi():
    def __init__(self, lung, lat, c, c2):
        self.lungime =lung
        self.latime = lat
        self.culoare = c
        self.new_color = c2

    def descriere_dreptunghi(self):
        print('Culoarea dreptunghiului este:'+ self.culoare)
        print('Lungimea este:' , self.lungime)
        print( 'Latimea este: ' , self.latime)


    def perimetru_dreptunghi(self):
        return 2 * self.lungime + 2 * self.latime

    def arie_dreptunghi(self):
        return self.lungime * self.latime

    def descriere_dreptunghi(self):
        print('Lungimea este:' , self.lungime)
        print( 'Latimea este: ' , self.latime)
        print('Noua culoare este:' + self.new_color)

dreptunghi1=Dreptunghi(5, 3, 'galben', 'rosu')
dreptunghi1.descriere_dreptunghi()
print(dreptunghi1.perimetru_dreptunghi())
print(dreptunghi1.arie_dreptunghi())
dreptunghi2=Dreptunghi(8, 4, 'roz', 'portocaliu')
dreptunghi2.descriere_dreptunghi()
print(dreptunghi2.perimetru_dreptunghi())
print(dreptunghi2.arie_dreptunghi())

# Clasa Angajat
#
# Atribute: nume, prenume, salariu
#
# Constructor pt toate atributele
#
# Metode:
# descrie()
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)

class Angajat():
    def __init__(self, num, pren, salar, sal2):
        self.nume = num
        self.prenume = pren
        self.salariu = salar
        self.salariu_nou = sal2

    def nume_complet(self):
      return 'Numele angajatului este:' + self.nume +" "+ self.prenume

    def salariu_lunar(self):
        return self.salariu
    def salariu_anual(self):
        return self.salariu * 12
    def marire_salariu(self):
         return str(100 * float(self.salariu_nou)/float(self.salariu)) + '%'

angajat2=Angajat('Mike', 'Sweedy', 4000, 300)
print(angajat2.nume_complet())
print(angajat2.salariu_lunar())
print(angajat2.salariu_anual())
print(angajat2.marire_salariu())

# Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate
# Metode:
# afisare_sold() - Titularul x are in contul y suma de n lei
# debitare_cont(suma)
# creditare_cont(suma)
#
#
class Cont():
    def __init__(self, titular, iban, so):
        self.titular = titular
        self.iban = iban
        self.sold_initial = so

    def detalii_titular(self):
       print(f"Titulaul {self.titular} are contul {self.iban} si suma de {self.sold_initial}RON")

    def debit_cont(self, suma):
      if suma > self.sold_initial:
          print()
      else:
          self.sold_initial -= suma
          print(f"{suma}RON a fost debitata din cont")

    def credit_cont(self, suma):
          self.sold_initial += suma
          print(f"{suma} RON a fost creditata din cont")

contul_meu = Cont('OanaG', 'Ro1111222233334444', 100_000_000)
contul_meu.detalii_titular()
contul_meu.debit_cont(600_000)
contul_meu.detalii_titular()
contul_meu.credit_cont(770_000)
contul_meu.detalii_titular()
cont2 = Cont('Irina Petre', 'Ro1111222233334444', 900_000)
cont2.detalii_titular()
cont2.debit_cont(30_000)
cont2.detalii_titular()
cont2.credit_cont(75_000)
cont2.detalii_titular()

# Clasa Factura
# Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie
#
# Metode:
# schimba_cantitatea(cantitate)
# schimba_pretul(pret)
# schimba_nume_produs(nume)
# genereaza_factura() - va printa tabelar daca reusiti
#
# Factura seria x numar y
# Data: generati automat data de azi
# Produs | cantitate | pret bucata | Total
# Telefon |      7       |       700       | 49000
#
# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/
from datetime import date

class Factura:
    serie ="78574493"

    def __init__(self, number, product_name, quantity, price_per_unit):
        self.number = number
        self.product_name = product_name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def change_quantity(self, new_quantity):
        self.quantity = new_quantity

    def change_price(self, new_ppu):
        self.price_per_unit = new_ppu

    def change_product_name(self, new_prod_name):
        self.product_name = new_prod_name

    def generate_bill(self):
        print(f"Date: {date.today()}\nProduct|Quantity|Price per unit|Total\n{self.product_name}|{self.quantity}|{self.price_per_unit}|{self.quantity * self.price_per_unit}")


vizualizam_factura = Factura(457, "Enel",78, 164)
vizualizam_factura.generate_bill()
