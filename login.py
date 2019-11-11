# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: TALES JOABE LIMA DA COSTA
#
# SCRIPT:
#

# importacao das bibliotecas
from socket import *
from client import *

# definicao das variaveis
username= ''
serverName = '' # ip do servidor
serverPort = 63200 # porta a se conectar

clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor

# O TAMANHO DO NICKNAME É RESTRITO A 16 OCTETOS
while len(username)==0 || len(s.encode('utf-8')) <=16:
    username = input('Username: ')

clientSocket.send(username.encode('utf-8'))
myThread(username, serverName, serverPort, clientSocket).start()
