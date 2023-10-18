# Python code for a simple chat program relying on TCP as the transport protocol (client)

import socket

# function to send and receive messages
def chat(sock, name, name2):
    while True:
        # if it's the client's turn to send a message
        if name:
            message = input(name+": ")
            sock.send(message.encode())
            print("Sent message to server")
            if message.lower() == "bye":
                break
            response = sock.recv(1024).decode()
            print(name2+":", response)
            if response.lower() == "bye":
                break

# create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

# read user 1's name from the input console and store it in a variable
name1 = input("Enter your name: ")

# connect to the server and send user 1's name
server_address = ('localhost', 10000)
sock.connect(server_address)
print("Connected to server")
sock.send(name1.encode())
print("Sent your name to server")

# receive user 2's name from the server
data = sock.recv(1024).decode()
name2 = data
print("Received user 2's name from server")

# start chatting in turn
print("Chat started")
print(name1, "goes first")
chat(sock, name1, name2)

# close the connection
sock.close()
print("Connection closed")