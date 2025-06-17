from PIL import Image
import numpy as np
import os

def xor_encrypt(text, key):
    return [ord(text[i]) ^ ord(key[i % len(key)]) for i in range(len(text))]

def xor_decrypt(byte_list, key):
    return ''.join([chr(byte ^ ord(key[i % len(key)])) for i, byte in enumerate(byte_list)])

def int_to_bits(n, bits=16):
    return [(n >> i) & 1 for i in reversed(range(bits))]

def bits_to_int(bits):
    return sum([bit << (len(bits) - 1 - i) for i, bit in enumerate(bits)])

def bytes_to_bits(byte_list):
    return [((byte >> i) & 1) for byte in byte_list for i in reversed(range(8))]

def bits_to_bytes(bits):
    return [sum([(bit << (7 - j)) for j, bit in enumerate(bits[i:i+8])]) for i in range(0, len(bits), 8)]

def embed_bits_in_image(image_array, bit_stream):
    flat = image_array.flatten()
    if len(bit_stream) > len(flat):
        raise ValueError("Message too large!")
    for i, bit in enumerate(bit_stream):
        flat[i] = (flat[i] & ~1) | bit
    return flat.reshape(image_array.shape)

def encode_image(input_path, output_path, message, key):
    img = Image.open(input_path)
    pixels = np.array(img)

    encrypted = xor_encrypt(message, key)
    length_bits = int_to_bits(len(encrypted))
    message_bits = bytes_to_bits(encrypted)
    all_bits = length_bits + message_bits

    encoded_pixels = embed_bits_in_image(pixels, all_bits)
    Image.fromarray(encoded_pixels).save(output_path)

def decode_image(stego_path, key):
    img = Image.open(stego_path)
    pixels = np.array(img).flatten()

    length_bits = [pixels[i] & 1 for i in range(16)]
    msg_length = bits_to_int(length_bits)
    message_bits = [pixels[i+16] & 1 for i in range(msg_length * 8)]
    byte_list = bits_to_bytes(message_bits)
    return xor_decrypt(byte_list, key)
