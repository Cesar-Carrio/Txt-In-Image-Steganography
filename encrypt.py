from PIL import Image


def encode(img,msg):

    length = len(msg) * 8 # 8 for the bits
    length_string = '{0:032b}'.format(length)
    ##print(length_string)
    rev_string = ''.join(reversed(length_string))
    length_list = list(rev_string)
    list_len = len(length_list)

    index_pixel = 0
    msg_index = 0

    #print(msg)
    bin_msg = ''.join(format(ord(x), '08b') for x in msg)


    #print(bin_msg)
    #print(len(ver_bin_msg))

    bin_msg_list = list(bin_msg)


    msg_len = len(bin_msg_list)
    msg_len_marker = len(bin_msg_list)
    #print(len(bin_msg_list))
    msg_rev_bin = ''.join(reversed(bin_msg_list))
    #print(msg_rev_bin)


    # use a copy of image to hide the text in
    encoded = img.copy()
    width, height = img.size


    for row in range(height - 1, 0, -1):
        for col in range(width - 1, 0, -1):
            if index_pixel < 11:

                #print("ORG: "+ str(img.getpixel((col,row))))
                r,g,b = img.getpixel((col,row))
                # taking binary value and converting into string for later use
                red_bin = str(bin(r))
                green_bin = str(bin(g))
                blue_bin = str(bin(b))

                # need to put bit that needs to encoded from length num
                red_list = list(red_bin)
                red_list[len(red_list) - 1] = length_list[list_len-1]

                list_len -= 1

                green_list = list(green_bin)
                green_list[len(green_list) - 1] = length_list[list_len-1]

                list_len -= 1

                if index_pixel == 10:
                    blue_list = list(blue_bin)
                    blue_list[len(blue_list) - 1] = blue_bin[len(blue_list)-1]
                    list_len -= 1

                else:
                    blue_list = list(blue_bin)
                    blue_list[len(blue_list) - 1] = length_list[list_len - 1]

                    list_len -= 1

                #converting back to string then int for rgb values
                red_conv_from_list_2_str = ''.join(red_list)
                red_str_in_bin = red_conv_from_list_2_str[2:]
                red_bin_to_integer = int(red_str_in_bin,2)

                green_conv_from_list_2_str = ''.join(green_list)
                green_str_in_bin = green_conv_from_list_2_str[2:]
                green_bin_to_integer = int(green_str_in_bin, 2)

                blue_conv_from_list_2_str = ''.join(blue_list)
                blue_str_in_bin = blue_conv_from_list_2_str[2:]
                blue_bin_to_integer = int(blue_str_in_bin, 2)


                blue_conv_from_list_2_str = ''.join(blue_list)
                blue_str_in_bin = blue_conv_from_list_2_str[2:]
                blue_bin_to_integer = int(blue_str_in_bin, 2)
                encoded.putpixel((col, row), (red_bin_to_integer, green_bin_to_integer, blue_bin_to_integer))
                #print("ENC: "+str(encoded.getpixel((col,row))))

                if index_pixel == 10:
                    index_pixel += 2
                    continue
                else:
                    index_pixel += 1
####################################################################################################################################
            if index_pixel > 11 and msg_index < msg_len_marker -1 and msg_index > -1:

                #print("ENC: " + str(encoded.getpixel((col, row))))
                rr, gg, bb = img.getpixel((col, row))
                # taking binary value and converting into string for later use
                red_binn = str(bin(rr))
                green_binn = str(bin(gg))
                blue_binn = str(bin(bb))

                if msg_len < 0:
                    continue
                else:
                    # need to put bit that needs to encoded from length num
                    red_listt = list(red_binn)
                    red_listt[len(red_listt) - 1] = msg_rev_bin[msg_len - 1]

                    msg_len -= 1

                if msg_len < 0:
                    continue
                else:
                    green_listt = list(green_binn)
                    green_listt[len(green_listt) - 1] = msg_rev_bin[msg_len - 1]

                    msg_len -= 1

                if msg_len < 0:
                    continue
                else:
                    blue_listt = list(blue_binn)
                    blue_listt[len(blue_listt) - 1] = msg_rev_bin[msg_len - 1]

                    msg_len -= 1

                red_conv_from_list_2_strr = ''.join(red_listt)
                red_str_in_binn = red_conv_from_list_2_strr[2:]
                red_bin_to_integerr = int(red_str_in_binn, 2)

                green_conv_from_list_2_strr = ''.join(green_listt)
                green_str_in_binn = green_conv_from_list_2_strr[2:]
                green_bin_to_integerr = int(green_str_in_binn, 2)

                blue_conv_from_list_2_strr = ''.join(blue_listt)
                blue_str_in_binn = blue_conv_from_list_2_strr[2:]
                blue_bin_to_integerr = int(blue_str_in_binn, 2)

                encoded.putpixel((col, row), (red_bin_to_integerr, green_bin_to_integerr, blue_bin_to_integerr))
                #print("ENC: " + str(encoded.getpixel((col, row))))

                msg_index += 1
                index_pixel += 1

    return encoded


img = Image.open("hacker-neo.jpg") #needs to be jpeg file that later converts to png



with open('SourceCode.txt', 'r') as myfile:
    data=myfile.read()

print(data+"\n\n")

msg = "security is not fun"

image_encoded = encode(img,msg)
image_encoded.save("encoded.png")
