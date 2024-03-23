import socket
import helper

serverPort = 1300
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(5)

print ("TCP Server\n")
print ("Gerando números primos")
p = helper.geraNumeroPrimo(1024)
q = helper.geraNumeroPrimo(1024)
print ("Números Gerados")

n = p * q
resultadoTotient = helper.funcaoTotiente(p, q)
resultadoPrimos = helper.primos_entre_si(resultadoTotient)
chavePublica = helper.gerarChavePublica(resultadoTotient, n)
chavePrivada = helper.modInverso(chavePublica[0], resultadoTotient)
print('n', n)
print('resultadoTotient ', resultadoTotient)
print('resultadoPrimos ', resultadoPrimos)

while True :
    connectionSocket, addr = serverSocket.accept()
    connectionSocket.sendall(str(chavePublica).encode())

    mensagem = connectionSocket.recv(65536)
    chavePublicaCliente = eval(mensagem.decode())
    print ("Chave publica cliente: ", chavePublicaCliente)

    mensagem = connectionSocket.recv(65536)
    mensagemEncriptada = eval(mensagem.decode())
    mensagemDecriptada = helper.decriptografa(mensagemEncriptada, chavePrivada, n)

    print("Mensagem recebida: ", mensagemDecriptada)

    mensagemMaiuscula = helper.criptografa(mensagemDecriptada.upper(), chavePublicaCliente) # processamento
    connectionSocket.send(str(mensagemMaiuscula).encode())

    sent = mensagemDecriptada.upper()
    print ("Sent back to Client: ", sent)