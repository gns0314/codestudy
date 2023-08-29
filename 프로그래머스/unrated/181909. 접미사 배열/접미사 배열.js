function solution(my_string) {
    const answer = [];
    const a = [];
    for (let i = 0; i < my_string.length; i++) {
        a.push(my_string.slice(-(i + 1)));
    }
    answer.push(...a.sort());
    return answer;
}