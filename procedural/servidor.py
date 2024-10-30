## importa o módulo socket para trabalhar com conexões de rede
import socket
# importa o módulo threading para trabalhar com múltiplas conexões
import threading

# define um dicionário com os dados que serão enviados aos clientes
dados = {
    1: 'Dado associado à chave 1',
    2: 'Dado associado à chave 2',
    3: 'Dado associado à chave 3',
    4: 'Dado associado à chave 4',
    5: 'Dado associado à chave 5',
}

# define a função que será executada para tratar as requisições dos clientes
def tratamento_de_cliente(client_socket):
    print('Nova conexão')
    while True:
        # recebe a chave do cliente
        chave = client_socket.recv(1024)

        # verifica se a chave é vazia
        if not chave:
            ## se for vazia, encerra o loop
            break

        # decodifica a chave recebida
        # try e except são usados para tratar exceções
        # caso falhe a decodificação da chave
        # o código dentro do bloco except será executado ao invés de gerar um erro
        try:
            chave = chave.decode()
        except:
            # envia uma mensagem de erro ao cliente
            client_socket.send('Chave inválida'.encode())
            # pula para a próxima iteração do loop
            continue

        # verifica se a chave é um número inteiro
        try:
            # tenta converter a chave para um número inteiro
            chave = int(chave)
        except:
            # se não for possível converter a chave para um número inteiro
            # envia uma mensagem de erro ao cliente
            client_socket.send('Chave deve ser um número inteiro'.encode())
            # pula para a próxima iteração do loop
            continue
    
        # verifica se a chave está no dicionário de dados
        if chave in dados:
            # envia a resposta ao cliente
            client_socket.send(dados[chave].encode())
        else:
            # envia uma mensagem de erro ao cliente
            client_socket.send('Chave não encontrada'.encode())

    # fecha a conexão com o cliente
    client_socket.close()
    print('Conexão fechada')

# cria um objeto socket para o servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# define o endereço e a porta em que o servidor irá escutar
host = 'localhost'
port = 12345
# associa o servidor ao endereço e à porta
server_socket.bind((host, port))
# inicia a escuta do servidor
server_socket.listen()
print('Servidor escutando na porta 12345 e no endereço localhost')

# loop principal do servidor
while True:
    # aceita a conexão de um cliente
    client_socket, address = server_socket.accept()
    # cria uma nova thread para tratar a conexão com o cliente
    thread = threading.Thread(
        target=tratamento_de_cliente,
        args=(client_socket,)
    )
    thread.start()
