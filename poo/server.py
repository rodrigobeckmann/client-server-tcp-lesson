import socket
import threading


class Servidor:

    DATA = {
        1: 'Data associated with key 1',
        2: 'Data associated with key 2',
        3: 'Data associated with key 3',
        4: 'Data associated with key 4',
        5: 'Data associated with key 5',
    }

    def __init__(
        self,
        host: str = 'localhost',
        port: int = 12345,
    ):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()
        print(f'Server listening on {self.host}:{self.port}')

    def __handle_client(self, client, address):
        print(f'New connection from {address}')
        while True:
            data = client.recv(1024)
            if not data:
                break

            try:
                key = int(data.decode())
            except ValueError:
                print(f'Invalid key received from {address}')
                client.send('Key should be an integer'.encode())
                continue

            response = self.DATA.get(key, 'Key not found')
            client.send(response.encode())

        client.close()
        print(f'Connection with {address} closed')
    
    def run(self):
        while True:
            client, address = self.server.accept()
            thread = threading.Thread(
                target=self.__handle_client,
                args=(client, address),
            )
            thread.start()

if __name__ == '__main__':
    servidor = Servidor()
    servidor.run()
