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
from threadClientEnviarDados import *

# define uma classe para a criacao de threads
class threadClientReceberDados (threading.Thread):
    # redefine a funcao __init__ para aceitar a passagem parametros de entrada
    def __init__(self, username, serverName, serverPort, clientSocket):
        threading.Thread.__init__(self)
        self.username = username
        self.serverName = serverName
        self.serverPort = serverPort
        self.clientSocket = clientSocket
        self._kill = threading.Event()
        #self.kill = threading.Event()

    # a funcao run() e executada por padrao por cada thread
    def run(self):
        while True:
            protocolo = self.clientSocket.recv(1024).decode('utf-8')
            #protocolo = protocolo.split('\0')
            #print(protocolo)
            mensagem = comandos(protocolo)
            #print(mensagem)
            #print("\0\0")
            mensagem = mensagem.split('\0')
            #print(mensagem)

            if(len(mensagem)!=0):
                if(mensagem[0]=='1'):
                    if(mensagem[1] != self.username):
                        print(colored(mensagem[1], 'green'), "entrou na sala\0")
                    else:
                        print(colored("você", 'green'), "entrou na sala\0")
                        threadClientEnviarDados(self.username, self.serverName, self.serverPort, self.clientSocket).start()
                elif(mensagem[0]=='2'):
                    if(mensagem[1] != self.username):
                        print(colored(mensagem[1], 'red'), "saiu da sala")
                    else:
                        print(colored("você", 'red'), "saiu da sala")
                        self.clientSocket.close()
                        self._kill.set()
                elif(mensagem[0]=='3'):
                    print(mensagem[2])
                elif(mensagem[0]=='4'):
                    if(mensagem[1] != self.username):
                        print(colored(mensagem[1], 'green'), "escreveu: ", mensagem[2])
                elif(mensagem[0]=='5'):
                    if(mensagem[2] == self.username):
                        print(colored(mensagem[1], 'green'), "escreveu em privado   : ", mensagem[3])
