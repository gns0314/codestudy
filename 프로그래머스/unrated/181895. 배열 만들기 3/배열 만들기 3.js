function solution(arr, intervals) {
    var answer = [];
    for (i of intervals) {
        var j = i[0];
        var k = i[1];
        answer.push(arr.slice(j, k+1)); 
    }
    return answer.flat(); 
}