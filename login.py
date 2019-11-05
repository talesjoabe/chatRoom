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
serverName = '' # ip do servidor
serverPort = 64000 # porta a se conectar

username = input('Username: ')

myThread(username, serverName, serverPort).start()
