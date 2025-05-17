# decode.py

from main import dna_to_binary, binary_to_image, decompress_binary_data

def decode_dna_to_image(dna_file_path, output_image_path):
    with open(dna_file_path, 'r') as file:
        dna_data = file.read().strip()
    binary_data = dna_to_binary(dna_data)
    decompressed_binary = decompress_binary_data(binary_data)
    binary_to_image(decompressed_binary, output_image_path)
