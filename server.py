import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
buffer_size = 1024
text = "no"
mysocket.bind(('127.0.0.1', 9876))
x = 0

mysocket.listen(1)
(client, (ip,port)) = mysocket.accept()
print(client, port)
client.send(b"knock knock knock, I'm the server")
while True:
    message = input("What would you like to send? ")
    client.send(message)
    data = client.recv(buffer_size)
    print(data.decode())
    break
mysocket.close()
