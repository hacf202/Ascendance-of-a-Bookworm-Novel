import os

files = [
    r"d:\novel\translated_179_200.txt",
    r"d:\novel\translated_201_220.txt",
    r"d:\novel\translated_221_250.txt",
    r"d:\novel\translated_251_300.txt"
]

for file_path in files:
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = content.replace("Ro de mai", "Ro ze mai")
        new_content = new_content.replace("Ro De Mai", "Ro Ze Mai")
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
