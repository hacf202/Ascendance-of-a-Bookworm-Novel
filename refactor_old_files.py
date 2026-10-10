import os
import re

files = [r"d:\novel\translated_179_200.txt", r"d:\novel\translated_201_220.txt"]

replacements = {
    "Rozemyne": "Ro de mai",
    "Ferdinand": "Phéc đi nan",
    "Solange": "Xô lăng",
    "Lieseleta": "Li xe lê ta",
    "Schwartz": "Sờ goát",
    "Weiss": "Uây",
    "Hirschur": "Hia su",
    "Cornelius": "Co nê li út",
    "Charlotte": "Sa lốt",
    "Wilfried": "Uin phờ rít",
    "Bonifatius": "Bô ni pha ti út",
    "Karstedt": "Cát sờ tét",
    "Sylvester": "Xin vét tơ",
    "Rihyarda": "Ri da đa",
    "Ottilie": "Ô ti li",
    "Damuel": "Đa mu en",
    "Hartmut": "Hát mút",
    "Philine": "Phi lin",
    "Brunhilde": "Bờ run hin đê",
    "Angelica": "An giê li ca",
    "Judithe": "Giu đít",
    "Leonore": "Lê ô no",
    "Eglantine": "E gờ lan tin",
    "Anastasius": "A nát ta xi út",
    "Sigiswald": "Xì ghi xoa",
    "Detlinde": "Đết lin đê",
    "Georgine": "Giooc gin",
    "Justus": "Giút tút",
    "Jonsara": "Giôn xa ra",
    "Kashick": "Ca xích",
    "Konrad": "Con rát",
    "Mestionora": "Mét ti ô nô ra"
}

for file_path in files:
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Remove Trang | XX
        content = re.sub(r'(?m)^Trang \| \d+\n?', '', content)
        
        # Replace names
        for old, new in replacements.items():
            content = content.replace(old, new)
            
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
