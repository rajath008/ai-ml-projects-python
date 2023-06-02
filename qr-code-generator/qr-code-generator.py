import qrcode
count=1
while 1:
    link =str(input("Enter URL for which you want to generate a QR code : "))
    img=qrcode.make(link)

    print(f"QR code for {link} has been generated and saved ")
   
    img.save(f"qrcode {count}.jpg")
    count+=1