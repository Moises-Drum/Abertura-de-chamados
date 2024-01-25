import socket, json

host = socket.gethostbyname(socket.gethostname())  # Deve ter o mesmo ip do servidor.
port = 55555


def main():
    # Comuncação entre o servidor
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        cliente.connect((host, port))
    except:  # Partes da comunicação entre o servidor
        return print('\nNão foi possívvel se conectar ao servidor!\n')

    print('Bem vindo ao projeto Abertura de Chamados\n' +
          'Este é um ambiente para clientes.\n')


    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    cidade = input("Digite o nome da cidade: ")
    telefone = input("Digite o telefone: ")
    setor = input("Digite o setor: ")
    email = input("Digite o endereço de e-mail: ")
    situacao = input("Informe o ocorrido: ")

    print("\n===== INFORMAÇÕES DO CHAMADO =====\n"
          "Solicitante : " + nome + "\n" +
          "CPF: " + cpf + "\n" +
          "cidade: " + cidade + "\n"+
          "Telefone: " + telefone + "\n"+
          "Setor: " + setor + "\n"+
          "E-mail: " + email + "\n"+
          "Descrição do ocorrido: " + situacao + "\n")


    dados = """
        {
            "Nome": "nome",
            "CPF": "cpf",
            "Cidade": "cidade",
            "Telefone": "tel",
            "Setor": "setor",
            "Email": "email",
            "Situacao": "situacao"
        }
        """

    info = json.loads(dados)

    for i in info:
        if i == "Nome":
            info[i] = nome
        elif i == "CPF":
            info[i] = cpf
        elif i == "Cidade":
            info[i] = cidade
        elif i == "Telefone":
            info[i] = telefone
        elif i == "Setor":
            info[i] = setor
        elif i == "Email":
            info[i] = email
        elif i == "Situacao":
            info[i] = situacao

    with open("bancodados.json", "w") as dAtua:
        dAtua.write(json.dumps(info, indent=2))
        # Partes da comunicação do arquivo json e o código
    with open("bancodados.json") as dAtua2:
        msg = json.load(dAtua2)

    cliente.send(f' {msg}'.encode())  # Envio de dados para o servidor

    print("Chamado aberto.")


main()
