from socket import *
import random
import math

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

def criptografa(frase, p, q, ):
    N = p * q
    m = funcaoTotiente(p, q)
    e = primos_entre_si(m)

    D = multiplicaInverso(e, m)

    # Converte a frase em uma lista de inteiros usando a função ord
    frase_inteiros = [ord(char) for char in frase]

    # Criptografa cada caractere da frase
    frase_criptografada = [pow(i, e, N) for i in frase_inteiros]
    return frase_criptografada, N, D

def decriptografa(mensagem_criptografada, d, n):
    # Descriptografa cada caractere da mensagem
    mensagem_descriptografada = [pow(i, d, n) for i in mensagem_criptografada]

    # Converte a mensagem descriptografada de uma lista de inteiros para uma string usando a função chr
    return ''.join(chr(i) for i in mensagem_descriptografada)

serverPort = 1300
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(5) # o argumento “listen” diz à biblioteca de soquetes que queremos enfileirar no máximo 5 requisições de conexão (normalmente o máximo) antes de recusar começar a recusar conexões externas. Caso o resto do código esteja escrito corretamente, isso deverá ser o suficiente.

print ("TCP Server\n")
print ("Gerando números primos")
p = geraNumeroPrimo(4096)
q = geraNumeroPrimo(4096)
print ("Números Gerados")
n = p * q
m = funcaoTotiente(p, q)
e = primos_entre_si(m)

chavePublica = (e, n)

connectionSocket, addr = serverSocket.accept()
sentence = connectionSocket.recv(65000)
received = str(sentence,"utf-8")

print ("Received From Client: ", received)

capitalizedSentence = sentence.upper() # processamento
connectionSocket.send(capitalizedSentence)

sent = str(capitalizedSentence,"utf-8")
print ("Sent back to Client: ", sent)
connectionSocket.close()