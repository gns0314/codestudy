function solution(arr, divisor) {
    var answer = [];
    //1.나누기
    for(let i=0; i<arr.length; i++){
        if(arr[i]%divisor === 0){ //몫이 있을때
            answer.push(arr[i]);
        }
    }
    if (answer.length === 0){
        answer = [-1];
    }
    //2.오름차순정렬
    return answer.sort((a,b)=>a-b);
}