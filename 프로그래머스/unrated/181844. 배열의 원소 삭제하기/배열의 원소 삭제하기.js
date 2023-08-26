function solution(arr, delete_list) {
    const deleteSet = new Set(delete_list);

    const result = arr.filter(element => !deleteSet.has(element));
    
    return result;
}