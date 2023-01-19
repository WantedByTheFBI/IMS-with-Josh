import logging
import threading
import socket
def readincomingtext(name): #a function that is basically instructions for the thread to recieve and log messages from the server
    while True:
        data = client.recv(buffer_size)  #makes the variable "data" equal to the data from the client up to the size of the buffer
        data = data.decode()  #decodes the data from it's byte typing into a string
        logging.info("s% i - From Client: " + data, name)  #logs the data with the timestamp of when it was logged

buffer_size = 1024  #the limit of how much data we will recieve from the client at once

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #creates a socket using the default parameters
mysocket.bind((socket.gethostname(), 9447))   #binds the created socket to this location
mysocket.listen()  #the socket waiting for a client to make a connection

(client, (ip, port)) = mysocket.accept()  #records the client and their ip and port info once they've connected
client.send(b"Connection with Server Established")  #sends a message to the client telling them that connection has been established

format = "%(asctime)s: %(message)s"  #is the format for the logging data
logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")  #configures how we log data

x = threading.Thread(target=readincomingtext, args=(1,), daemon=True)  #creates the thread object that will run our readincomingtext function
#takes in the arguement (1,) because otherwise the function take in no parameters and gets annoyed, and then sets it to be
# a daemon thread so that the thread will close when the rest of the code does
x.start()  #tells the thread to start doing it's job

print("\nEnter a message, or [close] to break connection.\n")
print("\n")
while True:
    message = input().encode("utf-8")  #encodes the message into data to be send
    if message.decode() == "[close]":
        client.send(("The Server has closed the application.").encode("utf-8"))  #tells the client we are closing the application
        break
    client.send(message)
mysocket.close()  #closes the socket