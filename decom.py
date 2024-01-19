import cv2
import base64
import gzip
import qrcode

# Define the symbol map used during encryption
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

# Read the QR code image
img = cv2.imread("g_qr_code_with_symbols.png")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create a QRCodeDetector object
qr_decoder = cv2.QRCodeDetector()

# Detect and decode the QR code
decoded_data, points, straight_qrcode = qr_decoder.detectAndDecode(gray)

# Extract the base64-encoded and compressed data
encoded_data = decoded_data.strip()

# Reverse Symbol Map for decoding
reverse_symbol_map = {v: k for k, v in symbol_map.items()}

# Convert symbols back to Base64 characters
base64_data = ''.join(reverse_symbol_map.get(char, char) for char in encoded_data)

# Decode base64 and decompress data
compressed_data = base64.b64decode(base64_data)
data = gzip.decompress(compressed_data).decode("utf-8")

print("Decoded Data:", data)
