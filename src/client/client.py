import socket

# os.system("python3.5 server_example.py &")
# time.sleep(2)

# creating socket and connecting to server
server_address = ('localhost', 2422)
sock = socket.socket()
sock.connect(server_address)

print("answer from server: {}".format(sock.recv(1024).decode()))

while True:
    message = input('enter your message: ')
    if message == 'exit':
        sock.close()
        break

    sock.sendall(message.encode())

    data = sock.recv(1024).decode()
    if data:
        print('answer from server: %s' % data)