import socket
import sys
import time
from _thread import *

# creating socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.0.104', 2425)
s.bind(server_address)
print('server started', file=sys.stderr)
s.listen(10)


# function for each client
def client_thread(conn):
    try:
        while True:
            data = conn.recv(1024).decode()
            print('received "%s"' % data, file=sys.stderr)

            if data == "":
                print("client connection was closed")
                break
            elif data == 'Hello':
                conn.sendall('Hi'.encode())
            elif data == 'bye':
                conn.sendall('bye'.encode())
            elif data == 'How are you?':
                conn.sendall('good, thanks'.encode())
            else:
                conn.sendall('I don\'t understand you'.encode())

    finally:
        time.sleep(1)
        print("connection closed", file=sys.stderr)
        connection.close()

# loop for accepting client
while True:
    connection, client_address = s.accept()
    print('connection from', client_address, file=sys.stderr)
    start_new_thread(client_thread, (connection,))
