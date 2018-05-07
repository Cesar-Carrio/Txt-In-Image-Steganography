https://github.com/Cesar-Carrio/Txt-In-Image-Steganography

## Cesar J Carrillo
# Txt-In-Image-Steganography
A python3 application using Pillow library to hide text in images.
Three Libraries will be required for this application, those are sys, PIL, and re.


# Instructions - Command Line Arguments
## Encoding Text Into Image
## Make sure that the image AND text file to be encoded with is in the same local path if not include the path
** `> python3 steg.py enc <jpg image> <txt file>` **
## The File that will be produced will be called encoded.png


## Decoding Text From Image
# Make sure to use the encoded.png file
** `> python3 steg.py dec encoded.png` **
