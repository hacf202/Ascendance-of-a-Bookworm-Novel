import os
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
    return text

def translate_file(input_path, output_path, start_pattern, end_pattern=None):
    if not os.path.exists(input_path):
        return

    with codecs.open(input_path, 'r', 'utf-8') as f:
        lines = f.readlines()
        
    start_idx = 0
    if start_pattern:
        for i, line in enumerate(lines):
            if start_pattern in line:
                start_idx = i
                break
                
    end_idx = len(lines)
    if end_pattern:
        for i, line in enumerate(lines[start_idx:]):
            if end_pattern in line:
                end_idx = start_idx + i
                break
                
    text_to_translate = "".join(lines[start_idx:end_idx])
    
    translator = Translator()
    
    # Split into chunks of 3000 chars
    chunks = []
    current_chunk = ""
    for paragraph in text_to_translate.split('\n'):
        if len(current_chunk) + len(paragraph) > 3000:
            chunks.append(current_chunk)
            current_chunk = paragraph + '\n'
        else:
            current_chunk += paragraph + '\n'
    if current_chunk:
        chunks.append(current_chunk)
        
    translated_text = ""
    for chunk in chunks:
        if not chunk.strip():
            continue
        try:
            res = translator.translate(chunk, dest='vi')
            translated = apply_rules(res.text)
            translated_text += translated + "\n"
        except Exception as e:
            print(f"Error translating chunk: {e}")
            translated_text += chunk + "\n"
        time.sleep(1) # Be nice to the API
        
    with codecs.open(output_path, 'w', 'utf-8') as f:
        f.write(translated_text)

# 1. Translate rawtext101_150.txt from page 124 to end
translate_file(
    r"d:\novel\Ascendance of a Bookworm Part 4 Volume 5\rawtext101_150.txt",
    r"d:\novel\Ascendance of a Bookworm Part 4 Volume 5\translated_124_150.txt",
    "124 | P a g e"
)

# 2. Translate rawtext151_200.txt from start to page 178
translate_file(
    r"d:\novel\Ascendance of a Bookworm Part 4 Volume 5\rawtext151_200.txt",
    r"d:\novel\Ascendance of a Bookworm Part 4 Volume 5\translated_151_178.txt",
    None,
    "179 | P a g e"
)
print("Translation done.")
