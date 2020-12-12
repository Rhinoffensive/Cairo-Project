import numpy as np
from PIL import Image
from pylab import *




img = Image.open('zeplin.jpg').convert('L')

im= np.array(img)

M,N = 10, 10




tiles = [im[x:x+M,y:y+N] for x in range(0,im.shape[0],M) for y in range(0,im.shape[1],N)]

plot(array(tiles[0]))


from PIL import Image

class SpriteSheetReader:

    def __init__(self, imageName, tileSize):
        self.spritesheet = Image.open(imageName)
        self.tileSize = tileSize
        self.margin = 1

    def getTile(self, tileX, tileY):
        posX = (self.tileSize * tileX) + (self.margin * (tileX + 1))
        posY = (self.tileSize * tileY) + (self.margin * (tileY + 1))
        box = (posX, posY, posX + self.tileSize, posY + self.tileSize)
        return self.spritesheet.crop(box)


from PIL import Image

class SpriteSheetReader:

    def __init__(self, imageName, tileSize):
        self.spritesheet = Image.open(imageName)
        self.tileSize = tileSize
        self.margin = 1

    def getTile(self, tileX, tileY):
        posX = (self.tileSize * tileX) + (self.margin * (tileX + 1))
        posY = (self.tileSize * tileY) + (self.margin * (tileY + 1))
        box = (posX, posY, posX + self.tileSize, posY + self.tileSize)
        return self.spritesheet.crop(box)

from PIL import Image

class SpriteSheetReader2:

    def __init__(self, imageName, rows, cols):
        self.spritesheet = Image.open(imageName)
        self.tileSizeX = self.spritesheet.width // cols
        self.tileSizeY =  self.spritesheet.height // rows
        self.margin = 1

    def getTile(self, tileX, tileY):
        posX = (self.tileSizeX * tileX) + (self.margin * (tileX + 1))
        posY = (self.tileSizeY * tileY) + (self.margin * (tileY + 1))
        box = (posX, posY, posX + self.tileSizeX, posY + self.tileSizeY)
        return self.spritesheet.crop(box)




reader = SpriteSheetReader2("zeplin.jpg", 10, 10)
tile1 = reader.getTile(9, 9)
tile1.show()



