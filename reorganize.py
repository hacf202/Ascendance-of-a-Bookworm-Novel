import os
import codecs
import re

base_dir = r"d:\novel\Ascendance of a Bookworm Part 4 Volume 5"

# 1. Clear out target files
targets = [
    "translated_01_50.txt",
    "translated_51_100.txt",
    "translated_101_150.txt",
    "translated_151_200.txt",
    "translated_201_250.txt",
]
for t in targets:
    with codecs.open(os.path.join(base_dir, t), 'w', 'utf-8') as f:
        f.write("")

# 2. Extract text from append_*.py
def append_from_script(script_name, target_name):
    script_path = os.path.join(base_dir, script_name)
    target_path = os.path.join(base_dir, target_name)
    with codecs.open(script_path, 'r', 'utf-8') as f:
        content = f.read()
    
    # Extract lines array
    # It looks like: lines = [\n "text",\n ... \n]
    match = re.search(r'lines = \[(.*?)\]\n\nwith', content, re.DOTALL)
    if match:
        lines_str = match.group(1)
        # Using eval is slightly unsafe normally but we know the content
        # Actually eval might fail due to syntax. Let's just run the script but with modified output path!
        new_content = content.replace("translated_1_50.txt", target_name)
        new_script_path = os.path.join(base_dir, "temp_" + script_name)
        with codecs.open(new_script_path, 'w', 'utf-8') as f:
            f.write(new_content)
        os.system(f'python "{new_script_path}"')
        os.remove(new_script_path)
    else:
        print(f"Could not parse {script_name}")

append_from_script("append_1_25.py", "translated_01_50.txt")
append_from_script("append_26_50.py", "translated_01_50.txt")
append_from_script("append_51_75.py", "translated_51_100.txt")
append_from_script("append_76_100.py", "translated_51_100.txt")
append_from_script("append_101_123.py", "translated_101_150.txt")

# 3. Concatenate the text files
def append_from_txt(source_name, target_name):
    source_path = os.path.join(base_dir, source_name)
    target_path = os.path.join(base_dir, target_name)
    if os.path.exists(source_path):
        with codecs.open(source_path, 'r', 'utf-8') as f:
            text = f.read()
        with codecs.open(target_path, 'a', 'utf-8') as f:
            f.write(text)

append_from_txt("translated_124_150.txt", "translated_101_150.txt")

append_from_txt("translated_151_178.txt", "translated_151_200.txt")
append_from_txt("translated_179_200.txt", "translated_151_200.txt")

append_from_txt("translated_201_220.txt", "translated_201_250.txt")
append_from_txt("translated_221_250.txt", "translated_201_250.txt")

print("Reorganization complete!")

