""" import socket
import time
from datetime import datetime
import uuid

#client _haifa al ashkar

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

#to send the request (client - server)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 1234

#we get the ip of the current device
i = socket.gethostname()
ip = socket.gethostbyname(i)

#we connect to server
client.connect((ip,port))

#the ip of the website needed (final ip)
ipf = input("Enter the IP needed: ")

#we formulate the get request
request = "GET / HTTP/1.1\r\nHost: " + ipf + "\r\n\r\n"

print(request)
#start time
ST = time.time()

#we encode the message to be able to send it
client.send(request.encode())
print("Requested to get data from the website with the IP: ", ipf, "At time: ",current_time)

#we wait for the response and decode it when we recieve it 
response = client.recv(4096).decode()
#end time
END = time.time()

a = END - ST
print(response)
print(f"RTT is: {a} seconds")
print("\nM")
print ("The formatted MAC address is : ", end="")
print (':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
for elements in range(0,2*6,2)][::-1]))

client.close() """