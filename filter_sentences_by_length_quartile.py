"""
filter_sentences_by_length_quartile.py - Wypisuje na wyjściu tylko zdania w czwartym kwartylu
pod względem długości zdania (kryterium - liczba znaków).
"""
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def is_end_of_sentence(char):
    """
    Sprawdza, czy znak jest końcem zdania.
    """
    return char in '.!?'

def filter_sentences_in_fourth_quartile():
    """
    Filtruje zdania należące do czwartego kwartyla pod względem długości.
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
    
    # Jeśli nie ma zdań, zwracamy pustą listę
    if not sentences:
        return []
    
    # Obliczanie długości zdań
    sentence_lengths = []
    for sentence in sentences:
        sentence_lengths.append(len(sentence))
    
    # Sortowanie długości zdań
    sorted_lengths = sorted(sentence_lengths)
    
    # Obliczanie punktu odcięcia dla czwartego kwartyla
    n = len(sorted_lengths)
    q3_index = int(0.75 * n)
    quartile_threshold = sorted_lengths[q3_index]
    
    # Filtrowanie zdań w czwartym kwartylu
    filtered_sentences = []
    for i, sentence in enumerate(sentences):
        if len(sentence) >= quartile_threshold:
            filtered_sentences.append(sentence)
    
    return filtered_sentences

def main():
    try:
        filtered_sentences = filter_sentences_in_fourth_quartile()
        if filtered_sentences:
            print("Zdania w czwartym kwartylu pod względem długości:")
            for i, sentence in enumerate(filtered_sentences, 1):
                print(f"{i}. {sentence}")
        else:
            print("Nie znaleziono zdań lub nie można obliczyć kwartyli.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()