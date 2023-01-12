import socket
host = 
port = 9443
buffer_size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
while True:
    text = ("https://github.com/WantedByTheFBI/IMS-with-Josh")
    text = text.encode('utf-8')
    s.send(text)
    breakoff = input("would you like to stop sending and receiving messages? (yes or no): ")
    if breakoff.lower() == "yes":
        break
    data = s.recv(buffer_size)
    print("received data:", data)
s.close()
