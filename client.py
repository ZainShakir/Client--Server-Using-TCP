from socket import *
from tkinter import *
import threading
import time

def client_messages():
    
    clientmsg=str(client_message.get("1.0",END))
    
    reply_box.insert(END,"Client:"+clientmsg)
    clientSocket.send(clientmsg.encode())
  
    
def server_messages():
    time.sleep(30)
    while True:
        modifiedSentence = clientSocket.recv(1024)
        servermsg=modifiedSentence.decode()
        reply_box.insert(END,"Server:"+servermsg)
        
        


    
def delete_text():
    reply_box.delete("1.0", "end")
    

    
def initialize_connection():
    global clientSocket
    ip=port_no.get()
    ip=ip.split(':')
    serverip=ip[0]
    serverPort=int(ip[1])
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverip,serverPort))
    print(type(clientSocket))


    

window =Tk()

clientSocket=socket()


window.title("LAN MESSANGER-Client")
window.minsize(width=500,height=600)
window.config(padx=50,bg='#B7CADB')

    # input port number
my_label=Label(text="Enter IP AND PORT:",font=("Arial",15),bg='#B7CADB')
my_label.place(rely=0.05,relx=0.24,anchor="center")

    #port number text box
port_no=Entry(width=20,font=("Arial",15))
port_no.place(relx=0.28,rely=0.12,anchor="center")

    #Button field
button=Button(text="Connect",command=initialize_connection,width=20,height=1,bg='#6FB2D2')
button.place(relx=1.01,rely=0.03,anchor="ne")

    #Button field
button=Button(text="Clear Chat",command=delete_text,width=20,height=1,bg='#6FB2D2')
button.place(relx=1.01,rely=0.1,anchor="ne")

    #Output field
reply_box=Text(height=20,width=50,bg='#B7CADB')
reply_box.insert(END,"")
reply_box.place(relx=0.5,rely=0.45,anchor="center")


    #Output field
client_message=Text(height=5,width=50)
client_message.insert(END,"")
client_message.place(relx=0.5,rely=0.82,anchor="center")


    #Button field
button=Button(text="Send Message",command=client_messages,width=20,height=1,bg='#6FB2D2')
button.place(relx=1.01,rely=0.95,anchor="se")

thread2 = threading.Thread(target=server_messages, args=())
thread2.start()

window.mainloop()
    


    


