function solution(dots) {
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] = dots
    // 선분 12, 선분 34
    gradient_12 = Math.abs((y2 - y1) / (x2 - x1))
    gradient_34 = Math.abs((y4 - y3) / (x4 - x3))
    // 선분 13, 선분 24
    gradient_13 = Math.abs((y3 - y1) / (x3 - x1))
    gradient_24 = Math.abs((y4 - y2) / (x4 - x2))
    // 선분 23, 선분 14
    gradient_23 = Math.abs((y3 - y2) / (x3 - x2))
    gradient_14 = Math.abs((y4 - y1) / (x4 - x1))
   
    if(gradient_12 == gradient_34 || gradient_23 == gradient_14 || gradient_13 == gradient_24){
        return 1
    }
    return 0;
}