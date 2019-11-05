# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Thread com execucao paralela
#

# importacao das bibliotecas
import threading # threads
import time # tempo (opcional)
from socket import *
from termcolor import colored
from functions import *

# define uma classe para a criacao de threads
class myThread (threading.Thread):
    # redefine a funcao __init__ para aceitar a passagem parametros de entrada
    def __init__(self, username, serverName, serverPort):
        threading.Thread.__init__(self)
        self.username = username
        self.clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
        self.clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor
        self.clientSocket.send(username.encode('utf-8')) # envia o nickname para o servidor

    # a funcao run() e executada por padrao por cada thread
    def run(self):
        #Mostrar que está conectado
        clientOn(self.clientSocket.recv(1024));
        

        self.clientSocket.close()
