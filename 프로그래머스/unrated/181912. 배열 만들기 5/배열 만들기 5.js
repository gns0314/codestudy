function solution(intStrs, k, s, l) {
    var answer = [];
    for(i of intStrs){
        if(+(i.slice(s,s+l)) > k){
            answer.push(+(i.slice(s,s+l)))
        }
    }
    return answer;
}