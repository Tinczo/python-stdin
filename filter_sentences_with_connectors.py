"""
filter_sentences_with_connectors.py - Wypisuje tylko zdania, które zawierają co najmniej dwa wyrazy
z następujących: „i", „oraz", „ale", „że", „lub".
"""
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def is_end_of_sentence(char):
    """
    Sprawdza, czy znak jest końcem zdania.
    """
    return char in '.!?'

def count_specific_words(sentence, target_words):
    """
    Liczy wystąpienia określonych wyrazów w zdaniu.
    """
    count = 0
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
    
    # Zliczamy wystąpienia docelowych wyrazów
    for word in words:
        if word in target_words:
            count += 1
    
    return count

def filter_sentences_with_connectors():
    """
    Filtruje zdania zawierające co najmniej dwa wyrazy z listy spójników.
    """
    connectors = ["i", "oraz", "ale", "że", "lub"]
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
    
    # Filtrowanie zdań z co najmniej dwoma spójnikami
    filtered_sentences = []
    
    for sentence in sentences:
        if count_specific_words(sentence, connectors) >= 2:
            filtered_sentences.append(sentence)
    
    return filtered_sentences

def main():
    try:
        filtered_sentences = filter_sentences_with_connectors()
        if filtered_sentences:
            print("Zdania zawierające co najmniej dwa spójniki z listy ('i', 'oraz', 'ale', 'że', 'lub'):")
            for i, sentence in enumerate(filtered_sentences, 1):
                print(f"{i}. {sentence}")
        else:
            print("Nie znaleziono zdań zawierających co najmniej dwa spójniki z listy.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()