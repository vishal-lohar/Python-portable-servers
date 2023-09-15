# Replace 'ShareName' with the desired name for the shared folder 
# and '/path/to/shared/folder' with the actual path to the directory you want to share.
from impacket.smbserver import SimpleSMBServer

server = SimpleSMBServer()
server.addShare('ShareName', '/path/to/shared/folder')
server.start()
