# text_decode.py

from main import dna_to_binary, binary_to_text, decompress_binary_data

def decode_dna_to_text(dna_file_path: str) -> str:
    with open(dna_file_path, 'r') as f:
        dna_data = f.read().strip()
    binary_data = dna_to_binary(dna_data)
    decompressed_binary = decompress_binary_data(binary_data)
    return binary_to_text(decompressed_binary)
