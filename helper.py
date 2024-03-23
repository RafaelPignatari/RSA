import math
import random

def primos_entre_si(totient):
    e = 2
    while math.gcd(e, totient) != 1:
        e += 1
    return e

def numeroEhPrimo(n, k=5):  
    if n < 2: return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n % p == 0: return n == p
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1: continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else: return False
    return True

def geraNumeroPrimo(bits):
    while True:
        p = random.getrandbits(bits)
        if numeroEhPrimo(p): return p

def multiplicaInverso(e, phi):
    def extended_gcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = extended_gcd(b % a, a)
            return (g, y - (b // a) * x, x)

    _, x, _ = extended_gcd(e, phi)
    return x % phi

def funcaoTotiente(p, q):
    return (p-1) * (q-1)

def criptografa(frase, chavePublica):
    e, n = chavePublica  # unpack the public key into e and n
    cipherText = [pow(ord(char), e, n) for char in frase]

    return cipherText

def decriptografa(mensagem_criptografada, chavePrivada, n):
    # Descriptografa cada caractere da mensagem
    mensagem_descriptografada = [pow(i, chavePrivada, n) for i in mensagem_criptografada]

    # Converte a mensagem descriptografada de uma lista de inteiros para uma string usando a função chr
    return ''.join(chr(i) for i in mensagem_descriptografada)

def gerarChavePublica(totient, n):
    while True:
        e = random.randint(2, totient - 1)
        if math.gcd(e, totient) == 1:
            return e, n

def modInverso(rp, rt):
    m0, x0, x1 = rt, 0, 1

    while rp > 1:
        q = rp // rt
        rt, rp = rp % rt, rt
        x0, x1 = x1 - q * x0, x0

    return x1 + m0 if x1 < 0 else x1