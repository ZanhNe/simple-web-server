import socket
import os

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 6789

base_dir = os.path.dirname(__file__)
    

def init_server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen()
    return sock

def resolve_request(request: bytes):
    decode_request = request.decode()
    [method, uri, *rest] = decode_request.split(' ')
    print(method, uri)
    if method == 'GET':
        if uri == '/':
            with open('templates/HelloWorld.html', 'r', encoding='utf-8') as file:
                html_content = file.read()
            response = f"""
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: {len(html_content.encode())}
Connection: close

{html_content}
            """
            return response.encode()
        if uri.endswith('.css'):
            with open(f"{base_dir}{uri.replace('/', '\\')}", 'r') as file:
                css_content = file.read()
            response = f"""
HTTP/1.1 200 OK
Content-Type: text/css;charset=utf-8
Content-Length: {len(css_content.encode())}
Connection: close

{css_content}
            """
            return response.encode()
        return None

server = init_server(SERVER_HOST, SERVER_PORT)


while True:
    connection, addr = server.accept()

    request = connection.recv(1024)
    print(request)
    response = resolve_request(request)
    if response:
        connection.sendall(response)
    connection.close()


