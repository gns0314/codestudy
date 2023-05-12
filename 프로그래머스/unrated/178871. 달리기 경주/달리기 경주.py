def solution(players, callings):
    player_indexes = {player: idx for idx, player in enumerate(players)}
    answer = players[:]
    for i, j in enumerate(callings):
        calling_idx = player_indexes[j]
        answer[calling_idx], answer[calling_idx-1] = answer[calling_idx-1], answer[calling_idx]
        player_indexes[j], player_indexes[answer[calling_idx]] = player_indexes[j]-1, calling_idx

    return answer