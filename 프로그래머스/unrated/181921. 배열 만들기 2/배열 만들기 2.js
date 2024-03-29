function solution(l, r) {
    const answer = [];

    for (let num = l; num <= r; num++) {
        if(num == 0){
            continue
        }
        const numStr = num.toString();

        if (/^[05]+$/.test(numStr)) {
            answer.push(num);
        }
    }

    return answer.length === 0 ? [-1] : answer;
}