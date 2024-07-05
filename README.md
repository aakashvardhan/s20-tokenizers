# Using Byte Pair Encoding (BPE) for tokenization of Hindi text

This is a simple implementation of Byte Pair Encoding (BPE) for tokenization of Hindi text. The code is written in Python and uses the `tokenizers` library for BPE tokenization. The code is tested on Hindi text but can be used for any language.

## Requirements
- tokenizers


## Running the code

```
[00:00:15] Pre-processing files (745 Mo)  █████████████████████████ 100%[00:00:00] Tokenize words                 █████████████████████████ 1001445  /  1001445
[00:00:04] Count pairs                    █████████████████████████ 1001445  /  1001445
[00:00:05] Compute merges                 █████████████████████████ 28999    /    28999
Original text: कई मुश्किलों के बावजूद स्टार्मर ने कभी हार नहीं मानी. वे बचपन से ही पढ़ाई में अच्छे थे, परीक्षाओं में अच्छे नंबर लाने की वजह से ही उनका एडमिशन एक प्रत...
Vocab Size: 30000
Encoded text: ['▁कई', '▁मुश्क', 'िलों', '▁के', '▁बावजूद', '▁स्टार', '्मर', '▁ने', '▁कभी', '▁हार', '▁नहीं', '▁मानी', '.', '▁वे', '▁बचपन', '▁से', '▁ही', '▁पढ़ाई', '▁में', '▁अच्छे', '▁थे,', '▁परीक्षाओं', '▁में', '▁अच्छे', '▁नंबर', '▁लाने', '▁की', '▁वजह', '▁से', '▁ही', '▁उनका', '▁एडम', 'िशन', '▁एक', '▁प्रत', '...']
Compression Ratio: 4.25
Decoded text: कई मुश्किलों के बावजूद स्टार्मर ने कभी हार नहीं मानी. वे बचपन से ही पढ़ाई में अच्छे थे, परीक्षाओं में अच्छे नंबर लाने की वजह से ही उनका एडमिशन एक प्रत...
```

## Screenshots from Hugging Face Gradio Interface

