from PIL import Image

class ImageTest:
    def __init__(self, image_path) -> None:
        self.image_path = image_path
        self.img = None
        self.img_map = None

    def import_image(self):
        self.img = Image.open(self.image_path, 'r').convert('RGB')
        self.img_map = list(self.img.getdata())

    def describe(self):
        if self.img is not None:
            print(f'{self.image_path} details:')
            print(f'Image size (w, h):\t{self.img.width} x {self.img.height}')
            print(f'Image format:\t\t{self.img.format}\n')

    def test_image_array(self):
        if self.img is not None:
            # this might be useful...
            # this gets the image array (no numpy)
            self.test_array = list(self.img.getdata(band=None))
            print(len(self.test_array))
            #for x in self.test_array:
                #print(x)

            print(self.img.getdata())

            # this gets a flat version of the array
            # ex: if I have [(255, 210, 123, 55), (90, 190, 200, 100)] in the array
            # this flattens to [255 ,210, 123, 55, 90, 190, 200, 100]
            self.test_array_flat = [x for sets in self.test_array for x in sets]

            print(f'Length before flattening: {len(self.test_array)}')
            print(f'Flattened length: {len(self.test_array_flat)}\n')
    
    def peek_image_array(self):
        if self.img_map is not None:
            print(self.img_map[0])

    

if __name__ == '__main__':
    bmp = '.\\..\\images\\tester.bmp'
    bmp2 = '.\\..\\images\\tester1_autoBitDepth.bmp'
    png = '.\\..\\images\\tester.png'
    jpg = '.\\..\\images\\tester.jpg'

    bmpI = ImageTest(bmp)
    bmpI2 = ImageTest(bmp2)
    pngI = ImageTest(png)
    jpgI = ImageTest(jpg)

    bmpI.import_image()
    bmpI.test_image_array()
    bmpI.peek_image_array()
    bmpI.describe()

    bmpI2.import_image()
    bmpI2.test_image_array()
    bmpI2.peek_image_array()
    bmpI2.describe()

    pngI.import_image()
    pngI.test_image_array()
    pngI.peek_image_array()
    pngI.describe()

    jpgI.import_image()
    jpgI.test_image_array()
    jpgI.peek_image_array()
    jpgI.describe()