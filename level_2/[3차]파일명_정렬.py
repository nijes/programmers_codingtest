import re

def solution(files):
    return sorted(files, key = lambda x : (re.match('^\D+', x)[0].lower(), int(re.search('\d+', x)[0])))