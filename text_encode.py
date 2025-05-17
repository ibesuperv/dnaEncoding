# text_encode.py

from main import text_to_binary, binary_to_dna, compress_binary_data

def encode_text_to_dna(text: str, output_dna_file: str):
    binary_data = text_to_binary(text)
    compressed_binary = compress_binary_data(binary_data)
    dna_data = binary_to_dna(compressed_binary)
    with open(output_dna_file, 'w') as f:
        f.write(dna_data)
