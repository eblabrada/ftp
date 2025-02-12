import socket
import ssl
from utils import log, from_json, to_json

class connection:
    host: str
    port: int
    client_socket: socket
    ssl_socket: ssl.SSLSocket
    
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        
    def connect(self):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((self.host, self.port))
            
            
            # data = from_json(client_socket.recv(1024))
            resp = client_socket.recv(1024).decode().strip()
            data = {
                'status_code': resp.split(' ')[0],
                'message': ' '.join(resp.split(' ')[1:])
            }
            
            print(data)
            
            if(data['status_code'] != '220'):
                return False
            
            return True
        except Exception as e:
            log(f'Error connecting to server: {e}')
            return False
        
    def send(self, data: bytes):
        self.ssl_socket.sendall(data)
        return self.ssl_socket.recv(1024)
    
    def send_file(self, filepath: str):
        pointer = open(filepath, 'rb')
        self.ssl_socket.sendfile(pointer)
        pointer.close()
            