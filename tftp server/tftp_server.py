#Make sure to replace '/path/to/tftp/root' with the actual path to the directory you want to serve via TFTP.
# To create a TFTP server in Python, you need to use a library that supports TFTP :
#pip3 install tftpy
from tftpy import TftpServer

server = TftpServer('path/to/tftp/root')

try:
    server.listen('0.0.0.0', 69)
except KeyboardInterrupt:
    pass
