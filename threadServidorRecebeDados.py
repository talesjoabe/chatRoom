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
class threadServidorRecebeDados (threading.Thread):
    # redefine a funcao __init__ para aceitar a passagem parametros de entrada
    def __init__(self, clients, username, listaSockets, connectionSocket, ip, port):
        threading.Thread.__init__(self)
        self.clients = clients
        self.username = username
        self.listaSockets = listaSockets
        self.connectionSocket = connectionSocket
        self.ip= ip
        self.port= port

    # a funcao run() e executada por padrao por cada thread
    def run(self):
        while True:
            protocolo = self.connectionSocket.recv(1024).decode('utf-8')

            if(protocolo.split('\0')[2]=="lista()"):
                    protocolo = protocolo+str(self.clients)
                    for i in range(0,len(self.clients)):
                        if(self.clients[i][0]==protocolo.split('\0')[1]):
                            print(self.clients[i][0]+" solicitou a listagem de membros")
                            self.listaSockets[i].send(protocolo.encode('utf-8'))
                            break
            else:
                for client in range(len(self.listaSockets)):
                        self.listaSockets[client].send(protocolo.encode('utf-8'))

                if(protocolo.split('\0')[2]=="sair()"):

                    for i in range(0,len(self.clients)):
                        if(self.clients[i][0]==protocolo.split('\0')[1]):
                            print(self.clients[i][0]+" desconectou-se")
                            del self.clients[i]
                            del self.listaSockets[i]
                            #print(self.clients,self.listaSockets)
                            break
