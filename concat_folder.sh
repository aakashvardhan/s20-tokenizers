#!/bin/bash

# Set paths
ZIP_FILE="archive.zip"
EXTRACT_DIR="."
TRAIN_DIR="$EXTRACT_DIR/train/train"
VALID_DIR="$EXTRACT_DIR/valid/valid"
TRAIN_OUTPUT="$EXTRACT_DIR/hindi_wiki_172k_train.txt"
VALID_OUTPUT="$EXTRACT_DIR/hindi_wiki_172k_valid.txt"

# Extract the zip file
unzip -q "$ZIP_FILE" -d "$EXTRACT_DIR"

# Function to combine text files
combine_files() {
    local input_dir=$1
    local output_file=$2
    
    # Clear the output file if it exists
    > "$output_file"
    
    # Combine all .txt files, adding <|endoftext|> and a newline after each file
    for file in "$input_dir"/*.txt; do
        cat "$file" >> "$output_file"
        echo "<|endoftext|>" >> "$output_file"
    done
    
    echo "Combined text saved to: $output_file"
}

# Combine training files
combine_files "$TRAIN_DIR" "$TRAIN_OUTPUT"

# Combine validation files
combine_files "$VALID_DIR" "$VALID_OUTPUT"

cat "$TRAIN_OUTPUT" "$VALID_OUTPUT" > hindi_wiki_172k_full.txt

echo "Process completed."