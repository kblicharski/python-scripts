def getBook(file):
    with open(file) as f:
        contents = f.readlines()
    return ''.join([line for line in contents if line != '\n' and line != '' and not line.isupper()])


def cleanup(text):
    replace_mapping = {"'s": "", "!": ".", "?": "."}
    bad_characters = "(),-:;\'\"*_"

    for mapping in replace_mapping:
        text = text.replace(mapping, replace_mapping[mapping])
    output = [c for c in text if c not in bad_characters and c != '']
    output_string = ''.join(output)
    return output_string


def extractWords(text):
    '''
    '''
    return sorted([word.lower().replace('.','') for word in text.split()])


def extractSentences(text):
    '''
    sentences = text.split('.')
    no_spaces = [sentence.strip() for sentence in sentences]
    no_blanks = [sentence for sentence in no_spaces if sentence != '']
    '''
    return [sentence.strip() for sentence in text.split('.') if sentence.strip() != '']


def countSyllables(word):
    if word.endswith('e') or word.endswith('s'):
        word = word[:-1]

    vowels = 'aeiou'
    num_syllables = 0
    old_letter = 'a'

    try:
        if word[0] in vowels:
            num_syllables += 1
    except Exception:
        return 0

    for letter in word.lower():
        if old_letter not in vowels and (letter in vowels or letter == 'y'):
            num_syllables += 1
        old_letter = letter

    if num_syllables == 0:
        num_syllables = 1
        
    return num_syllables


def ars(text):
    words = extractWords(text)
    sentences = extractSentences(text)

    character_count = sum(len(word) for word in words)
    cpw = character_count / len(words) 

    sentence_word_count = sum(len(sentence.split()) for sentence in sentences)
    wps = sentence_word_count / len(sentences)
    
    return 4.71*cpw + 0.5*wps - 21.43


def fki(text):
    words = extractWords(text)
    sentences = extractSentences(text)
    # print([word for word in words if len(word) < 1])

    wps = sum(len(sentence.split()) for sentence in sentences) / len(sentences)
    spw = sum(countSyllables(word) for word in words) / len(words)

    return 0.39 * wps + 11.8 * spw - 15.59


def cli(text):
    """Average Number of characters per 100 words and average number of sentences per 100 words"""
    words = extractWords(text)
    sentences = extractSentences(text)
    print(len(words))

    # This is the current word we have looked at
    num_words = 0

    # This is the running count of characters
    character_count = 0

    # This is going to keep track of our segments
    character_counts = []

    for word in words:
        # We have looked at a word
        num_words += 1
        # Add its characters to the running count
        character_count += len(word)

        # Restart per 100 words
        if num_words == 100:
            character_counts.append(character_count)
            character_count = 0
            num_words = 0

    # We have counted the segments, now find the average
    cphw = sum(character_counts) / len(character_counts)

    num_words = 0
    sentence_count = 0
    sentence_counts = []

    for sentence in sentences:
        sentence_words = sentence.split()

        for word in sentence_words:
            num_words += 1
        
        sentence_count += 1
        
        if num_words >= 100:
            sentence_counts.append(sentence_count)
            sentence_count = 0
            num_words = 0
        
    sphw = sum(sentence_counts) / len(sentence_counts)
    
    return 0.0588 * cphw - 0.296 * sphw - 15.8

def evalBook(filename):
    book = getBook(filename)
    clean_book = cleanup(book)

    print(filename.upper())
    print("ARS: {}".format(ars(clean_book)))
    print("FKI: {}".format(fki(clean_book)))
    print("CLI: {}".format(cli(clean_book)))
    print("*"*50)

evalBook('test.txt')
evalBook('wind.txt')
evalBook('iliad.txt')
