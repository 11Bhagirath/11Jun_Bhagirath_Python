import qrcode

url="https://www.google.com/maps/dir//SHAGUN+TRADING,+Gondal+Rd,+CHAUKDI,+Rajkot,+Kotharia,+Gujarat+360002/@22.2444186,70.8032677,17z/data=!4m8!4m7!1m0!1m5!1m1!1s0x3959ca9b1eea3e03:0xd15931cd3ec33c34!2m2!1d70.8032448!2d22.2442746?entry=ttu&g_ep=EgoyMDI1MDcwOS4wIKXMDSoASAFQAw%3D%3D"

qr=qrcode.make(url)

qr.save("Shagun_Location.png")