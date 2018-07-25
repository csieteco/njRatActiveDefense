# -*- coding: utf-8 -*-
import socket

ccip = '34.201.243.2'
ccport = 2024

def detect():
  print 'Trying to connect... ' + ccip + ':' + str(ccport)
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((ccip, ccport))
  client.send(str(len('PLG'))+'\x00'+'PLG')
  print 'Waiting for the answer'
  response = client.recv(2048)
  try:
    delimiter = response.split('PLG')[1].split('\x00')[0]
    print "NjRAT answer found!!!, consider this delimiter: " + delimiter
  except:
    print "NjRAT answer not found. Response=(" + response + ")"

detect()
