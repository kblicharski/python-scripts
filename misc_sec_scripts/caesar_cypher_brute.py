key = 'abcdefghijklmnopqrstuvwxyz'

def decrypt(n, text):
    result = ''
    for letter in text:
        try:
            i = (key.index(letter) - n) % 26
            result += key[i]
        except ValueError:
            result += letter
    return result
