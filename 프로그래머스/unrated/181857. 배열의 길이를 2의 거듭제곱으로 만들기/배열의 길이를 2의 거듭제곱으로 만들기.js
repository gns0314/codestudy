function solution(arr) {
  const length = arr.length;
  let newlength = 1;

  while (newlength < length) {
    newlength *= 2;
  }

  const zero = newlength - length;
  const result = arr.concat(new Array(zero).fill(0));

  return result;
}