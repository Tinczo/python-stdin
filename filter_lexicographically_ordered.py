"""
filter_lexicographically_ordered.py - Wypisuje tylko te zdania, których wyrazy są w porządku leksykograficznym.
"""
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def is_end_of_sentence(char):
    """
    Sprawdza, czy znak jest końcem zdania.
    """
    return char in '.!?'

def is_lexicographically_ordered(sentence):
    """
    Sprawdza, czy wyrazy w zdaniu są w porządku leksykograficznym.
    """
    words = []
    word = ""
    
    for char in sentence:
        if char in ' \t\n\r\f\v.,!?:;()[]{}':
            if word:
                words.append(word.lower())
                word = ""
        else:
            word += char
    
    if word:
        words.append(word.lower())
    
    # Sprawdzamy, czy wyrazy są posortowane leksykograficznie
    for i in range(1, len(words)):
        if words[i] < words[i-1]:
            return False
    
    return True

def filter_lexicographically_ordered_sentences():
    """
    Filtruje zdania, których wyrazy są w porządku leksykograficznym.
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
    
    # Filtrowanie zdań z wyrazami w porządku leksykograficznym
    filtered_sentences = []
    
    for sentence in sentences:
        if is_lexicographically_ordered(sentence):
            filtered_sentences.append(sentence)
    
    return filtered_sentences

def main():
    try:
        filtered_sentences = filter_lexicographically_ordered_sentences()
        if filtered_sentences:
            print("Zdania z wyrazami w porządku leksykograficznym:")
            for i, sentence in enumerate(filtered_sentences, 1):
                print(f"{i}. {sentence}")
        else:
            print("Nie znaleziono zdań z wyrazami w porządku leksykograficznym.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()