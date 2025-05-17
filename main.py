# main.py

import zlib

# Binary ↔ DNA
def binary_to_dna(binary_str):
    mapping = {'00': 'A', '01': 'C', '10': 'G', '11': 'T'}
    return ''.join(mapping[binary_str[i:i+2]] for i in range(0, len(binary_str), 2))

def dna_to_binary(dna_str):
    reverse_mapping = {'A': '00', 'C': '01', 'G': '10', 'T': '11'}
    return ''.join(reverse_mapping[nuc] for nuc in dna_str)

# Compression
def compress_binary_data(binary_str: str) -> str:
    data = int(binary_str, 2).to_bytes((len(binary_str) + 7) // 8, byteorder='big')
    compressed = zlib.compress(data)
    return ''.join(f'{byte:08b}' for byte in compressed)

def decompress_binary_data(binary_str: str) -> str:
    compressed_bytes = bytes(int(binary_str[i:i+8], 2) for i in range(0, len(binary_str), 8))
    decompressed = zlib.decompress(compressed_bytes)
    return ''.join(f'{byte:08b}' for byte in decompressed)

# Image
def image_to_binary(image_path):
    with open(image_path, 'rb') as file:
        binary_data = file.read()
    return ''.join(f'{byte:08b}' for byte in binary_data)

def binary_to_image(binary_str, output_path):
    bytes_list = [int(binary_str[i:i+8], 2) for i in range(0, len(binary_str), 8)]
    with open(output_path, 'wb') as file:
        file.write(bytearray(bytes_list))

# Text
def text_to_binary(text: str) -> str:
    return ''.join(f'{ord(char):08b}' for char in text)

def binary_to_text(binary_str: str) -> str:
    chars = [chr(int(binary_str[i:i+8], 2)) for i in range(0, len(binary_str), 8)]
    return ''.join(chars)
