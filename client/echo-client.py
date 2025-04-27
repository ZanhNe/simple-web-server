import sys
import socket

if len(sys.argv) != 4:
    print("please follow this format on terminal: python 'entry' 'server_host' 'server_port' 'filename' ")
    sys.exit()

[entry, server_host, server_port, filename] = sys.argv


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_host, int(server_port)))

message = (
    f"GET /{filename} HTTP/1.0\r\n",
    "\r\n"
)
sock.sendall(''.join(message).encode())

response = sock.recv(1024)

print(response.decode())