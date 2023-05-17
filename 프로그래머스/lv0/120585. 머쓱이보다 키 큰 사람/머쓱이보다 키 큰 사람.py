def solution(array, height):
    answer = len(list(filter(lambda x:x>height,array)))
    return answer