from PIL import Image
import os
import argparse

def rescale_images(directory, size):
    for img in os.listdir(directory):
        im = Image.open(directory+img)
        im_resized = im.resize(size, Image.ANTIALIAS)
        im_resized.save(directory+img)
    
def convert_image(directory):
    for img in os.listdir(directory):
        im = Image.open(directory+img).convert("RGB")
        im.save(directory+img, "jpeg")
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rescale images")
    parser.add_argument('-d', '--directory', type=str, required=True, help="Put the directory name here")
    parser.add_argument('-s', '--size', type=int, nargs=2, required=False, help="Type in the sizwe of the image here")
    args = parser.parse_args()
    rescale_images(args.directory, args.size)
    #convert_image(args.directory)
