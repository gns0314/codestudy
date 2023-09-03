function solution(arr, flag) {
    var answer = [];
    for(let i=0; i<flag.length; i++){
        let cnt = 0;
        if (flag[i] == true){
            while(cnt < arr[i]*2){
                answer.push(arr[i])
                cnt += 1;
            }
        }else{
            answer = answer.slice(0,(answer.length)-arr[i])
        }
    }
    return answer;
}