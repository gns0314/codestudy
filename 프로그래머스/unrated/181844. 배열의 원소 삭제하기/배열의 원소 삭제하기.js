function solution(arr, delete_list) {
    var answer = []
    for(i of arr){ 
        if(delete_list.includes(i) == false){
        answer.push(i)}
    } 
    return answer
    
}

