import qrcode
import socket

# Auto-detect your local IP address
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # connect to Google DNS
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

# Get current IP and create full Flask URL
local_ip = get_local_ip()
url = f"http://{local_ip}:5001"
print(f"Detected local IP: {local_ip}")
print(f"Generating QR for: {url}")

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)
qr.add_data(url)
qr.make(fit=True)

# Create image
img = qr.make_image(fill_color="black", back_color="white")

# Save QR code image
img.save("smartqueue_qr.png")
print("✅ QR code saved as smartqueue_qr.png")

# Optionally open the image (Mac only)
try:
    import os
    os.system("open smartqueue_qr.png")
except:
    pass
