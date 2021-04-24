import socket,threading,sys,argparse
global s

parser=argparse.ArgumentParser()
parser.add_argument("-i",dest="host",help="Host address...",default='0.0.0.0',type=str)
parser.add_argument("-p",dest="port",help="Port...",default=4444,type=int)
p=parser.parse_args()

host= p.host
port=p.port

def rcv():
  global s
  while True:
    b=s.recv(2000)
    if b!=b"":
      print(b.decode("UTF-8"))
    
def snd():
  global s
  while True:
    msg=bytes(input()+'\n','utf-8')  
    s.send(msg)
      

try:
  s=socket.socket()
  s.connect((host,port))
  print("(+) Connected... \n")
  t1=threading.Thread(target=rcv)
  t2=threading.Thread(target=snd)
  #t3=threading.Thread(target=acp,args=(s,))	  
  t1.start()
  t2.start()
  
  
except Exception as e:
  print(e)
  con.close()

