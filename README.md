Image Steganography Using LSB + XOR Encryption

This project demonstrates image steganography using the Least Significant Bit (LSB) technique combined with XOR encryption. It includes a browser-based GUI built with Flask for easy encoding and decoding of secret messages in images.


🚀 Features

- Message encryption using XOR logic
- Embeds secret message into image pixels using LSB
- Auto message length handling (no manual setting)
- Flask GUI (encode/decode in browser)


📁 Project Structure
IMG_STEGANOGRAPHY
  ├── app.py # Flask web app
  ├── stegano.py # Core logic for encoding/decoding
  ├── templates/ # HTML files 
  ├── static/uploads/ # Uploaded/stego images
  ├── cover.png # Input image
  ├── stego.png # Output image with message


⚙️ How to Run Locally

  1. Install dependencies:
  pip install flask pillow numpy
  2. Run the Flask app:
  python app.py
  3. Open browser and visit:
  http://127.0.0.1:5000



