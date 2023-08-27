function solution(arr1, arr2) {
    var answer = 0;
    if(arr1.length == arr2.length){
        if(arr1.reduce((a,c)=>a+c,0) > arr2.reduce((b,d)=>b+d, 0)){
            answer = 1
        }
        else if (arr1.reduce((a,c)=>a+c,0) == arr2.reduce((b,d)=>b+d, 0)){
            answer = 0
        }
        else{
            answer = -1
        }
    }else if(arr1.length > arr2.length){
        answer = 1
    }
    else {
        answer = -1
    }
    return answer;
}