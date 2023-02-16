""" #server _haifa al ashkar

import socket
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

#to recieve the request (client - server)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 1234
#we get the ip of the current device 
i = socket.gethostname()
ip = socket.gethostbyname(i)

server.bind((ip,port))
server.listen(1)

#to connect to the website (server-proxy server)
proxy = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

while True: #we recieve a message, accept it and decode it
    client, address = server.accept()
    mes = client.recv(4096)
    mes = mes.decode()

    #we print a message describing this request with the IP and exact time of the request
    print(f"Request received: {mes}")
    print("\nAt time: ",current_time)

    #we try to retrieve the IP from the message sent by the client
    messplit = mes.split()
    ipf = messplit[4]

    #we connect to the server responsible to bring the data needed through the ip found
    proxy.connect((ipf, 80))

    #we encode message to send to 2nd server
    proxy.send(mes.encode())

    #we print a message with exact time of the actual request
    print("\nClient request sent to server at time: ", current_time)


    reply = proxy.recv(4096).decode()

    #we print a message that the response was received with the exact time 
    print("\nResponse received from server at: ", current_time)
    proxy.close()

    break

#we finally send the response to client 
client.send(reply.encode())


#we print a message that the response was sent with the exact time
print("\nResponse sent from proxy server to client at time: ",current_time)
server.close() """