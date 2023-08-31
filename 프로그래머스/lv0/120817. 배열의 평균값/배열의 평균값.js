function solution(numbers) {
    var answer = 0;
    answer = numbers.reduce((a,c) => a+c, 0)/ numbers.length
    return answer;
}