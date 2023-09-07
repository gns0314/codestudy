function solution(n) {
    let num = n**(1/2)
    if(Number.isInteger(num)){
       return 1
    }else{
        return 2
    }
}