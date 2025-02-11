import socket
from utils import log, from_json, to_json

class connection:
    host: str
    port: int
    client_socket: socket
    
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        
    def connect(self):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((self.host, self.port))
            
            data = client_socket.recv(1024)
            print(data)
            
            if(data['status_code'] != '220'):
                return False
            
            self.client_socket = client_socket
            return True
        except Exception as e:
            log(f'Error connecting to server: {e} {data}')
            return False
        
    def send(self, data: bytes):
        self.client_socket.sendall(data)
        return self.client_socket.recv(1024)
    
    def send_file(self, filepath: str):
        pointer = open(filepath, 'rb')
        self.client_socket.sendfile(pointer)
        pointer.close()
            