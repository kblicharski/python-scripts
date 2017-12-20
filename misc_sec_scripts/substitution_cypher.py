text = 'GANG MAY KNOW YOUR IDENTITY ABORT ABORT MEET AT SAFE HOUSE B'
text_tokens = text.lower().split()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
replacements = 'fghijklmnopqrstuvwxyzabcde'

new_word = ''

for token in text_tokens:
    for l in token:
        print(l)
        index = alphabet.index(l)
        new_word += replacements[index]
    new_word += ' '

print(new_word)
