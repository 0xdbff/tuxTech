import qrcode
from PIL import Image

# Your QR code data (any string)
data = 'https://example.com'

# Create a QR code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add the data to the QR code object
qr.add_data(data)
qr.make(fit=True)

# Generate the QR code as an image
img = qr.make_image(fill_color='black', back_color='white')

# Save the QR code as an image
img.save('qr_code.png', 'PNG')

print("QR code image saved as 'qr_code.png'")

