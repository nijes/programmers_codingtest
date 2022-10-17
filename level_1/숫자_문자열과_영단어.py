def solution(s):
    word_dic = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4',\
                'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    for word in list(word_dic.keys()):
        s = s.replace(word, word_dic[word])
    return int(s)