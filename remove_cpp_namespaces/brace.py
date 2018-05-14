def find_matching_brace(text):
    count = 0
    for i, c in enumerate(text):
        if c == '{':
            count += 1
        elif c == '}':
            count -= 1

        if count == 0:
            return i

    return -1

def get_inner_text(text):
    fbi = text.find('{')
    if fbi == -1:
        return ''

    mbi = find_matching_brace(text[fbi:])
    if mbi == -1 or mbi == 1:
        return ''

    return text[(fbi+1):(fbi+mbi)]
