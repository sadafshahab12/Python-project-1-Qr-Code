import qrcode 
from PIL import Image
import qrcode.constants

#QRCode -->  change qr code functionality change border fix error , formatting, overlapping, set version
qr=qrcode.QRCode(version=1 , error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=12, border=3,)
qr.add_data("https://www.facebook.com/profile.php?id=61556555833599");
qr.make(fit=True)
img= qr.make_image(fill_color="red", back_color="blue");
img.save("sadaf_facebook_profile.png")
