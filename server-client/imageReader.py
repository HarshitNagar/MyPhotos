import pickle
from PIL import Image


class ImgReader:
    def __init__(self):
        self.img_name = "01.png"
        # self.base_path = "/Users/harshit/gitrepos/personal/MyPhotos/imageReader/image-store"
        self.base_path = "/usr/src/MyPhotos/imageReader/image-store"
    def read_image(self):
        im = Image.open(self.base_path+"/"+self.img_name)
        return {
            'pixels': im.tobytes(),
            'size': im.size,
            'mode': im.mode,
        }

    def show_image(self, image):
        im = Image.frombytes(image['mode'], image['size'], image['pixels'])
        im.show()

    def serialize_image(self, image):
        return pickle.dumps(image)

    def deserialize_image(self, serialised_image):
        return pickle.loads(serialised_image)
