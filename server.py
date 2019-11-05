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

# definicao das variaveis
lista = []
serverName = '' # ip do servidor (em branco)
serverPort = 64000 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))
clients = []
while True:
  connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
  username = connectionSocket.recv(1024) # recebe dados do cliente
  username = str(username).encode('utf-8')

  connectionSocket.send(username)
  addList(clients,username, addr[0], addr[1])

  #connectionSocket.send(capitalizedSentence.encode('utf-8')) # envia para o cliente o texto transformado
  connectionSocket.close() # encerra o socket com o cliente
serverSocket.close() # encerra o socket do servidor
