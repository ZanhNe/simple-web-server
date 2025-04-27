from Server import Server
import signal

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 6789

server = Server()
signal.signal(signal.SIGINT, server.signal)

if __name__ == '__main__':
    server.run_server(SERVER_HOST, SERVER_PORT)