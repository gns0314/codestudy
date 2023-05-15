def solution(myStr):
    answer = []
    split_str = ''
    for c in myStr:
        if c in ['a', 'b', 'c']:
            split_str += ' '
        else:
            split_str += c
    answer = split_str.strip().split()
    
    if not answer:
        answer = ['EMPTY']
        
    return answer