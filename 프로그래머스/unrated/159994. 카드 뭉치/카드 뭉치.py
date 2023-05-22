def solution(cards1, cards2, goal):
    def dfs(cards1, cards2, goal):
        if len(goal) == 0:
            return True

        if len(cards1) > 0 and cards1[0] == goal[0]:
            if dfs(cards1[1:], cards2, goal[1:]):
                return True

        if len(cards2) > 0 and cards2[0] == goal[0]:
            if dfs(cards1, cards2[1:], goal[1:]):
                return True

        return False

    if dfs(cards1, cards2, goal):
        return "Yes"
    else:
        return "No"