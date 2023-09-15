from tftpy import TftpServer

server = TftpServer('/path/to/tftp/root')

try:
    server.listen('0.0.0.0', 69)
except KeyboardInterrupt:
    pass
