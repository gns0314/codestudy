def solution(s):
    # 문자열 s에서 필요한 정보만 추출하기 위해 중괄호와 숫자만 남기고 나머지 문자 제거
    s = s[2:-2].split('},{')
    
    # 길이 순으로 정렬
    s.sort(key=lambda x: len(x))
    
    answer = []
    for element in s:
        # 각 원소를 숫자로 변환하여 리스트에 추가
        nums = element.split(',')
        for i in nums:
            if int(i) not in answer:
                answer.append(int(i))
    
    return answer