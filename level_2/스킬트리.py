def solution(skill, skill_trees):
    answer = len(skill_trees)
    for tree in skill_trees:
        skill_list = list(skill)
        for s in tree:
            if s in skill_list and s != skill_list.pop(0):
                answer -= 1
                break
    return answer