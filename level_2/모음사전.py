def solution(word):
    answer = 0
    vowel = 'AEIOU'
    for i in range(len(word)):
        answer += (vowel.find(word[i])*sum(5**j for j in range(5-i)) + 1)
    return answer