import socket
server=socket.socket(socket
                     .AF_INET,socket.SOCK_STREAM)
ip=socket.gethostbyname(socket.gethostname())
print(ip)
port=7777
server.bind((ip,port))
server.listen()
i=0
while i==0:
    c_socket,c_ip=server.accept()
    print(f"{c_ip} connected")
    while 1:
        msg=c_socket.recv(1024)
        print(msg)
        if msg==b"send":
    
            c_socket.send("sending".encode("utf-8"))
            with open("hi.txt","r") as op:
                c_socket.send(op.read().encode("utf-8"))
        elif msg==b"close":

            c_socket.close()
    i+=1
    
