import os
import sys
import numpy as np
from tokenizers import Tokenizer
import tokenizers
import subprocess


def train(input_file):

    tokenizer = tokenizers.SentencePieceBPETokenizer()
    tokenizer.train(input_file)
    tokenizer.save("hindi_tokenizer.json")


def compression_ratio(text, encoded):
    return len(text) / len(encoded.ids)


def main():
    # install from requirements.txt
    subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)

    if len(sys.argv) != 2:
        print("Usage: python train.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    train(input_file)
    load_tokenizer = Tokenizer.from_file("hindi_tokenizer.json")
    text = """कई मुश्किलों के बावजूद स्टार्मर ने कभी हार नहीं मानी. वे बचपन से ही पढ़ाई में अच्छे थे, परीक्षाओं में अच्छे नंबर लाने की वजह से ही उनका एडमिशन एक प्रत..."""
    encode_text = load_tokenizer.encode(text)

    print(f"Original text: {text}")
    print(f"Vocab Size: {load_tokenizer.get_vocab_size()}")
    print(f"Encoded text: {encode_text.tokens}")
    print(f"Compression Ratio: {compression_ratio(text, encode_text)}")
    print(f"Decoded text: {load_tokenizer.decode(encode_text.ids)}")


if __name__ == "__main__":
    main()
