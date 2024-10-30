## importa o módulo socket para trabalhar com conexões de rede
import socket

## cria um objeto socket para o cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
## define o endereço e a porta do servidor
host = 'localhost'
port = 12345
## conecta o cliente ao servidor
client_socket.connect((host, port))

## loop principal do cliente
while True:
    ## solicita ao usuário que insira a chave
    chave = input('Insira a chave para recuperar o dado (ou exit para sair): ')
    
    ## verifica se a chave é vazia
    if not chave:
        ## se for vazia, pula para a próxima iteração do loop
        continue
    
    ## verifica se a chave é igual a 'exit'
    ## usando a função lower() para converter a chave para minúsculas
    if chave.lower() == 'exit':
        ## se for igual a 'exit', exibe uma mensagem e encerra o loop
        print('Saindo...')
        break
    
    ## envia a chave ao servidor
    client_socket.send(chave.encode())
    ## recebe a resposta do servidor
    resposta = client_socket.recv(1024)
    ## exibe a resposta na tela
    print(f'\nResposta do servidor: {resposta.decode()}\n')