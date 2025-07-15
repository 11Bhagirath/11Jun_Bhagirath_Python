import qrcode

url="http://rainduction.com"

qr=qrcode.make(url)

qr.save("Ra.png")