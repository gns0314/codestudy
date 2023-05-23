import re
def solution(my_string):
    return re.sub('[aioeu]','',my_string)