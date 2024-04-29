#QR Code generator

#Installing packages 
#!pip install qrcode 
#!pip install pypng
'''Documentation of the qrcode Library:
    "https://pypi.org/project/qrcode/"
'''
#Importing qrcode
import qrcode

#Optional functions for advanced customization
#from qrcode.image.styledpil import StyledPilImage
#from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
#from qrcode.image.styles.colormasks import RadialGradiantColorMask

#Customizing QRcode features
features = qrcode.QRCode(
    version = 3,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 8,
    border = 3) 

#Inserting The String that the QRcode represents
features.add_data('String on the QR code - Links work as well')
features.make(fit = True)

#Creation of The QRCode
#Color customization (RGB codes can be used as parameters too)
img = features.make_image(fill_color = 'black', back_color = 'white')

#Saving the QRCode as a .PNG file
img.save("QR.png")


'''Optional Customization
img_1 allows rouded linesa on the QRCode 
img_2 allows the use of a gradient color not just a static combination of collors
img_3 allows an image of your choice to be placed in the middle of the QRCode
'''
#img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
#img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
#img_3 = qr.make_image(image_factory=StyledPilImage, embeded_image_path=" file-path")

#img_1.save("QR com imagem.png")
#img_2.save("QR com imagem.png")
#img_3.save("QR com imagem.png")