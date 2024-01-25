import socket, json

host = socket.gethostbyname(socket.gethostname()) # Deve ter o mesmo IP do servidor.
port = 55555


def main():

    tecnico = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        tecnico.connect((host, port))
    except:                                                        #Partes da comunicação entre o servidor
        return print('\nNão foi possívvel se conectar ao servidor!\n')

    print('Bem vindo ao projeto de Abertura de Chamados')
    print('Este é um ambiente para técnicos.\n')

    print('Chamados abertos: \n')

    while True:
        msg = tecnico.recv(2048).decode()        #Partes da comunicação entre o servidor
        msg = eval(msg)

        with open("bancodados.json", "w") as dAtua:
            dAtua.write(json.dumps(msg, indent=2))
                                                    #Partes da comunicação entre o arquivo json e o código
        with open("bancodados.json", "r") as dAtua2:
            msg2 = json.load(dAtua2)

        for i in msg2:
                nome =  msg2["Nome"]
                cpf = msg2["CPF"]
                cidade = msg2["Cidade"]
                telefone = msg2["Telefone"]
                setor = msg2["Setor"]
                email = msg2["Email"]
                situacao = msg2["Situacao"]
        
        print('Nome do solicitante: {}\n'.format(nome) + 
                'CPF: {}\n'.format(cpf) +
                'Cidade: {}\n'.format(cidade) +
                'Telefone: {}\n'.format(telefone) +
                'Setor: {}\n'.format(setor) + 
                'E-mail: {}\n'.format(email) +
                'Descrição do chamado: {}\n'.format(situacao))

main()
