def no_dups(s):
    # Your code here
    s = s.split()
    no_duplicate_words = ''
    for words in s:
        if words not in no_duplicate_words:
            if no_duplicate_words == '':
                no_duplicate_words += words
            else:
                no_duplicate_words += ' ' + words
    return no_duplicate_words


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))