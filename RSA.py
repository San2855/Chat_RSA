import random

def totient(number): 
    if is_prime(number):
        return number - 1
    else:
        return False

def is_prime(n): # verifica se um número é primo
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
           return False
        i += 6
    return True

def generate_e(num): 
    def gcd(n1, n2):
        rest = 1
        while n2 != 0:
            rest = n1 % n2
            n1 = n2
            n2 = rest
        return n1

    while True:
        e = random.randrange(2, num) 
        if gcd(num, e) == 1:
            return e

def generate_prime(): # gera o número primo - p e 
    while True: # 2**2048 é o padrão de chaves RSA
        x = random.randrange(1, 100) # define o intervalo
        if is_prime(x):
            return x

def mod(a, b): # função módulo
    if a < b:
        return a
    else:
        c = a % b
        return c

def cipher(words, e, n): # obtém as palavras e calcula a cifra
    tam = len(words)
    i = 0
    lista = []
    while i < tam:
        letter = words[i]
        k = ord(letter)
        k = k ** e
        d = mod(k, n)
        lista.append(str(d))
        i += 1
    return lista

def decipher(cipher, n, d):
    lista = ""
    i = 0
    tamanho = len(cipher)
    # texto = cifra ^ d mod n
    while i < tamanho:
        result = int(cipher[i]) ** d
        texto = mod(result, n)
        letra = chr(texto)
        lista = lista + letra
        i += 1
    return lista

def calculate_private_key(totient, e):
    d = 0
    while mod(d * e, totient) != 1:
        d += 1
    return d
