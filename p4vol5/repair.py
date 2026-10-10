import codecs

# Read the original up to line 106
lines = codecs.open('d:/novel/p4vol5/translated_251_300.txt', 'r', 'utf-8-sig').read().split('\n')
base_text = '\n'.join(lines[:106])

# Read the temp_translate.txt which contains the accumulated translation
temp_text = codecs.open('d:/novel/p4vol5/temp_translate.txt', 'r', 'utf-8-sig').read()

# Combine them
final_text = base_text + '\n\n' + temp_text

# Write back
codecs.open('d:/novel/p4vol5/translated_251_300.txt', 'w', 'utf-8-sig').write(final_text)

print("Done repairing file.")
