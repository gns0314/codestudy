function solution(my_str, n) {
    var answer = [];
    for(let i=1; i<=Math.ceil(my_str.length/n); i++){
        answer.push(my_str.slice((i-1)*n,i*n))
    }
    return answer;
}