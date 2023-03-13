def duplicate_count(text):
    # Your code goes here
    lst = []
    n=0
    if text == "" :
        return 0
    while n < len(text):
        txt = text.lower()
        lst.append(txt[n])
        n = n+1
    hand = {}
    for word in lst :
        hand[word] = hand.get(word, 0) + 1
    bigcount = 0
    for key, var in hand.items():
        if var > 1:
            bigcount = bigcount + 1
    return bigcount