"""https://programmers.co.kr/learn/courses/30/lessons/17680"""




"""
사용한 논리 및 오류:
초기 캐시크기는 전부 5초가 걸린다
반복문을 사용하여 해당 값이 안에 있으면 1초를 더한다
해당 값이 없으면 5초를 더하고 값을 변경한다 

한번 참조된 부분은 무조건 캐싱하는 것을 간과하여 계산하였다
"""




def solution(cacheSize, cities):
    count = 0

    cache = []

    if cacheSize == 0:
        return len(cities)*5

    for city in cities:
        city = city.lower()


        if city in cache:
            cache.remove(city)
            count += 1
            
        else:
            count += 5

        if len(cache) >= cacheSize:
            cache.pop(0)


        cache.append(city)

    return count


