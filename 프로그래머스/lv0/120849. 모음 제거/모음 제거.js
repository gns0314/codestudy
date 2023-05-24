function solution(my_string) {
    result = ''
  for (const s of my_string) {
    if (["a", "e", "i", "o", "u"].includes(s)) {
      continue;
    }
    result += s;
  }
    return result
}
