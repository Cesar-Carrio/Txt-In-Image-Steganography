from PIL import Image
import re

#work on decryption first
def decode(img):
    width, height = img.size
    msg = ""
    size_of_msg = ""
    return_msg = ""
    index_pixel = 0

    for row in range(height-1,0,-1):
        for col in range(width-1,0,-1):

            if index_pixel < 11:
                r,g,b = img.getpixel((col,row))
                #taking binary value and converting into string for later use
                red_bin = str(bin(r))
                green_bin = str(bin(g))
                blue_bin = str(bin(b))

                if index_pixel == 10:
                    newString = red_bin[len(red_bin) - 1] + green_bin[len(green_bin) - 1]
                    size_of_msg = size_of_msg + newString
                    num_pixels_req = ((int(size_of_msg[:len(size_of_msg)], 2)))/3 + 11
                    index_pixel += 1
                else:
                    newString = red_bin[len(red_bin) - 1] + green_bin[len(green_bin) - 1] + blue_bin[len(blue_bin) - 1]
                    size_of_msg = size_of_msg + newString
                    index_pixel += 1

            elif index_pixel > 10 and index_pixel <= num_pixels_req:
                r, g, b = img.getpixel((col, row))
                # taking binary value and converting into string for later use
                red_bin = str(bin(r))
                green_bin = str(bin(g))
                blue_bin = str(bin(b))
                index_pixel += 1
                newString = red_bin[len(red_bin) - 1] + green_bin[len(green_bin) - 1] + blue_bin[len(blue_bin) - 1]
                msg = msg + newString

    #used regex to slice the long string of
    #binary numbers in order to convert
    #binary to Int then to ascii

    bin_text = re.findall('........', msg)
    for i in range(len(bin_text)):
        return_msg += chr(int(bin_text[i],2))

    return return_msg

img = Image.open("encoded.png")
decrypted_msg = decode(img)


img2 = Image.open("Secret.png")
decrypted_msg2 = decode(img2)

print("My Encoded Test: "+decrypted_msg)
print(decrypted_msg2)
