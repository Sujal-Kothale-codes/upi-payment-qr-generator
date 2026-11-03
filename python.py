import qrcode

#taking UPI id from user 

UPI_id = input ("Enter your upi id = ")

#upi= //pay? pa=upi_id & pn =NAME & am = amount  & cu=currency & tn = message 

# Defining  the payment URl based on the upi id and payment app
# you can modify these URl based on the payment apps you want to support 

phonepe_url = f'upi://pay?pa={UPI_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={UPI_id}&pn=Recipient%20Name&mc=1234'
googlepay_url = f'upi://pay?pa={UPI_id}&pn=Recipient%20Name&mc=1234'

#create QR codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make (paytm_url)
googlepay_qr = qrcode.make(googlepay_url)

#save the QR code to image file 

phonepe_qr.save('phonepay.png')
paytm_qr.save('paytm.png')
googlepay_qr.save('googlepay.png')

#display the QR code (you need to install PIL/Pillow library)
phonepe_qr.show()
paytm_qr.show()
googlepay_qr.show()

