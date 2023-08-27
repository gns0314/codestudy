function solution(arr) {
    var answer = [];
    for(i of arr){
        var cnt = 0
        while(cnt != i){
            cnt += 1
            answer.push(i)
        }
    }
    return answer;
}