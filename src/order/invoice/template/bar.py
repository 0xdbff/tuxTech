import barcode
from barcode.writer import ImageWriter

# Choose the type of barcode you want to create, in this case, 'code128'
barcode_type = "code128"

# Your barcode data
barcode_data = "1234567890"

# Create a barcode class
barcode_class = barcode.get_barcode_class(barcode_type)

# Subclass ImageWriter to remove the text below the barcode
class NoTextImageWriter(ImageWriter):
    def _paint_text(self, xpos, ypos):
        pass


# Create the custom writer instance
writer = NoTextImageWriter()

# Modify the scale to make the barcode larger
writer_options = {
    "xdim": 6,  # Increase the horizontal size of the barcode (default is 1)
    "ydim": 1,  # Keep the vertical size the same (default is 1)
}
writer.set_options(writer_options)

# Create the barcode object
barcode_object = barcode_class(barcode_data, writer)

# Save the barcode as an image
barcode_image = barcode_object.save("wide_barcode_image")

print("Wide barcode image saved as 'wide_barcode_image.png'")
