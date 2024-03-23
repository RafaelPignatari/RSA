import socket
import helper

print ("TCP Server\n")
print ("Gerando números primos")
p = helper.geraNumeroPrimo(4096)
q = helper.geraNumeroPrimo(4096)
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

serverAddress = ('10.1.70.23', 1300)
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
input ("Pressione uma tecla para conectar ao servidor")
clientSocket.connect(serverAddress)

mensagem = clientSocket.recv(524288)
chavePublicaServidor = eval(mensagem.decode())
print ("Chave publica servidor: ", chavePublicaServidor)
clientSocket.send(str(chavePublicaCliente).encode())
sentence = input("Input lowercase sentence: ")

clientSocket.send(str(helper.criptografa(sentence, chavePublicaServidor)).encode())

mensagem = clientSocket.recv(524288)
msgCriptografada = eval(mensagem.decode())
msgDecriptografada = helper.decriptografa(msgCriptografada, chavePrivadaCliente, n)

print ("Received from Make Upper Case Server: ", msgDecriptografada)

clientSocket.close()