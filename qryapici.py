import qrcode # Kütüphaneyi import ediyoruz. - We import the library.
img = qrcode.make(".com") # URL Adresi veya Site Domain, Youtube Linki'de dahil herşey. - URL Address or Site Domain, everything including Youtube Link.

type(img) # QR Kod'un türü, img = Resim - Type of QR Code, img = Image
img.save(".png") # QR Kod kayıt edilirken hangi ad ile kaydedilecek belirtiniz. - Specify the name under which the QR Code will be saved.
