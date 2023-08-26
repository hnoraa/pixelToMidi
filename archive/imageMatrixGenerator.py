from os import path
from sys import platform
from PIL import Image
from numpy import asarray


class ImageMatrixGenerator():
    def __init__(self, filePath):
        self.filePath = filePath
        self.extensions = ["bmp", "png"]
        self.error = False
        self.acceptableFileFormat = True

        self.__checkExt()
        if not self.acceptableFileFormat:
            raise Exception(f"Incorrect file format: {self.filePath}")

        self.__checkPath()
        if self.error:
            raise Exception(f"Image not found: {self.filePath}")

        try:
            self.image = Image.open(self.filePath)
        except:
            raise Exception(f"Cannot load image: {self.filePath}")

        self.__getArray()
        
    def __checkExt(self):
        fileParts = self.filePath.split(".")
        if not fileParts[len(fileParts)-1].lower() in self.extensions:
            self.acceptableFileFormat = False
        
    def __checkPath(self):
        if "\\" in self.filePath or platform == "win32" or self.filePath:
            self.filePath.replace("\\","/")

        if path.exists(self.filePath):
            self.fileName, self.fileExtension = path.basename(self.filePath).split('.')
        else:
            self.error = True
            raise FileNotFoundError(f"Image not found: {self.filePath}")

    def __getArray(self):
        self.imageMatrix = asarray(self.image)
