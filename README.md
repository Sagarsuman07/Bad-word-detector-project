# Bad Words Detector

A Python script designed to detect the language of a text and filter out bad or abusive words.

### Problem Statement:
In many cases, large texts (such as articles or comments) contain inappropriate or offensive language. The challenge is to filter out these "bad words" in texts whose language is not predetermined. This script helps by detecting the language and filtering out offensive words in multiple languages including English, Spanish, French, and German.

### Key Features:
- **Language Detection**: The script automatically detects the language of the provided text.
- **Bad Word Filtering**: Once the language is identified, it fetches a predefined list of bad words for that language and filters them out.
- **Multi-language Support**: Currently supports **English**, **Spanish**, **French**, and **German**.

### How It Works:
The problem was solved in three main phases:
1. **Language Detection**: Using the NLTK library, the script identifies the language of the text.
2. **Bad Word Identification**: It fetches a dataset of common bad words for the detected language.
3. **Output**: The script outputs the bad words found in each line of the text.

### Requirements:
- **Python**: Make sure Python is installed on your system.
- **NLTK Library**: You will need the NLTK library to run the script.

To install NLTK, run the following command:

```bash
pip install nltk
```
### How to Use:

1. **Prepare your text file**:  
   Put the text you want to analyze in a `.txt` file. For example, `test-english.txt` in the `test-files` folder.

2. **Run the script**:  
   Use the following command in your terminal to run the script:

   ```bash
   python bad-word-detector.py path/to/your-text-file.txt
   ```
   ```bash
   python bad-word-detector.py test-files/test-english.txt
   ```

### Example Usage:

1. Clone or download this repository.
2. Open a terminal or command prompt and navigate to the folder containing `bad-words-detector.py`.
3. Run the script with a sample text file:

   ```bash
   python bad-word-detector.py test-files/test-english.txt
