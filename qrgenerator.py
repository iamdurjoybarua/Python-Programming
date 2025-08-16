# To install: pip install qrcode Pillow

import qrcode

def generate_qr_code(data, filename="qrcode.png"):
    """
    Generates and saves a QR code for the given data.
    """
    img = qrcode.make(data)
    img.save(filename)
    print(f"QR code successfully generated and saved as '{filename}'")

if __name__ == "__main__":
    data_to_encode = input("Enter the data (e.g., URL or text) to encode into a QR code: ")
    generate_qr_code(data_to_encode)