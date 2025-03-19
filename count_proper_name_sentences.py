"""
count_proper_name_sentences.py - Liczy procent zdań, które zawierają przynajmniej jedną nazwę własną.
Nazwą własną jest każdy wyraz napisany wielką literą, nie będący pierwszym wyrazem w zdaniu.
"""
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def is_end_of_sentence(char):
    """
    Sprawdza, czy znak jest końcem zdania.
    """
    return char in '.!?'

def has_proper_name(sentence):
    """
    Sprawdza, czy zdanie zawiera nazwę własną.
    """
    words = []
    word = ""
    
    for char in sentence:
        if char in ' \t\n\r\f\v':
            if word:
                words.append(word)
                word = ""
        else:
            word += char
    
    if word:
        words.append(word)
    
    # Sprawdzamy, czy istnieje wyraz z wielką literą, który nie jest pierwszym wyrazem zdania
    for i in range(1, len(words)):
        word = words[i]
        if word and word[0].isupper():
            return True
    
    return False

def count_sentences_with_proper_names():
    """
    Liczy procent zdań, które zawierają przynajmniej jedną nazwę własną.
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
    
    # Obliczanie procentu zdań z nazwami własnymi
    proper_name_count = 0
    total_sentences = len(sentences)
    
    for sentence in sentences:
        if has_proper_name(sentence):
            proper_name_count += 1
    
    if total_sentences > 0:
        percent = (proper_name_count / total_sentences) * 100
    else:
        percent = 0
    
    return percent, proper_name_count, total_sentences

def main():
    try:
        percent, proper_name_count, total_sentences = count_sentences_with_proper_names()
        print(f"Procent zdań z nazwami własnymi: {percent:.2f}% ({proper_name_count}/{total_sentences})")
    except Exception as e:
        print(f"Wystąpił błąd: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()