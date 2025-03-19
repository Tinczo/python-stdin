"""
filter_short_sentences.py - Wypisuje tylko zdania zawierające co najwyżej 4 wyrazy.
"""
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def is_end_of_sentence(char):
    """
    Sprawdza, czy znak jest końcem zdania.
    """
    return char in '.!?'

def count_words(sentence):
    """
    Liczy liczbę wyrazów w zdaniu.
    """
    word_count = 0
    in_word = False
    
    for char in sentence:
        if char in ' \t\n\r\f\v':
            if in_word:
                in_word = False
        else:
            if not in_word:
                word_count += 1
                in_word = True
    
    return word_count

def filter_sentences_with_at_most_4_words():
    """
    Filtruje zdania zawierające co najwyżej 4 wyrazy.
    """
    text = sys.stdin.read()
    
    sentences = []
    sentence = ""
    in_sentence = False
    
    for i in range(len(text)):
        char = text[i]
        
        if not in_sentence and not (char in ' \t\n\r\f\v'):
            in_sentence = True
        
        if in_sentence:
            sentence += char
            
            if is_end_of_sentence(char) or (char == '\n' and i+1 < len(text) and text[i+1] == '\n'):
                # Koniec zdania
                sentences.append(sentence.strip())
                sentence = ""
                in_sentence = False
    
    # Obsługa ostatniego zdania, jeśli nie kończy się znakiem końca zdania
    if sentence:
        sentences.append(sentence.strip())
    
    # Filtrowanie zdań z co najwyżej 4 wyrazami
    filtered_sentences = []
    
    for sentence in sentences:
        if count_words(sentence) <= 4:
            filtered_sentences.append(sentence)
    
    return filtered_sentences

def main():
    try:
        short_sentences = filter_sentences_with_at_most_4_words()
        if short_sentences:
            print("Zdania zawierające co najwyżej 4 wyrazy:")
            for i, sentence in enumerate(short_sentences, 1):
                print(f"{i}. {sentence}")
        else:
            print("Nie znaleziono zdań zawierających co najwyżej 4 wyrazy.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()