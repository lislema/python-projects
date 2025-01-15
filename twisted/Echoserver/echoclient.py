from twisted.internet import reactor, protocol

class EchoClientProtocol(protocol.Protocol):
    def connectionMade(self):
        """Called when a connection is made to the server."""
        message = "Hello, Echo Server!"
        print(f"Client sending: {message}")
        self.transport.write(message.encode('utf-8'))  # Send data to the server

    def dataReceived(self, data):
        """Called when data is received from the server."""
        print(f"Client received: {data.decode('utf-8')}")
        self.transport.loseConnection()  # Close the connection after receiving data

class EchoClientFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        """Create and return an EchoClientProtocol instance."""
        return EchoClientProtocol()

    def clientConnectionFailed(self, connector, reason):
        print(f"Connection failed: {reason.getErrorMessage()}")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost.")
        reactor.stop()

if __name__ == "__main__":
    host = "localhost"
    port = 12345  # Port the server is listening on
    reactor.connectTCP(host, port, EchoClientFactory())
    reactor.run()

