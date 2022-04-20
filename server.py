from socket import *
from tkinter import *
import threading

import time


def client_messages():
    time.sleep(30)
    while True:
        sentence = connectionSocket.recv(1024).decode()
        client_reply.insert(END,"Client:"+sentence)

        
        
        
def server_messages():
        #server_message=input("Enter message")
        server_msg=str(Server_message.get("1.0",END))
        client_reply.insert(END,"Server:"+server_msg)
        connectionSocket.send(server_msg.encode())
        
        



def delete_text():
    client_reply.delete("1.0", "end")
    
    
def create_connection(portn):
    global connectionSocket
    ip="127.0.0.1"
    Port=portn
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind((ip,Port))
    serverSocket.listen(1)
    connectionSocket, addr = serverSocket.accept()
    time.sleep(10)
    print(f"Connestion established : {addr[0]}:{addr[1]}")
    
    
    
def initialize_server():
    

    Port = int(port_no.get())
    create_connection(Port)
    
   


window =Tk()

connectionSocket=socket()

window.title("LAN MESSANGER-Server")
window.minsize(width=500,height=600)
window.config(padx=50,bg='#B7CADB')

# input port number
my_label=Label(text="Port Number:",font=("Arial",15),bg='#B7CADB')
my_label.place(rely=0.03,x=-40,anchor="nw")

#port number text box
port_no=Entry(width=12,font=("Arial",15))
port_no.place(relx=0.25,rely=0.03,anchor="nw")

#Button field
button=Button(text="Start Listening",command=initialize_server,width=20,height=1,bg='#6FB2D2')
button.place(relx=1.01,rely=0.03,anchor="ne")

#Button field
button=Button(text="Clear Chat",command=delete_text,width=20,height=1,bg='#6FB2D2')
button.place(relx=1.01,rely=0.1,anchor="ne")

#Output field
client_reply=Text(height=20,width=50,bg='#B7CADB')
client_reply.insert(END,"")
client_reply.place(relx=0.5,rely=0.45,anchor="center")


#Output field
Server_message=Text(height=5,width=50)
Server_message.insert(END,"")
Server_message.place(relx=0.5,rely=0.82,anchor="center")


#Button field
button=Button(text="Send Message",command=server_messages,width=20,height=1,bg='#6FB2D2')
button.place(relx=1.01,rely=0.95,anchor="se")


thread1 = threading.Thread(target=client_messages, args=())
thread1.start()

window.mainloop()


