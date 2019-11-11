
'''
    A chave é o item 1 da lista retornada

    1. Identificação que um novo usuário entrou na sala de bate papo
    2. Identificação que um usuário saiu da sala de bate papo
'''
# Print when Client enter on the chatRoom
def clientOn(username):
    userOn= username.decode('utf-8')[2:len(username)-1]
    return '1'+userOn

def clientOff(username):
    userOn= username.decode('utf-8')[2:len(username)-1]
    return '2'+userOff

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
    print(listSockets)

def remListSockets(listSockets, Socket):
    listSockets.pop(Socket)

def protocoloComunicacao(tam, nickname, comando, dados):
    if(tam<100 and len(nickname.encode('utf-8'))<=16 and len(comando.encode('utf-8')<=8)):
        s= str(tam)+'\0'+nickname+'\0'+comando+'\0'+dados+'\0'
        return s
    else:
        return '-1'
