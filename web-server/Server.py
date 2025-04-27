from socket import *
import time
import os
import threading

base_dir = os.path.dirname(__file__)

class Server:
    def __init__(self):
        self.server = socket(AF_INET, SOCK_STREAM)
        self.is_running = True
    def run_server(self, host, port):
        self.server.bind((host, port))
        self.server.settimeout(1)
        self.server.listen(5)
        print(f"Server running on http://{host}:{port}")

        try:
            while self.is_running:
                try:
                    connection, addr = self.server.accept()
                    thread = threading.Thread(target=self.seperate_thread, args=(connection, addr,), daemon=True)
                    thread.start()

                except timeout:
                    continue
        except Exception as e:
            print(e)
        finally:
            self.shutdown()
            print("Server has closed")

    def seperate_thread(self, connection: socket, addr: tuple):
        request = connection.recv(1024) 
        response = self.resolve_request(request)
        if response:
            time.sleep(5)
            connection.sendall(response)
        connection.close()

    def shutdown(self):
        self.server.close()

    def signal(self, sig, frame):
        self.is_running = False
    
    def resolve_request(self, request: bytes):
        decode_request = request.decode()
        [method, uri, *rest] = decode_request.split(' ')
        if method == 'GET':
            if 'static' in uri:
                try:
                    with open(f"{base_dir}{uri.replace('/', '\\')}", 'r') as file:
                        static_content = file.read()
                    type = ""
                    if uri.endswith('.css'):
                        type = "text/css"
                    elif uri.endswith('.js'):
                        type = "text/javascript"
                    
                    response = (
                        "HTTP/1.1 200 OK\r\n",
                        f"Content-Type: {type};charset=utf-8\r\n",
                        f"Content-Length: {len(static_content.encode())}\r\n",
                        "Connection: close\r\n",
                        "\r\n",
                        f"{static_content}"
                    )

                    return ''.join(response).encode()
                except FileNotFoundError:
                    response = (
                        "HTTP/1.1 404 Not Found\r\n,"
                        "Connection: close\r\n",
                        "\r\n"
                    )
                    return ''.join(response).encode()
            elif uri == '/about.html':
                with open(f"{base_dir}\\templates\\{uri.replace('/', '\\')}", 'r', encoding='utf-8') as file:
                    html_content = file.read()
                response = (
                    "HTTP/1.1 200 OK\r\n",
                    "Content-Type: text/html\r\n",
                    f"Content-Length: {len(html_content.encode())}\r\n",
                    "Connection: close\r\n",
                    "\r\n",
                    f"{html_content}"
                )
                return ''.join(response).encode()
            elif uri == '/':
                with open(f"{base_dir}\\templates\\{uri.replace('/', '\\')}home.html", 'r', encoding='utf-8') as file:
                    html_content = file.read()
                response = (
                    "HTTP/1.1 200 OK\r\n",
                    "Content-Type: text/html\r\n",
                    f"Content-Length: {len(html_content.encode())}",
                    "Connection: close\r\n",
                    "\r\n",
                    f"{html_content}"
                )
                return ''.join(response).encode()
            else:
                response = (
                        "HTTP/1.1 404 Not Found\r\n,"
                        "Connection: close\r\n",
                        "\r\n"
                    )
                return ''.join(response).encode()
        else:
            return None
                


            
        
            
            

                

        

    

