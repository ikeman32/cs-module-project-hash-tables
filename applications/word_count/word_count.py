def word_count(s):
    # Your code here
    count = {}
    ignore= ('.\'",')
    s = s.lower()
    for c in s:
        for i in ignore:
            if c == i:
                s = s.replace(i, '')

    s = list(s.split(' '))
    if not s:
        return count

    for w in s:
        if w not in count:
            count[w] = 1
        else:
            count[w] += 1
    
    return count
        



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))