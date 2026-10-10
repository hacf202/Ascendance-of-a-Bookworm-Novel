import codecs

lines = codecs.open('d:/novel/p4vol5/translated_251_300.txt', 'r', 'utf-8-sig').read().split('\n')
dupes = []
seen = {}

for i, line in enumerate(lines):
    l = line.strip()
    if not l or len(l) < 30: continue
    if l in seen:
        dupes.append((seen[l], i+1, l[:50]))
    else:
        seen[l] = i+1

for d in dupes:
    print(f'Line {d[1]} duplicates Line {d[0]}: {d[2]}')
