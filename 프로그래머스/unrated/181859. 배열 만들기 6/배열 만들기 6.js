function solution(arr) {
    var answer = [];
    let i = 0;
    while(i != arr.length){
        if(answer.length == 0){
            answer.push(arr[i])
        }else if(answer.slice(-1) == arr[i]){
            answer.pop()
        }else if(answer.slice(-1) != arr[i]){
            answer.push(arr[i])
        }
        i++;
    }
    return answer.length ? answer : [-1];
}