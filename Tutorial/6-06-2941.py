def word_iterator(word, length):
    if len(word) == 0:
        return length
    if len(word) == 1:
        return word_iterator(word[1:], length + 1)
    elif len(word) >= 2:
        if word[0] == 'c':
            if word[1] == '=':
                return word_iterator(word[2:], length + 1)
            elif word[1] == '-':
                return word_iterator(word[2:], length + 1)
            else:
                return word_iterator(word[1:], length + 1)
        elif word[0] == 'd':
            if len(word) >= 3:
                if word[1] == 'z' and word[2] == '=':
                    return word_iterator(word[3:], length + 1)
            if word[1] == '-':
                return word_iterator(word[2:], length + 1)
            else:
                return word_iterator(word[1:], length + 1)
        elif word[0] == 'l':
            if word[1] == 'j':
                return word_iterator(word[2:], length + 1)
            else:
                return word_iterator(word[1:], length + 1)
        elif word[0] == 'n':
            if word[1] == 'j':
                return word_iterator(word[2:], length + 1)
            else:
                return word_iterator(word[1:], length + 1)
        elif word[0] == 's':
            if word[1] == '=':
                return word_iterator(word[2:], length + 1)
            else:
                return word_iterator(word[1:], length + 1)
        elif word[0] == 'z':
            if word[1] == '=':
                return word_iterator(word[2:], length + 1)
            else:
                return word_iterator(word[1:], length + 1)
        else:
            return word_iterator(word[1:], length + 1)
print(word_iterator(input(), 0))