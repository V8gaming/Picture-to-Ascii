import PIL.Image
from PIL import Image

ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]
def mainmain():
    path = input("Input valid path name to image:\n")
    try:
        image = PIL.Image.open(path) 
    except:
        print(path, "Is not a valid path to picture.")
    return(path)
path = mainmain()


im = Image.open(path)
width = im.size[0]
height = im.size[1]

im = im.resize((int(width /100 * 165), height), 2)
im = im.save("Temp.png")
im = Image.open("Temp.png")
new_width = im.size[0]
new_height = im.size[1]

def greyscale(image):
    greyscale_image = image.convert("L")
    return(greyscale_image)

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)

def main(innerwidth = int(new_width)):
    image = PIL.Image.open("Temp.png")
    new_image_data = pixels_to_ascii(greyscale(image))

    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+innerwidth)] for i in range(0, pixel_count, innerwidth))

    print(ascii_image)

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)
main()