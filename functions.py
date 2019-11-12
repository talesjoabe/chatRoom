
'''
    A chave é o item 1 da lista retornada

    1. Identificação que um novo usuário entrou na sala de bate papo
    2. Identificação que um usuário saiu da sala de bate papo
'''
# Print when Client enter on the chatRoom
def clientOn(username):
    userOn= username.decode('utf-8')[2:len(username)-1]
    return '1'+'\0'+userOn
    #return '1'+userOn

# Add ClientInfo in list
def addListClient(clients,username, ip, port):
    clientName = username.decode('utf-8')[2:len(username)-1]
    clientInfo = [clientName, ip, port]
    clients.append(clientInfo)

def remListClient(clients,username,ip,port):
    clientName = username.decode('utf-8')[2:len(username)-1]
    clientInfo = [clientName, ip, port]
    clients.pop(clientInfo)

def addListSockets(listSockets, Socket):
    listSockets.append(Socket)

def remListSockets(listSockets, indiceSocket):
    listSockets.pop(indiceSocket)

def protocoloComunicacao(tam, nickname, comando, dados):
    if(tam<100 and len(nickname.encode('utf-8'))<=16 and len(comando.encode('utf-8'))<=25):
        s= str(tam)+'\0'+nickname+'\0'+comando+'\0'+str(dados)
        return s
    else:
        return '-1'

def comandos(protocolo):
    protocolo = protocolo.split('\0')
    tam = protocolo[0]
    nickname = protocolo[1]
    comando = protocolo[2]
    dados = protocolo[3]
    #print(dados)
    indiceClient=0

    if(comando == 'entrar()'):
        return '1'+'\0'+nickname
    if(comando == 'sair()'):
        return '2'+'\0'+nickname
    elif(comando == 'lista()'):
        return '3'+'\0'+nickname+'\0'+str(dados)
    elif(comando == 'mensagem()'):
        return '4'+'\0'+nickname+'\0'+dados
    else:
        # (5) + REMETENTE + DESTINATARIO + MSG
        return '5'+'\0'+nickname+'\0'+comando[8:len(comando)]+'\0'+dados
