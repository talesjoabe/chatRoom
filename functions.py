from termcolor import colored

# Print when Client enter on the chatRoom
def clientOn(username):
    userOn= username.decode('utf-8')[2:len(username)-1]
    print(colored(userOn, 'green'), "entrou na sala")

# Add ClientInfo in list
def addList(clients,username, ip, port):
    clientName = username.decode('utf-8')[2:len(username)-1]
    clientInfo = [clientName, ip, port]
    clients.append(clientInfo)
    print(clients)
