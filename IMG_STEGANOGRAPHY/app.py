from flask import Flask, render_template, request, redirect, send_file
import os
from stegano import encode_image, decode_image

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['GET', 'POST'])
def encode():
    if request.method == 'POST':
        file = request.files['image']
        message = request.form['message']
        key = request.form['key']

        input_path = os.path.join(UPLOAD_FOLDER, 'cover.png')
        output_path = os.path.join(UPLOAD_FOLDER, 'stego.png')
        file.save(input_path)

        try:
            encode_image(input_path, output_path, message, key)
            return render_template('encode.html', success=True, stego_path=output_path)
        except Exception as e:
            return render_template('encode.html', error=str(e))

    return render_template('encode.html')

@app.route('/decode', methods=['GET', 'POST'])
def decode():
    if request.method == 'POST':
        file = request.files['image']
        key = request.form['key']

        stego_path = os.path.join(UPLOAD_FOLDER, 'uploaded_stego.png')
        file.save(stego_path)

        try:
            message = decode_image(stego_path, key)
            return render_template('decode.html', message=message)
        except Exception as e:
            return render_template('decode.html', error=str(e))

    return render_template('decode.html')

if __name__ == '__main__':
    app.run(debug=True)
