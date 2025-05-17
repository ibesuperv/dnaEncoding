# app.py

import streamlit as st
from encode import encode_image_to_dna
from decode import decode_dna_to_image
from text_encode import encode_text_to_dna
from text_decode import decode_dna_to_text
from PIL import Image
import os

st.set_page_config(page_title="DNA Encoder/Decoder", layout="centered")
st.title("🧬 DNA Encoder & Decoder")
st.caption("Encode and decode images or text into DNA sequences (compression only, no encryption).")

mode = st.selectbox("Select Mode", [
    "Encode Image to DNA",
    "Decode DNA to Image",
    "Encode Text to DNA",
    "Decode DNA to Text"
])

if mode == "Encode Image to DNA":
    st.header("🖼️ Encode Image")
    uploaded_image = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
    output_dna_file = st.text_input("DNA File Name", "image_dna.txt")

    if uploaded_image and st.button("Encode Image"):
        with open("temp_image", "wb") as f:
            f.write(uploaded_image.getbuffer())
        try:
            encode_image_to_dna("temp_image", output_dna_file)
            with open(output_dna_file) as f:
                dna = f.read()
            st.success("✅ Image encoded into DNA!")
            st.text_area("DNA Output", dna[:500] + "..." if len(dna) > 500 else dna, height=150)
            st.download_button("⬇ Download DNA", dna, file_name=output_dna_file)
        except Exception as e:
            st.error(f"Error: {e}")
        os.remove("temp_image")

elif mode == "Decode DNA to Image":
    st.header("🖼️ Decode DNA to Image")
    uploaded_dna = st.file_uploader("Upload DNA File", type=["txt"])
    output_image_file = st.text_input("Output Image Filename", "decoded_image.png")

    if uploaded_dna and st.button("Decode DNA"):
        with open("temp_dna.txt", "wb") as f:
            f.write(uploaded_dna.getbuffer())
        try:
            decode_dna_to_image("temp_dna.txt", output_image_file)
            st.success("✅ DNA decoded into image!")
            st.image(output_image_file, caption="Decoded Image", use_container_width=True)
            with open(output_image_file, "rb") as f:
                st.download_button("⬇ Download Image", f.read(), file_name=output_image_file)
        except Exception as e:
            st.error(f"Error: {e}")
        os.remove("temp_dna.txt")

elif mode == "Encode Text to DNA":
    st.header("✍️ Encode Text")
    input_text = st.text_area("Enter Text")
    output_dna_file = st.text_input("DNA File Name", "text_dna.txt")

    if input_text and st.button("Encode Text"):
        try:
            encode_text_to_dna(input_text, output_dna_file)
            with open(output_dna_file) as f:
                dna = f.read()
            st.success("✅ Text encoded into DNA!")
            st.text_area("DNA Output", dna[:500] + "..." if len(dna) > 500 else dna, height=150)
            st.download_button("⬇ Download DNA", dna, file_name=output_dna_file)
        except Exception as e:
            st.error(f"Error: {e}")

elif mode == "Decode DNA to Text":
    st.header("📖 Decode Text from DNA")
    uploaded_dna = st.file_uploader("Upload DNA File", type=["txt"])

    if uploaded_dna and st.button("Decode DNA"):
        with open("temp_dna_text.txt", "wb") as f:
            f.write(uploaded_dna.getbuffer())
        try:
            decoded_text = decode_dna_to_text("temp_dna_text.txt")
            st.success("✅ DNA decoded into text!")
            st.text_area("Decoded Text", decoded_text, height=150)
        except Exception as e:
            st.error(f"Error: {e}")
        os.remove("temp_dna_text.txt")
