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
    def __init__(self, username, serverName, serverPort, clientSocket):
        threading.Thread.__init__(self)
        self.username = username
        self.serverName = serverName
        self.serverPort = serverPort
        self.clientSocket = clientSocket

    # a funcao run() e executada por padrao por cada thread
    def run(self):
        while True:
            mensagem = self.clientSocket.recv(1024).decode('utf-8')
            if(len(mensagem)!=0):
                if(mensagem[0]=='1'):
                    if(mensagem[1:] != self.username):
                        print(colored(mensagem[1:], 'green'), "entrou na sala")
                    else:
                        print(colored("você", 'green'), "entrou na sala")
                elif(mensagem[0]=='2'):
                    if(mensagem[1:] != self.username):
                        print(colored(mensagem[1:], 'red'), "saiu da sala")
                    else:
                        print(colored("você", 'green'), "saiu na sala")
            else:
                mensagem = input("Digite: ")
                
