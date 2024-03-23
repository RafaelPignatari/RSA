import socket
import helper

print ("TCP Server\n")
print ("Gerando números primos")
p = helper.geraNumeroPrimo(1024)
q = helper.geraNumeroPrimo(1024)
print ("Números Gerados")

n = p * q
resultadoTotient = helper.funcaoTotiente(p, q)
resultadoPrimos = helper.primos_entre_si(resultadoTotient)
chavePublicaCliente = helper.gerarChavePublica(resultadoTotient, n)
chavePrivadaCliente = helper.modInverso(chavePublicaCliente[0], resultadoTotient)
print('n', n)
print('resultadoTotient ', resultadoTotient)
print('resultadoPrimos ', resultadoPrimos)
print('chavePublica ', chavePublicaCliente)
print('chavePrivada ', chavePrivadaCliente)

serverAddress = ('192.168.228.121', 1300)
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
input ("Pressione uma tecla para conectar ao servidor")
clientSocket.connect(serverAddress)

mensagem = clientSocket.recv(65536)
chavePublicaServidor = eval(mensagem.decode())
print ("Chave publica servidor: ", chavePublicaServidor)
clientSocket.send(str(chavePublicaCliente).encode())
sentence = input("Input lowercase sentence: ")

# clientSocket.send(bytes(helper.criptografa(sentence, chavePublica), "utf-8"))
clientSocket.send(str(helper.criptografa(sentence, chavePublicaServidor)).encode())

mensagem = clientSocket.recv(65536)
msgCriptografada = eval(mensagem.decode())
msgDecriptografada = helper.decriptografa(msgCriptografada, chavePrivadaCliente, n)

print ("Received from Make Upper Case Server: ", msgDecriptografada)

clientSocket.close()