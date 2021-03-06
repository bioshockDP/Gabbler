import socket
import sys
import time
from _thread import *
from src.server_utils.answers_for_client import get_answer

# creating socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.0.104', 2422)
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
            else:
                answer = get_answer(data)
                conn.sendall(answer.encode())

    finally:
        time.sleep(1)
        print("connection closed", file=sys.stderr)
        connection.close()


# loop for accepting client
while True:
    connection, client_address = s.accept()
    connection.sendall("(якесь вітання)".encode())
    print('connection from', client_address, file=sys.stderr)
    start_new_thread(client_thread, (connection,))
