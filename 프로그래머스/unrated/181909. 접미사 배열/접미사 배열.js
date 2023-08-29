function solution(my_string) {
    const a = [];
    for (let i = 0; i < my_string.length; i++) {
        a.push(my_string.slice(-(i + 1)));
    }
    return a.sort();
}