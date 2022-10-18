# C09_EX03 (Tema ex1): a) Scrieti o functie care primeste un numar natural si returneaza daca e prim sau nu
#  e.g.: is_prime(13) => True
#          is_prime(24) => False
# b) Scrieti test unitare pentru functia is_prime
# c). Scrieti o functie care are 2 parametrii nr naturale a,b cu a<b. Functia returneaza lista numerelor prime din intervalul [a,b].
# e.g.: list_of_primes_in_interval(3, 31) => [3,5,7,11,13,17,19,23,29,31]
# d) Scrieti test unitare pentru functia list_of_primes_in_interval

def isprime(num):
    for n in range(2, int(num**0.5)+1):
        if num%n==0:
            return False
        return True


def prime_list(a, b):
    prime_list = []
    for i in range(a, b):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i / 2) + 1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list
