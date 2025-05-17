# encode.py

from main import image_to_binary, binary_to_dna, compress_binary_data

def encode_image_to_dna(image_path, output_dna_file):
    binary_data = image_to_binary(image_path)
    compressed_binary = compress_binary_data(binary_data)
    dna_data = binary_to_dna(compressed_binary)
    with open(output_dna_file, 'w') as file:
        file.write(dna_data)
