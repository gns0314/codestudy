def solution(my_string, letter):
    answer = [i for i in my_string if i != letter]
    return ''.join(answer)