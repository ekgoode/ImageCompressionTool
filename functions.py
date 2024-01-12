# This program contains the functions required to compress and resize images
from PIL import Image
import os

def lossy_compress(Img, ImgFormat="PNG", CompressPct=100, FileName="image-file-compressed"):

    #Rescale Compression from interpretable scale to practical scale
    if CompressPct == 0:
        CompressPctScaled = 0
    else:
        CompressPctScaled = (95 * CompressPct)/100
    
    #Find and open image to be compressed
    image = Image.open(Img)
    
    #Save under different quality
    image.save(filename=FileName,
               format = ImgFormat,
               optimize = True,
               quality = CompressPct
               )
    
    return

