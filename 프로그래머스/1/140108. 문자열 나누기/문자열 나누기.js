function solution(s) {
    function count(s) {
        const x = s[0];
        let same = 0;
        let dif = 0;
        
        for (let i = 0; i < s.length; i++) {
            if (s[i] === x) {
                same++;
            } else {
                dif++;
            }
            
            if (same === dif) {
                break;
            }
        }
        
        return { same, dif };
    }
    
    const result = [];
    
    while (s.length > 0) {
        const { same, dif } = count(s);
        result.push(s.substr(0, same + dif));
        s = s.substr(same + dif);
    }
    
    return result.length;
}