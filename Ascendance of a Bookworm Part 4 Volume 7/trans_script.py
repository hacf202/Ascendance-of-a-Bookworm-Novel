import os
import re
import codecs
from googletrans import Translator
import time

def apply_rules(text):
    text = text.replace("Quý bà", "Phu nhân")
    text = text.replace("Quý cô", "Tiểu thư")
    text = text.replace("Chúa tể", "Ngài")
    text = text.replace("Lãnh chúa", "Ngài")
    text = text.replace("Lady", "Tiểu thư")
    text = text.replace("Lord", "Ngài")
    text = text.replace("Madam", "Phu nhân")
    text = text.replace("Rozemyne", "Ro ze mai")
    text = text.replace("Mana", "Ma lực")
    text = text.replace("mana", "ma lực")
    text = text.replace("Feybeast", "Quái thú")
    text = text.replace("feybeast", "quái thú")
    return text

def clean_page_numbers(text):
    # Remove lines like "Page | 179" or "124 | P a g e"
    text = re.sub(r'(?i)^\s*(Page\s*\|\s*\d+|\d+\s*\|\s*P\s*a\s*g\s*e)\s*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'\n{2,}', '\n', text)
    return text

def translate_file():
    input_path = "rawtext101_150.txt"
    output_path = "translated_101_150.txt"
    
    with codecs.open(input_path, 'r', 'utf-8') as f:
        content = f.read()
        
    content = clean_page_numbers(content)
    
    translator = Translator()
    
    # Split into paragraphs
    paragraphs = [p for p in content.split('\n') if p.strip()]
    
    translated_text = ""
    print(f"Total paragraphs to translate: {len(paragraphs)}")
    
    for i, p in enumerate(paragraphs):
        try:
            res = translator.translate(p, dest='vi')
            translated = apply_rules(res.text)
            translated_text += translated + "\n"
        except Exception as e:
            print(f"Error at paragraph {i}: {e}")
            # on error, keep the original to not lose text, or retry
            try:
                time.sleep(2)
                res = translator.translate(p, dest='vi')
                translated = apply_rules(res.text)
                translated_text += translated + "\n"
            except Exception as e2:
                print(f"Retry failed for paragraph {i}: {e2}")
                translated_text += p + "\n"
                
        if i % 10 == 0:
            print(f"Translated {i}/{len(paragraphs)} paragraphs...")
        time.sleep(0.5)

    with codecs.open(output_path, 'w', 'utf-8') as f:
        f.write(translated_text)
        
    print("Translation completed successfully.")

if __name__ == "__main__":
    translate_file()
