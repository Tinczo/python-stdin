"""
find_longest_sentence.py - Wypisuje najdłuższe zdanie w książce (kryterium - liczba znaków).
"""
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def is_end_of_sentence(char):
    """
    Sprawdza, czy znak jest końcem zdania.
    """
    return char in '.!?'

def find_longest_sentence():
    """
    Znajduje najdłuższe zdanie w książce.
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
    
    # Znajdowanie najdłuższego zdania
    longest_sentence = ""
    max_length = 0
    
    for sentence in sentences:
        length = len(sentence)
        if length > max_length:
            max_length = length
            longest_sentence = sentence
    
    return longest_sentence, max_length

def main():
    try:
        longest_sentence, length = find_longest_sentence()
        print(f"Najdłuższe zdanie ({length} znaków):")
        print(longest_sentence)
    except Exception as e:
        print(f"Wystąpił błąd: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()