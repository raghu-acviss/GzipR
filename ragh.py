import gzip
import base64
import qrcode

# Data to compress
data_to_compress = "Raghu"

# Compress the data
compressed_data = gzip.compress(data_to_compress.encode("utf-8"))

# Encode the compressed data in base64 for easier handling
encoded_data = base64.b64encode(compressed_data).decode("utf-8")

# Symbol mapping using Unicode symbols
symbol_map = {
    'A': '\u25A0',  # Black Square
    'B': '\u25A1',  # White Square
    'C': '\u25A2',  # White Square with Rounded Corners
    'D': '\u25A3',  # White Square Containing Black Small Square
    'E': '\u25A4',  # Square with Horizontal Fill
    'F': '\u25A5',  # Square with Vertical Fill
    'G': '\u25A6',  # Square with Orthogonal Crosshatch Fill
    'H': '\u25A7',  # Square with Upper Left to Lower Right Fill
    'I': '\u25A8',  # Square with Upper Right to Lower Left Fill
    'J': '\u25A9',  # Square with Diagonal Crosshatch Fill
    'K': '\u25AA',  # Black Small Square
    'L': '\u25AB',  # White Small Square
    'M': '\u25AC',  # Black Rectangle
    'N': '\u25AD',  # White Rectangle
    'O': '\u25AE',  # Black Vertical Rectangle
    'P': '\u25AF',  # White Vertical Rectangle
    'Q': '\u25B0',  # Black Parallelogram
    'R': '\u25B1',  # White Parallelogram
    'S': '\u25B2',  # Black Up-Pointing Triangle
    'T': '\u25B3',  # White Up-Pointing Triangle
    # Add more symbols as needed
}

# Convert Base64-encoded data to symbols
symbolic_data = ''.join(symbol_map.get(char, char) for char in encoded_data)

# Create a QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add the symbolic data to the QR code
qr.add_data(symbolic_data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save or display the QR code image
img.save("g_qr_code_with_symbols.png")
