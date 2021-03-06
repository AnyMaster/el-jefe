import socket

#settings for xml server
LOGHOST = ([(s.connect(('1.1.1.1', 0)), s.getsockname()[0], s.close())
            for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])
LOGPORT = 5555

#logging options
LOGGING_FILENAME="ElJefeXMLServer.log"
LOGGING_LEVEL="INFO"

#be sure to use your own certs
KEYFILE='certs/server.key'
CERTFILE='certs/server.pem'
CA_CERTFILE='certs/cacert.pem'

# Email alert settings
ENABLE_EMAIL_ALERTS = False
EMAIL_ACCOUNT = "youraccount@domainthatshouldreallybeset.com" 
SMTP_SERVER = "127.0.0.1"
SMTP_PORT = 25
