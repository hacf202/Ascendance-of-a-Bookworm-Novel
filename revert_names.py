import os
import re

files = [
    r"d:\novel\translated_179_200.txt",
    r"d:\novel\translated_201_220.txt",
    r"d:\novel\translated_221_250.txt",
    r"d:\novel\translated_251_300.txt"
]

revert_dict = {
    "Phéc đi nan": "Ferdinand",
    "Xô lăng": "Solange",
    "Li xe lê ta": "Lieseleta",
    "Sờ goát": "Schwartz",
    "Uây": "Weiss",
    "Hia su": "Hirschur",
    "Co nê li út": "Cornelius",
    "Sa lốt": "Charlotte",
    "Uin phờ rít": "Wilfried",
    "Bô ni pha ti út": "Bonifatius",
    "Cát sờ tét": "Karstedt",
    "Xin vét tơ": "Sylvester",
    "Ri da đa": "Rihyarda",
    "Ô ti li": "Ottilie",
    "Đa mu en": "Damuel",
    "Hát mút": "Hartmut",
    "Phi lin": "Philine",
    "Bờ run hin đê": "Brunhilde",
    "Bờ run hin đờ": "Brunhilde",
    "An giê li ca": "Angelica",
    "Giu đít": "Judithe",
    "Lê ô no": "Leonore",
    "E gờ lan tin": "Eglantine",
    "A nát ta xi út": "Anastasius",
    "Xì ghi xoa": "Sigiswald",
    "Đết lin đê": "Detlinde",
    "Đết lin đờ": "Detlinde",
    "Giooc gin": "Georgine",
    "Giút tút": "Justus",
    "Giôn xa ra": "Jonsara",
    "Ca xích": "Kashick",
    "Con rát": "Konrad",
    "Mét ti ô nô ra": "Mestionora",
    "Han nê lo": "Hannelore",
    "Lét ti lau": "Lestilaut",
    "Óc tuyn": "Ortwin",
    "Ru đi gờ": "Rudiger",
    "A đôn phin": "Adolphine",
    "Gút run": "Gudrun",
    "Éc hát": "Eckhart"
}

for file_path in files:
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        for vn, en in revert_dict.items():
            content = content.replace(vn, en)
            
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
