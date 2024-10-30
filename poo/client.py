import socket


class Cliente:

    def __init__(
        self,
        host: str = 'localhost',
        port: int = 12345,
    ):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    def run(self):
        while True:
            key = input('Input the id to retrieve data (or exit to leave): ')

            if not key:
                continue

            if key.lower() == 'exit':
                print('Leaving...')
                break

            self.client.send(key.encode())
            response = self.client.recv(1024)
            print(f'\nResponse from server: {response.decode()}\n')

        self.client.close()
    
if __name__ == '__main__':
    cliente = Cliente()
    cliente.run()
