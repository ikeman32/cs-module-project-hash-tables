# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

def get_message():

    with open('ciphertext.txt', 'r') as ciphertext:
        msg = ciphertext.read()
    return msg

def get_index(index):
    for c in msg:
        if c >= 'A' and c <= 'Z':
            if c not in index:
                index[c] = 1
            else:
                index[c] += 1
    return index

def crack_it(ctext):
    global plain_text
    index_of_occurences = list(ctext.items())

    index_of_occurences.sort(key = lambda k: k[1], reverse=True)


    for i in range(26):
        key.update({index_of_occurences[i][0]:letters[i]})

    for l in msg:
        if not key.get(l):
            plain_text += l
        else:
            plain_text += key.get(l)

if __name__ == '__main__':
    letters = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
    plain_text = ''
    index = {}
    key = {}
    msg = get_message()
    index = get_index(index)
    crack_it(index)
    print(plain_text)