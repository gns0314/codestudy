def solution(numbers):
    num_dic = {0:0, 1:0, 2:0 ,3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0 }
    for i in numbers:
        num_dic[i] += 1
    num_list= list(filter(lambda x:x[1]<1, num_dic.items()))
    sum_num = sum([j[0] for j in num_list])
    return sum_num