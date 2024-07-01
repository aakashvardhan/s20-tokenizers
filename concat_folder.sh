#!/bin/bash

# Check if the correct number of arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 source_folder output_file"
    exit 1
fi

# Assign arguments to variables
SOURCE_FOLDER=$1
OUTPUT_FILE=$2

touch "$OUTPUT_FILE"

# Check if source folder exists
if [ ! -d "$SOURCE_FOLDER" ]; then
    echo "Source folder '$SOURCE_FOLDER' does not exist."
    exit 1
fi

# Concatenate all text files in the source folder into the output file using find and xargs
find "$SOURCE_FOLDER" -type f -name '*.txt' -print0 | xargs -0 cat > "$OUTPUT_FILE"

# Check if the concatenation was successful
if [ $? -eq 0 ]; then
    echo "All text files in '$SOURCE_FOLDER' have been successfully concatenated into '$OUTPUT_FILE'."
else
    echo "An error occurred while concatenating the files."
    exit 1
fi

# Delete the original folder

rm -rf "$SOURCE_FOLDER"

# Check if the deletion was successful
if [ $? -eq 0 ]; then
    echo "$SOURCE_FOLDER' has been successfully deleted."
else
    echo "An error occurred while deleting the original files."
    exit 1
fi