"""
find_first_complex_sentence.py - Wyszukuje pierwsze zdanie, które ma więcej niż jedno zdanie podrzędne 
(na podstawie przecinków).
"""
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')


def is_end_of_sentence(char):
    """
    Sprawdza, czy znak jest końcem zdania.
    """
    return char in '.!?'

def has_multiple_subordinate_clauses(sentence):
    """
    Sprawdza, czy zdanie ma więcej niż jedno zdanie podrzędne (na podstawie przecinków).
    """
    comma_count = 0
    
    for char in sentence:
        if char == ',':
            comma_count += 1
    
    return comma_count > 1

def find_first_complex_sentence():
    """
    Znajduje pierwsze zdanie, które ma więcej niż jedno zdanie podrzędne.
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
    
    # Znajdowanie pierwszego zdania z wieloma zdaniami podrzędnymi
    for sentence in sentences:
        if has_multiple_subordinate_clauses(sentence):
            return sentence
    
    return ""

def main():
    try:
        complex_sentence = find_first_complex_sentence()
        if complex_sentence:
            print("Pierwsze zdanie z więcej niż jednym zdaniem podrzędnym:")
            print(complex_sentence)
        else:
            print("Nie znaleziono zdania z więcej niż jednym zdaniem podrzędnym.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()