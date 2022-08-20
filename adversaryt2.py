import socket
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
s.bind(('127.0.0.1', 0))
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
i=1
while True:
   print "number of this message: %s",i
   data, addr =s.recvfrom(65565)
   print data
   i+=1