import qrcode as qrc

from PIL import Image

qr = qrc.QRCode(version=1,error_correction=qrc.constants.ERROR_CORRECT_H,box_size=10,border=5)

qr.add_data("https://github.com/charantm7")
qr.make(fit=True)

img = qr.make_image(fill_color="orange",back_color="green")
img.save("charan_github_profile.png")