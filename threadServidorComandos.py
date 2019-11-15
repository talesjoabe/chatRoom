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
class threadServidorComandos (threading.Thread):
    # redefine a funcao __init__ para aceitar a passagem parametros de entrada
    def __init__(self, clients, listaSockets, serverSocket):
        threading.Thread.__init__(self)
        self.clients = clients
        self.listaSockets = listaSockets
        self.serverSocket = serverSocket

    # a funcao run() e executada por padrao por cada thread
    def run(self):
        while True:
            command = input("")
            print(command)
            if(command.find("sair()")==0):
                for client in range(len(self.clients)):
                    mensagem= str("6"+'\0'+self.clients[client][0]+"\0sair()"+"\0o servidor foi encerrado")
                    mensagem = str(len(mensagem)+2)+'\0' + mensagem
                    self.listaSockets[client].send(str("6"+'\0'+self.clients[client][0]+"\0sair()"+"\0o servidor foi encerrado").encode('utf-8'))
                del self.clients
                del self.listaSockets
                self.serverSocket.close()
                exit()
            elif (command.find("lista()")==0):
                if len(self.clients) != 0:
                    print (self.clients)
                else:
                    print("sem clientes conectados")
