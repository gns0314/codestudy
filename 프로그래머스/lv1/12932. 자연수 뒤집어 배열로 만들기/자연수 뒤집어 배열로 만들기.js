function solution(n) {
    let arr = [...(n.toString())]
    const b = arr.length
    var answer = [];
    for(let i = 0; i<b; i++){
    answer.push(parseInt((arr.pop())))
    }
    return answer;
}