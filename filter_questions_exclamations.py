"""
filter_questions_exclamations.py - Wypisuje tylko zdania, które są pytaniami lub wykrzyknieniami.
"""
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def is_question_or_exclamation(sentence):
    """
    Sprawdza, czy zdanie jest pytaniem lub wykrzyknieniem.
    """
    if not sentence:
        return False
    
    # Usuwamy białe znaki z końca zdania
    sentence = sentence.strip()
    
    # Sprawdzamy ostatni znak
    if sentence and (sentence[-1] == '?' or sentence[-1] == '!'):
        return True
    
    return False

def filter_questions_and_exclamations():
    """
    Filtruje zdania będące pytaniami lub wykrzyknieniami.
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
            
            if char in '.!?' or (char == '\n' and i+1 < len(text) and text[i+1] == '\n'):
                # Koniec zdania
                sentences.append(sentence.strip())
                sentence = ""
                in_sentence = False
    
    # Obsługa ostatniego zdania, jeśli nie kończy się znakiem końca zdania
    if sentence:
        sentences.append(sentence.strip())
    
    # Filtrowanie pytań i wykrzyknień
    filtered_sentences = []
    
    for sentence in sentences:
        if is_question_or_exclamation(sentence):
            filtered_sentences.append(sentence)
    
    return filtered_sentences

def main():
    try:
        filtered_sentences = filter_questions_and_exclamations()
        if filtered_sentences:
            print("Zdania będące pytaniami lub wykrzyknieniami:")
            for i, sentence in enumerate(filtered_sentences, 1):
                print(f"{i}. {sentence}")
        else:
            print("Nie znaleziono zdań będących pytaniami lub wykrzyknieniami.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()