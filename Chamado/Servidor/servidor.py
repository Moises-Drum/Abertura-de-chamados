import threading
import socket

host = socket.gethostbyname(socket.gethostname())
port = 55555

clients = []

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



    try:
        server.bind ((host , port))
        server.listen(10)
        print('\nServidor {} iniciado. Aguardando conexões...'.format(host))
    except:
        return print('\nNão foi possível iniciar o servidor!\n')

    #loop esperando conexões
    while True:
        clientV, addr = server.accept()
        clients.append(clientV)

        thread = threading.Thread(target=messagesTreatment, args=[clientV])
        thread.start()
        print(f"[conexoes ativas] {threading.active_count() - 1}")

#função que recebe as mensagens
def messagesTreatment(clientV):
    while True:
        msg = clientV.recv(2048)
        broadcast(msg, clientV)


def broadcast(msg, clientV):
    for clientItem in clients:
        if clientItem != clientV:
            clientItem.send(msg)
                
main()

