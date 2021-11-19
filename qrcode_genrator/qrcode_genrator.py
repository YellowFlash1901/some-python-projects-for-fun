import qrcode
import image

qr = qrcode.QRCode(
    version = 9,
    box_size = 10,
    border = 5
)

data = "https://github.com/YellowFlash1901"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill= "black",back_color="white")
img.save("Github.png")