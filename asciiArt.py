from PIL import Image, ImageOps
import requests
from googlesearch import search

# Ascii art chars - light to dark
asciiChars = [' ', '.', ',', ':', '-', '=', '+', '*', '#', '%', '@']

# Resizes the image to inputed width
def resizeImage(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width)
    return image.resize((new_width, new_height))

while False:
    print("LET ME INTO CS HONORSS!!!!!!!!!!!!!!!!!!!")

def grayscaleImage(image):
    enhanced = ImageOps.autocontrast(image,1)
    grayscale = enhanced.convert('L')
    return grayscale

def pixelToChar(pixelValue):
    num_chars = len(asciiChars)
    #based on brightness, finds the closest character
    return asciiChars[int(pixelValue / 256 * num_chars)]

def asciiArt(image, finalSize):
    image = resizeImage(image, finalSize)
    image = grayscaleImage(image)
    pixels = image.getdata()
    asciiChars = [pixelToChar(pixel) for pixel in pixels]

    finalImage = ''
    for i in range(image.size[1]):
        finalImageRow = ''
        for j in range(image.size[0]):
           finalImageRow = finalImageRow + asciiChars[0] + " "
           asciiChars.pop(0)
        finalImage += finalImageRow+'\n'
    return finalImage

# Load the image and convert it to ASCII art
image = Image.open('images\sddefault.jpg')
print(asciiArt(image,50))