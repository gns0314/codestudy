from itertools import product

def solution(word):
    answer = 0
    word_list = list()
    words = ['A','E','I','O','U']
    
    for i in range(1,6):
        for j in product(words, repeat=i):
            word_list.append(list(j))
            
    word_list.sort()
    
    for k in word_list:
        answer += 1
        st = ''.join(s for s in k)
        if(word == st):
            break
    return answer