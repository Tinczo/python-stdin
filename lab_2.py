"""
lab_2.py - Odczytuje treść książki z wejścia standardowego, ignorując preambułę i informacje o wydaniu.
Usuwa zbędne spacje wewnątrz linii i oczyszcza białe znaki na początku i końcu każdej linii.
"""
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def main():
    # Zmienne do śledzenia stanu
    in_preamble = True        # Czy jesteśmy w preambule
    empty_line_count = 0      # Licznik pustych linii (do wykrycia końca preambuły)
    preamble_line_count = 0   # Licznik linii preambuły
    
    for line in sys.stdin:
        # Sprawdzenie czy to początek informacji o wydaniu
        if line.strip() == "-----":
            break
        
        # Obsługa preambuły
        if in_preamble:
            preamble_line_count += 1
            
            # Sprawdzenie, czy linia jest pusta
            if not line.strip():
                empty_line_count += 1
            else:
                empty_line_count = 0
            
            # Wykrywanie końca preambuły
            if empty_line_count >= 2:
                in_preamble = False
                empty_line_count = 0
            
            # Jeśli przejrzeliśmy 10 linii i nie znaleźliśmy dwóch pustych z rzędu, zakładamy brak preambuły
            if preamble_line_count >= 10 and empty_line_count < 2:
                in_preamble = False
                # Ponieważ nie ma preambuły, musimy zacząć od początku
                sys.stdin.seek(0)
                preamble_line_count = 0
            
            # Kontynuujemy, jeśli wciąż jesteśmy w preambule
            if in_preamble:
                continue
        
        # Przetwarzanie treści książki
        processed_line = process_line(line)
        
        # Wypisanie przetworzonej linii
        if processed_line or processed_line == "":
            print(processed_line)

def process_line(line):
    """
    Przetwarza linię usuwając zbędne spacje i białe znaki na początku i końcu.
    """
    processed = ""
    prev_space = False
    
    for char in line:
        if char == ' ' or char == '\t':
            if not prev_space:
                processed += ' '
                prev_space = True
        else:
            processed += char
            prev_space = False
    
    return processed.strip()

if __name__ == "__main__":
    main()