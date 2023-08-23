from socket import *
import datetime
import sys
# declare the server port
serverPort = 2000
serverSocket = socket(AF_INET, SOCK_STREAM)

# call local machine and the port
serverSocket.bind(('', serverPort))

# the server socket will listen for a connection
serverSocket.listen(1)
print('Web server is on port', serverPort)

while True:
    # Establish the connection
    print('Ready to serve...')

    # accepting connection from the client
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]

        # We have to read the path from the second character due to /
        f = open(filename[1:])

        # store the contents of file in temporary buffer
        outputdata = f.read()
        print(outputdata)
        # print out to console what the HTML file says

        # Send the  HTTP header line into connection socket
        connectionSocket.send("\nHTTP/1.1 200 OK\n\n".encode())

        # send the contents of file to connection socket
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

    except IOError:
        # send the HTTP response message if file not found for errors
        connectionSocket.send("\nHTTP/1.1 Error 404: FILE NOT FOUND\n\n".encode())
        # print to webpag HTML 404 NOT FOUND in the event of wrong url
        connectionSocket.send("<html><head></head><body><hl>404 NOT FOUND</hl><body></html>\r\n.".encode())

        # close the client connection socket
        connectionSocket.close()
# close the serversocket
    serverSocket.close()
    # close program
    sys.exit()
