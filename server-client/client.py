import socket
import imageReader


class MyPhotosClient:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 4459
        self.addr = (self.host, self.port)
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.imageSize = 4500
        self.image_reader = imageReader.ImgReader()

    def connect(self):
        self.clientSocket.connect(self.addr)

    def receive_image(self):
        image = self.clientSocket.recv(self.imageSize)
        deserialized_image = self.image_reader.deserialize_image(image)
        self.image_reader.show_image(deserialized_image)


if __name__ == "__main__":
    client = MyPhotosClient()
    client.connect()
    client.receive_image()
