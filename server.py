import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
buffer_size = 1024
text = "no"
mysocket.bind((socket.gethostname(), 9440))
mysocket.listen()
(client, (ip,port)) = mysocket.accept()
print(client, port)
client.send(b"knock knock knock, I'm the server")
while True:
    message = input("What would you like to send?(or enter [close] if you want to stop messaging: ").encode("utf-8")
    if message.decode() == "[close]":
        break
    client.send(message)
    data = client.recv(buffer_size)
    print("received data:")
mysocket.close()
