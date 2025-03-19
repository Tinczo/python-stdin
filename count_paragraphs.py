"""
count_paragraphs.py - Zlicza akapity w tekście (akapit jest oddzielony pustą linią).
"""
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def count_paragraphs():
    """
    Zlicza akapity w tekście z wejścia standardowego.
    Akapit definiowany jest jako tekst oddzielony pustymi liniami.
    """
    paragraph_count = 0
    prev_line_empty = True  # Zakładamy, że przed pierwszą linią jest "pusta linia"
    
    for line in sys.stdin:
        current_line_empty = line.strip() == ""
        
        # Jeśli poprzednia linia była pusta i obecna nie jest, to zaczynamy nowy akapit
        if prev_line_empty and not current_line_empty:
            paragraph_count += 1
        
        prev_line_empty = current_line_empty
    
    return paragraph_count

def main():
    try:
        paragraph_count = count_paragraphs()
        print(f"Liczba akapitów: {paragraph_count}")
    except Exception as e:
        print(f"Wystąpił błąd: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()