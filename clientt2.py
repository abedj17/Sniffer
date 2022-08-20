import socket,sys,time
import ast
from functools import reduce

def sxor(s1,s2):   
    # convert strings to a list of character pair tuples
    # go through each tuple, converting them to ASCII code (ord)
    # perform exclusive or on the ASCII code
    # then convert the result back to ASCII (chr)
    # merge the resulting array of characters as a string
    x = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))
    return x


sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12321)
i = 1
f1 = open('poem.txt', 'r')
f2 = open('poem.txt', 'r')

fullText=[]
for line in f1:
    fullText.append(line)
f1.close()
e=reduce(sxor,fullText)
sentE = sock1.sendto(e, server_address)
print e
data1, server1 = sock1.recvfrom(100)
print data1


for line in f2:
    time.sleep(3)
    print 'Sequence number',i
    i += 1
    sent = sock2.sendto(line, server_address)
    data2, server2 = sock2.recvfrom(100)
    print 'From Server',data2

print sys.stderr, 'closing socket'
sock2.close()
sock1.close()