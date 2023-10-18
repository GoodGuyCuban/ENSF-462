# Python code for a simple chat program relying on TCP as the transport protocol (server)

import socket

# function to send and receive messages
def chat(sock, name, name2):
    while True:
        # if it's the server's turn to send a message
        if name:
            response = sock.recv(1024).decode()
            print(name2+":", response)
            if response.lower() == "bye":
                break
            message = input(name+": ")
            sock.send(message.encode())
            print("Sent message to client")
            if message.lower() == "bye":
                break

# create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

# read user 2's name from the input console and store it in a variable
name2 = input("Enter your name: ")

# bind the socket to a specific address and port
server_address = ('localhost', 10000)
sock.bind(server_address)
print("Socket bound to", server_address)

# listen for incoming connections
sock.listen(1)
print("Waiting for connection...")

# accept the first incoming connection and receive user 1's name
connection, client_address = sock.accept()
print("Connected to client")
data = connection.recv(1024).decode()
print("Received user 1's name from client")
name1 = data

# send user 2's name to the client
connection.send(name2.encode())
print("Sent your name to client")

# start chatting in turn
print("Chat started")
print(name1, "goes first")
chat(connection, name2, name1)

# close the connection
connection.close()
sock.close()
print("Connection closed")