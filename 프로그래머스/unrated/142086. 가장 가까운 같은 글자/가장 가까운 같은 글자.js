function solution(s) {
    const answer = [];
    const a = [];

    for (let i = 0; i < s.length; i++) {
        if (!a.includes(s[i])) {
            answer.push(-1);
        } else {
            const lastIndex = a.lastIndexOf(s[i]);
            answer.push(i - lastIndex);
        }
        a.push(s[i]);
    }

    return answer;
}