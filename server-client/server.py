import socket
import imageReader


class MyPhotosServer:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 4459
        self.addr = (self.host, self.port)
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.image_reader = imageReader.ImgReader()

    def bind(self):
        self.serverSocket.bind(self.addr)
        self.serverSocket.listen(1)

    def run(self):
        while True:
            client_socket, client_addr = self.serverSocket.accept()
            self.send_image(client_socket)

    def send_image(self, client_socket):
        image = self.image_reader.read_image()
        serialised_image = self.image_reader.serialize_image(image)
        client_socket.send(serialised_image)


if __name__ == "__main__":
    server = MyPhotosServer()
    server.bind()
    server.run()
