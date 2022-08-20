from __future__ import unicode_literals
import socket,sys
from functools import reduce
from io import open
def sxor(s1,s2):   
    # convert strings to a list of character pair tuples
    # go through each tuple, converting them to ASCII code (ord)
    # perform exclusive or on the ASCII code
    # then convert the result back to ASCII (chr)
    # merge the resulting array of characters as a string
    x = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))
    return x



sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 12321)
print >> sys.stderr, 'starting up on localhost port 12321 \n'
sock.bind(server_address)

j=0
i=1
while True:
    data, address = sock.recvfrom(100)
    print 'Recieved %s bytes from packet with sequence number:%s ' % (len(data),i)
    i+=1
    f = open("eServer.txt", "a",encoding="utf-8")
    f.write(data.decode())
    print data
    if data:
        sent = sock.sendto(data, address)
        print >> sys.stderr, 'sent %s bytes back to %s' % (sent, address)
    print '\n'
    j+=1