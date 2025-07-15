import qrcode

#url="https://www.tops-int.com/"

#qr=qrcode.make(url)


data=f"Address: 101, Aditya Complex, Jalaram 2 Street Number 2, above Sbi Bank, Near Indira Circle, Jala Ram Nagar, Rajkot, Gujarat 360005\nhttps://maps.app.goo.gl/vf8cqLgEBvfkCyp19"


qr=qrcode.make(data)
qr.save("tops1.png")