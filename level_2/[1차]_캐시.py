def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.append(city)
            cache.remove(city)
        else:
            answer += 5
            cache.append(city)
            if len(cache) > cacheSize:
                del cache[0]
    return answer