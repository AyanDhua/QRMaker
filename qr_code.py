import qrcode
print("Let's make QR codes")
while True:
    inp = eval(input("Please choose the desired option: \n 1: Make Simple QR \n 2: Generate customised QR Code \n 3: Exit \nEnter your choice: "))
    match inp:
        case 1:
            url=input("Enter the text you want to make QR of: ")
            name=input("Enter the name with which you want to save your QR: ")
            img= qrcode.make(url)
            img.save(f"{name}.png")
            print("QR generated successfully ")
            break
        case 2:
            url = input("Enter the text you want to make QR of: ")
            name = input("Enter the name with which you want to save your QR: ")
            b_size=int(input("Enter box size:"))
            b=int(input("Enter border width:"))
            q_color=input("Enter color for the QR code:")
            q_bcolor= input("Enter background color for the QR code:")
            qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=b_size,border=b)
            qr.add_data(url)
            qr.make(fit=True)
            img=qr.make_image(fill_color=q_color,back_color=q_bcolor)
            img.save(f"{name}.png")
            print("QR generated successfully ")
            break
        case 3:
            print("Thank You")
            break
        case _ :
            print("Please enter a valid Choice")
