import socket,threading,sys,argparse
global lst,s

parser=argparse.ArgumentParser()
parser.add_argument("-i",dest="host",help="Host address...",default='0.0.0.0',type=str)
parser.add_argument("-p",dest="port",help="Port...",default=4444,type=int)
p=parser.parse_args()

host= p.host
port=p.port

def rcv():
  global lst
  while True:
    for i in lst:
      b=i.recv(2000)
      if b!=b"":
        print(b.decode("UTF-8"))
    
def snd():
  global lst
  while True:
    msg=bytes(input()+'\n','utf-8')  
    for s in lst:
      s.send(msg)
      
def acp(s):
  global lst
  while True:
    con,addr=s.accept()
    lst.append(con)

lst=[]
try:
  s=socket.socket()
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.bind((host,port))
  s.listen(3)
  print("(+) Server Created... \n")
  t1=threading.Thread(target=rcv)
  t2=threading.Thread(target=snd)
  t3=threading.Thread(target=acp,args=(s,))	  
  t1.start()
  t2.start()
  t3.start()
  
  
except Exception as e:
  print(e)
  con.close()

'''s.listen()
  	#(con,addr)=s.accept()
  	#lst.append(con)
  	#t1=threading.Thread(target=rcv,args=(s,))
  	while True:
  	  (con,addr)=s.accept()
  	  lst.append(con)
  	  msg=bytes('< {addr} connected > \n','utf-8')
  	  for i in lst:
  	    i.send(msg)'''
  	