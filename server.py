# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: TALES JOABE LIMA DA COSTA
#
# SCRIPT:
#

# importacao das bibliotecas
from socket import * # sockets
from functions import *
from threadServidorRecebeDados import *


def sair():
    clientSocket.close() # encerramento o socket do cliente

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 63000# porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))
clients = []
listaSockets = []
while True:
      connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
      addListSockets(listaSockets, connectionSocket)
      username = connectionSocket.recv(1024) # recebe dados do cliente
      username = str(username).encode('utf-8')
      addListClient(clients,username, addr[0], addr[1])
      print(username.decode('utf-8')[2:len(username)-1]+ " contectou-se")
     # print(clients, listaSockets)

      protocolo = '0'+'\0'+username.decode('utf-8')[2:len(username)-1]+'\0'+'entrar()'+'\0'+""

      for client in range(len(listaSockets)):
              listaSockets[client].send(protocolo.encode('utf-8'))

      threadServidorRecebeDados(clients, username, listaSockets, connectionSocket, addr[0],addr[1]).start()
