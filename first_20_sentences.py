"""
first_20_sentences.py - Wypisuje pierwszych 20 zdań z tekstu.
"""
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def is_end_of_sentence(char):
    """
    Sprawdza, czy znak jest końcem zdania.
    """
    return char in '.!?'

def get_first_n_sentences(n=20):
    """
    Pobiera pierwszych n zdań z tekstu.
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
                
                # Zatrzymujemy się po zebraniu n zdań
                if len(sentences) >= n:
                    break
    
    # Obsługa ostatniego zdania, jeśli nie kończy się znakiem końca zdania
    if sentence and len(sentences) < n:
        sentences.append(sentence.strip())
    
    return sentences[:n]  # Upewniamy się, że mamy dokładnie n zdań (lub mniej, jeśli tyle nie ma)

def main():
    try:
        n = 20  # Liczba zdań do wypisania
        sentences = get_first_n_sentences(n)
        
        if sentences:
            print(f"Pierwszych {len(sentences)} zdań:")
            
            # Wypisujemy zdania w formacie zachowującym strukturę akapitów
            for sentence in sentences:
                # Sprawdzamy, czy zdanie kończy się znakiem końca zdania
                if sentence and sentence[-1] in '.!?':
                    print(sentence)
                else:
                    print(sentence + ".")
                
                # Dodajemy pustą linię po zdaniach kończących akapit
                if sentence and sentence[-1] == '\n':
                    print()
        else:
            print("Nie znaleziono żadnych zdań w tekście.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()