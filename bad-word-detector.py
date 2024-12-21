import sys
import time
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords

# Ensure NLTK stopwords corpus is downloaded
import nltk
nltk.download('stopwords')

def calculate_languages_ratios(text):
    languages_ratios = {}
    tokens = wordpunct_tokenize(text)
    words = [word.lower() for word in tokens]

    # Compute per language the number of unique stopwords appearing in analyzed text
    for language in stopwords.fileids():
        stopwords_set = set(stopwords.words(language))
        common_elements = set(words).intersection(stopwords_set)
        languages_ratios[language] = len(common_elements)  # language "score"

    return languages_ratios

def detect_language(text):
    ratios = calculate_languages_ratios(text)
    return max(ratios, key=ratios.get)

def map_language(language):
    # Map unconventional languages to supported ones
    language_mapping = {
        'hinglish': 'english',  # Map HINGLISH to ENGLISH
        # Add more mappings if needed
    }
    return language_mapping.get(language.lower(), language.lower())

def load_bad_words(language):
    if language.lower() in ['english', 'french', 'spanish', 'german']:
        try:
            badwords_list = []
            with open(f'datasets/{language.lower()}.csv', 'r', encoding='utf-8') as file:
                badwords_list = [word.strip().lower() for word in file]
            return set(badwords_list)
        except Exception as e:
            print(f"Error loading bad words for {language}: {e}")
            return set()
    else:
        return set()

def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python badworddet.py <text_file>")
        sys.exit(1)

    filename = sys.argv[1]
    print(f"Input File Name: {filename}")

    try:
        text = load_file(filename)   
          #load_file is function that is defined above 
        print('\n-----------------Input Text-----------------')
        print(text)
        print('--------------------------------------------\n')
    except Exception as e:
        print(f"Error loading text file. Error: {e}")
        sys.exit(1)

    language = detect_language(text)
    mapped_language = map_language(language)  # Map unconventional language names
    print(f"\n----------------------------")
    print(f"Language Detected: {language.upper()}")
    print(f"Mapped Language: {mapped_language.upper()}")
    print(f"----------------------------\n")

    print(f"Checking for bad words in {mapped_language.upper()} language...")
    print('**********************************************************\n')

    badwords = load_bad_words(mapped_language)
    if not badwords:
        print(f"No bad words found or language {mapped_language.upper()} not supported.")
        return

    lines = text.split('\n')
    for line_number, sentence in enumerate(lines, 1):
        for punct in ['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}']:
            sentence = sentence.replace(punct, '')
        abuses = [word for word in sentence.lower().split() if word in badwords]
        if abuses:
            print(f"-- {len(abuses)} Bad Words found at line number: {line_number} --")
            print(f"Bad Words: {', '.join(abuses)}")
            print('-----------------\n')

if __name__ == "__main__":
    main()
