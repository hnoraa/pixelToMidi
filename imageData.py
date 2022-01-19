from PIL import Image
from numpy import asarray


class ImageData():
    def __init__(self, file_name):
        self.file_name = file_name
        self.image = Image.open(self.file_name)
        self.pixel_array = asarray(self.image)
