function solution(array) {
    var answer = 0;
    let maxcount = 0;
    let count = {};
    // 딕셔너리에 해당 숫자가 몇개있는지 값을 추가  
    for (let i = 0; i < array.length; i++) {
        const num = array[i];
        if (count[num]) {
          count[num]++;
        } else {
          count[num] = 1;
        }
    }
    
    // 최빈값 구하기
    for (let j in count) {
        if (count[j] > maxcount) {
          maxcount = count[j];
          answer = parseInt(j);
        } else if (count[j] === maxcount) {
          answer = -1;
        }
  }
        
  return answer;
  }
    
