import qrcode
import image

qr = qrcode.QRCode(
    version = 9, #add complexity to the qr higher the no. higher the complexity
    box_size = 10, #it decides the no. of boxes in which the qrcode should be made
    border = 5 #white part of image
   
)

data = "https://github.com/YellowFlash1901" #add your own data to generate a qr code for your own data(website links,... etc).

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill= "black",back_color="white")
img.save("Github.png")
