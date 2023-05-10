def solution(todo_list, finished):
    answer = []
    for i in range(len(finished)):
        if finished[i] == 0:
            answer.append(todo_list[i])
    return answer

# 리스트컴프리헨션시
def solution(todo_list, finished):
    answer = [todo_list[i] for i in range(len(finished)) if finished[i] == 0]
    return answer
