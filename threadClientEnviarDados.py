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
import re

# define uma classe para a criacao de threads
class threadClientEnviarDados (threading.Thread):
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
            mensagem = input("")
            if(mensagem[0:7] == 'sair()'):
                comando = mensagem[0:7]
                dados = mensagem[mensagem.find(')')+1:]
                tam = len(dados)
            elif(mensagem.find("privado(")) == 0:
                comando = mensagem[0:mensagem.find(')')]
                dados = mensagem[mensagem.find(')')+1:]
                tam = 0
            elif(mensagem[0:8] == 'lista()'):
                comando = mensagem[0:8]
                dados = mensagem[mensagem.find(')')+1:]
                tam = len(dados)
            else:
                comando = "mensagem()"
                dados = mensagem[:]
                tam = len(dados)

            comunicacao = protocoloComunicacao(tam, self.username, comando, dados)

            self.clientSocket.send(comunicacao.encode('utf-8'))
