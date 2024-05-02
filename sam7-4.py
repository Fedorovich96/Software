from get_datetime import get_datetime
get_datetime()

import re

def load_banned_words(filename):
    with open(filename, 'r') as file:
        return file.read().split()

def censor_text(text, banned_words):
    for word in banned_words:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        text = pattern.sub('*' * len(word), text)
    return text

def main():
    banned_words = load_banned_words('input2.txt')
    sentence = ("Hello, world! Python IS the programming language of thE future. My "
                "EMAIL is.... PYTHON is awesome!!!!")
    censored_text = censor_text(sentence, banned_words)
    print(censored_text)

if __name__ == "__main__":
    main()



