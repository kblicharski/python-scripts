key = 'abcdefghijklmnopqrstuvwxyz'
references = ['ucffng', 'tfbuqptu', 'gvero', 'cnkkr', 'gfwxyjr', 'fkdlq']  
offsets = [2, 1, 4, 6, 5, 3]


def decrypt(n, text):
    result = ''

    for letter in text:
        try:
            i = (key.index(letter) - n) % 26
            result += key[i]
        except ValueError:
            result += letter
    return result

offset_index = 0
for reference in references:
    print(decrypt(offsets[offset_index], reference))
    offset_index += 1
    
