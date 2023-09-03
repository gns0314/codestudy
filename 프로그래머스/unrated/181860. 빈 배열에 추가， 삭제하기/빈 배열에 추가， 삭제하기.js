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
            while(cnt < arr[i]){
                answer.pop()
                cnt += 1;
            }
        }
    }
    return answer;
}