import qrcode

url="https://www.marwadiuniversity.ac.in/"

qr=qrcode.make(url)

qr.save("Ra.png")