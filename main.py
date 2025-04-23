import socket


SERVER_HOST = '127.0.0.1'
SERVER_PORT = 6789

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(1)
    conn, addr = s.accept()
    message = conn.recv(1024)
    print(message.decode())
    with open('templates/HelloWorld.html', 'r') as file:
        html_content = file.read()
    
    response = f"""
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: {len(html_content.encode())}
Connection: close

{html_content}
"""
    conn.sendall(response.encode())
    conn.close()
    



