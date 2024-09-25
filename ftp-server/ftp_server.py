# Modify User Credentials and Directory
# To create a FTP server in Python, you need to use a library that supports TFTP :
# pip3 install pyftpdlib
from pyftpdlib import servers
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer

# Define user credentials and directory
user = "user"
password = "12345"
directory = "/opt/nobody"

authorizer = DummyAuthorizer()
authorizer.add_user(user, password, directory, perm="elradfmw")
authorizer.add_anonymous("/opt/nobody", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server = servers.FTPServer(("0.0.0.0", 21), handler)
server.serve_forever()
