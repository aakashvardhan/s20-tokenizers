"""
Train our Tokenizers on some data, just to see them in action.
The whole thing runs in ~25 seconds on my laptop.
"""

import os
import time
from basic_tokenizer import BasicTokenizer
from regex_tokenizer import RegexTokenizer
HINDI_PATTERN = r'[^\r\n\p{L}\p{N}]?[\p{L}\p{M}]+|\p{N}{1,3}| ?[^\s\p{L}\p{N}]+[\r\n]*|\s*[\r\n]|\s+(?!\S)|\s+'
# open some text and train a vocab of 512 tokens
text = open("train.txt", "r", encoding="utf-8").read()

# create a directory for models, so we don't pollute the current directory
os.makedirs("models", exist_ok=True)

t0 = time.time()

# construct the Tokenizer object and kick off verbose training
tokenizer = RegexTokenizer(pattern=HINDI_PATTERN)
tokenizer.train(text, 512, verbose=True)
# writes two files in the models directory: name.model, and name.vocab
prefix = os.path.join("models", "regex")
tokenizer.save(prefix)
t1 = time.time()

print(f"Training took {t1 - t0:.2f} seconds")
