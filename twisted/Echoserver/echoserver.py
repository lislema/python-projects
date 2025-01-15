from twisted.internet import reactor, protocol

class EchoServerProtocol(protocol.Protocol):
    def dataReceived(self, data):
        """Called when data is received from the client."""
        print(f"Server received: {data.decode('utf-8')}")
        self.transport.write(data)  # Echo the data back to the client

class EchoServerFactory(protocol.Factory):
    def buildProtocol(self, addr):
        """Create and return an EchoServerProtocol instance."""
        return EchoServerProtocol()

if __name__ == "__main__":
    port = 12345  # Port to listen on
    reactor.listenTCP(port, EchoServerFactory())
    print(f"Echo server is running on port {port}")
    reactor.run()