def solution(s):
    result = []
    words = s.split(" ")
    for i in words:
        if i != '' and i[0].isalpha():
            result.append(i[0].upper() + i[1:].lower())
        else:
            result.append(i.lower())
    return ' '.join(result)