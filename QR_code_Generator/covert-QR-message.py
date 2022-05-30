import cv2
d = cv2.QRCodeDetector()
val, _, _ = d.detectAndDecode(cv2.imread("BABC-QR.jpg"))
print("Decoded text is: ", val)
