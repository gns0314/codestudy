from collections import deque

def solution(cacheSize, cities):
    l = [''] * cacheSize
    cache = deque(l, maxlen=cacheSize) # 길이 제한을 하고
    answer = 0
    for city in cities:
        city = city.lower() # 소문자로 다 바꾸고
        if city in cache: #cache hit
            cache.remove(city)
            cache.append(city)
            answer += 1
        else: #cache miss
            cache.append(city)
            answer += 5
    return answer