def solution(babbling):
    result = 0
    words = ['aya', 'ye', 'woo', 'ma']

    for bab in babbling:
        for word in words:
            if word * 2 not in bab:
                bab = bab.replace(word, ' ')

        if bab.isspace():
            result += 1

    return result