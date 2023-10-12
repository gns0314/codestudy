function solution(num, total) {
    var answer = [];
    let avg = Math.ceil(total / num)
    if(num % 2 !== 0){
        for(let i = avg-(Math.floor(num/2)); i<= avg+Math.floor(num/2); i++)
            answer.push(i)
    }
    else{
        for(let i = avg-(Math.floor(num/2)); i<= avg+Math.floor(num/2)-1; i++)
            answer.push(i)
    }
    return answer;
}